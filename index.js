const express = require("express");
const path = require("path");
const TelegramBot = require("node-telegram-bot-api");
const TOKEN = "5752732229:AAFCsQbXvVaCN1MhJBynhQgQMHq_8yYWUbw";
const server = express();
const bot = new TelegramBot(TOKEN, { polling: true } );
const port = process.env.PORT || 5000;
const gameName = "SHORT_NAME_YOUR_GAME";
const queries = {};

server.use(express.static(path.join(__dirname, 'public')));

bot.onText(/start|game/, (msg) => bot.sendGame(msg.from.id, gameName));
bot.onText(/start|game/, (msg) => bot.sendGame(msg.from.id, gameName));

bot.on("callback_query", function (query) {
  if (query.game_short_name !== gameName) {
    bot.answerCallbackQuery(query.id, "Sorry, '" + query.game_short_name + "' is not available.");
  } else {
    queries[query.id] = query;
    let gameurl = "https://YOUR_URL_HERE/index.html?  id="+query.id;
    bot.answerCallbackQuery({
      callback_query_id: query.id,
      url: gameurl
    });
  }
});

server.listen(port);
