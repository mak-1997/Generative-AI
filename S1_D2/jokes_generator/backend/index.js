const express = require("express");
require("dotenv").config();
const cors = require("cors");
const { Configuration, OpenAIApi } = require("openai");

const app = express();

app.options("*", cors());
app.use(express.json());
app.use(cors({ origin: "*" }));

const configuration = new Configuration({
  apiKey: process.env.OPEN_AI_KEY,
});
const openai = new OpenAIApi(configuration);

app.post("/", async (req, res) => {
  const { type, keywords } = req.body;
  try {
    const response = await openai.createCompletion({
      engine: "text-davinci-003",
      prompt: `Create a ${type} using these keywords -> ${keywords}.`,
      maxTokens: 256,
      temperature: 1,
      n: 1,
      top_p: 1,
      frequency_penalty: 0,
      presence_penalty: 0,
      stop: "\n",
    });

    const data = response.choices[0].text.trim();
    console.log(data);
    res.status(200).send({ data });
  } catch (error) {
    console.log(`Error generating ${type}: `, error);
    res.status(500).send({ msg: error.message });
  }
});

app.listen(process.env.PORT, async () => {
  console.log(`Server is running on port ${process.env.PORT}`);
});
