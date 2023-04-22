"""
✘ **Bantuan Untuk Webshot**

๏ **Perintah:** `adzan` <nama kota>
◉ **Keterangan:** Dapatkan jadwal adzan.
"""
import json

import requests
from . import *

@ayra_cmd(pattern="(A|a)dzan( (.*)|$)")
async def get_adzan(e):
    LOKASI = e.pattern_match.group(1)
    if not LOKASI:
        await e.eor("<i>Silahkan Masukkan Nama Kota Anda</i>")
        return True
    url = f"http://muslimsalat.com/{LOKASI}.json?key=bd099c5825cbedb9aa934e255a81a5fc"
    request = requests.get(url)
    if request.status_code != 200:
        return await eor(e, get_string("adzan1").format(LOCATION), time=120
                               )
    result = json.loads(request.text)
    catresult = f"<b>Jadwal Shalat Hari Ini:</b>\
            \n<b>📆 Tanggal </b><code>{result['items'][0]['date_for']}</code>\
            \n<b>📍 Kota</b> <code>{result['query']}</code> | <code>{result['country']}</code>\
            \n\n<b>Terbit  : </b><code>{result['items'][0]['shurooq']}</code>\
            \n<b>Subuh : </b><code>{result['items'][0]['fajr']}</code>\
            \n<b>Zuhur  : </b><code>{result['items'][0]['dhuhr']}</code>\
            \n<b>Ashar  : </b><code>{result['items'][0]['asr']}</code>\
            \n<b>Maghrib : </b><code>{result['items'][0]['maghrib']}</code>\
            \n<b>Isya : </b><code>{result['items'][0]['isha']}</code>\
    "
    await eor(e, catresult, "html")
