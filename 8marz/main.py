import asyncio
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import Message, FSInputFile

from state_machine import StateMachine
from questions import questions


load_dotenv()

bot = Bot(token=os.environ.get("TOKEN"))
sm = StateMachine()
dp = Dispatcher()

buttons = []
for i in range(3):
    buttons.append([KeyboardButton(text=str(i+1))])
kb = ReplyKeyboardMarkup(
    keyboard=buttons,
    resize_keyboard=True
)

@dp.message(Command("start"))
async def cmd_start(message):
    user_id = message.chat.id
    if user_id not in sm.state_dict.keys():
        sm.state_dict[user_id] = [0, "Гость", "Anastasia.mp4", "BAACAgIAAxkDAAIBg2fLTKnEN4SreHxtAzXOFcP9rN6BAAJacAACtrdgSlw4FudXV1uYNgQ"]
    if user_id in sm.state_dict.keys():
        name = sm.state_dict[user_id][1]
        video_url = 'video/'+sm.state_dict[user_id][2]
        sm.state_dict[user_id][0] = 1
        question = questions[0]
        question_text = question.get("question")
        for i, option in enumerate(question.get("options")):
            question_text += "\n" + str(i+1) + ". " + option
        await message.answer(f"{name}, рады тебя видеть!")
        await bot.send_video(user_id, sm.state_dict[user_id][3])
        await message.answer(question_text, reply_markup=kb)


@dp.message()
async def text(message):
    user_id = message.chat.id
    if user_id in sm.state_dict.keys():
        state = sm.state_dict[user_id][0]
        name = sm.state_dict[user_id][1]
        if sm.state_dict[user_id][0] == len(questions) + 1:
            await message.answer("Игра окончена! /start для перезапуска")
        else:
            if message.text in ("1", "2", "3"):
                question = questions[state-1]
                if question.get("options")[int(message.text)-1] == question.get("correct_answer"):
                    await message.answer("Правильно!")
                else:
                    await message.answer(f"Неправильно! Ответ: {question.get('correct_answer')}")
                sm.state_dict[user_id][0] += 1
                if sm.state_dict[user_id][0] == len(questions) + 1:
                    await message.answer("С завершением квиза! А вот и обещанная награда)\nhttps://vkvideo.ru/video280364165_456241018?list=ln-6NZmhT9MKEwNzijiIm", reply_markup=ReplyKeyboardRemove())
                else:
                    question = questions[sm.state_dict[user_id][0]-1]
                    question_text = question.get("question")
                    for i, option in enumerate(question.get("options")):
                        question_text += "\n" + str(i+1) + ". " + option
                    await message.answer(question_text)
            else:
                await message.answer(f"{name}, воспользуйся кнопками внизу!")
    else:
        await message.answer("Выполни /start для перезапуска!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())