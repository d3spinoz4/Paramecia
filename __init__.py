#!/path/to/python/env
from multiprocessing import shared_memory
from scipy.interpolate import interp1d
from .eigentransform import runcol
from flask_executor import Executor
from flask import Flask, request
import multiprocessing
import cython_eigenx
from io import BytesIO
import multiprocessing
import numpy as np
import mariadb
import pickle
import urllib
import flask
import time
import mmap
import json
import cv2
import sys
import os


def updatequery(taskid, elapsed_time):

    conn = mariadb.connect(
        user="userJDE",
        password="hsomeMmx5Weird6FN4PasswordGHpYouMXDon'tOlKnow",
        host="localhost",
        database="sampledbName")
    cur = conn.cursor()

    some_name = taskid
    some_time = elapsed_time
    cur.execute("SELECT text,day FROM tasks WHERE id=?", (some_name,))

    for taskname, taskday in cur:
        print(f"Task name: {taskname}, Day: {taskday}")

    try:
        cur.execute("UPDATE tasks SET reminder=1, time = ? WHERE id = ?", (elapsed_time, some_name,))
    except mariadb.Error as e:
        print(f"Error: {e}")

    conn.commit()
    conn.close()

def runstream(buffname, width, height):

    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    rows = [(i, buffname, width, height) for i in range(0, height)]

    mandelImg = pool.map(runcol, rows)
    pool.close()
    pool.join()

    last_buff = shared_memory.SharedMemory(name=f'{buffname}-2')
    leimgbuff = np.ndarray((height, width), dtype=np.uint8, buffer=last_buff.buf)

    eigimg_sorted_small_32_avg_r = np.floor((interp1d([leimgbuff.min(), leimgbuff.max()], [0.0, 256.0 - 1e-4]))(leimgbuff))
    last_buff.unlink()
    return eigimg_sorted_small_32_avg_r.astype(np.uint8)

app = Flask(__name__)

executor = Executor(app)

@app.route('/frames/<int:x>/<int:y>', methods=['GET', 'POST'])
def frames(x, y):
    if request.method == 'POST':
        reqstr = request.stream.read()
        dstr = urllib.parse.unquote(reqstr, encoding='utf-8', errors='replace')
        bytem = bytes(reqstr)
        bimg = BytesIO(bytem)
        shm_buff = shared_memory.SharedMemory(create=True, size=len(bytem))
        shm_buff.buf[:] = bimg.read()
        shmb_name = shm_buff.name
        eigimg_buff = shared_memory.SharedMemory(create=True, size=len(bytem), name=f'{shmb_name}-2')
        img = runstream(shmb_name, x, y)
        response = flask.make_response(img.tobytes())
        shm_buff.unlink()

        return response
