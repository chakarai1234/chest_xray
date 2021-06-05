const express = require("express");
const cors = require("cors");

const app = express();

const PORT = process.env.PORT || 80;

app.use(cors());
app.use("/chest_xray", express.static(__dirname + "/model_for_web"));

app.get("/", (req, res) => {
  res.send("hello Backend");
});

app.listen(PORT, () => {
  console.log("Connected to the Port 80");
});
