import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from PIL import Image, ImageDraw, ImageFont
import storage

import datetime


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

data = None


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global data
    data.add_user_to_list(user_id=update.effective_chat.id, time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("Current list users with dates: \n", data.get_users_with_dates(), "\n")
    await send_message(chat_id=update.effective_chat.id, context=context)


async def send_message(chat_id: int, context: ContextTypes.DEFAULT_TYPE):
    offset = datetime.timezone(datetime.timedelta(hours=3))
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    im = Image.open('cat.jpg')
    font_type = ImageFont.truetype('Arial.ttf', 70)
    draw_text = ImageDraw.Draw(im)
    width = im.width
    height = im.height
    # Положение текста нужно подбирать самому
    draw_text.text(
        xy=(width // 6, height * 4 // 5),
        text=current_time,
        fill='white',
        font=font_type
    )
    im.save('cat_with_cur_time.png')
    await context.bot.send_photo(
        chat_id=chat_id,
        photo='cat_with_cur_time.png'
    )


def main(store: storage.Store, TOKEN):
    application = ApplicationBuilder().token(TOKEN).build()
    global data
    data = store
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()