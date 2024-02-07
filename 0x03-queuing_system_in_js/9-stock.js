const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const app = express();
const client = redis.createClient();

const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

const getItemById = (id) => listProducts.find((item) => item.itemId === id);

const reserveStockById = (itemId, stock) => {
  const key = `item.${itemId}`;
  client.set(key, stock);
};

const getCurrentReservedStockById = promisify(async (itemId) => {
  const key = `item.${itemId}`;
  const result = await client.get(key);
  return parseInt(result) || 0;
});

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    res.json({ status: 'Product not found' });
  } else {
    const currentQuantity = await getCurrentReservedStockById(itemId);
    res.json({ ...item, currentQuantity });
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    res.json({ status: 'Product not found' });
  } else {
    const currentQuantity = await getCurrentReservedStockById(itemId);

    if (currentQuantity === item.initialAvailableQuantity) {
      res.json({ status: 'Not enough stock available', itemId });
    } else {
      reserveStockById(itemId, currentQuantity + 1);
      res.json({ status: 'Reservation confirmed', itemId });
    }
  }
});

const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
