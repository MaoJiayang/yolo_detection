import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# 下载函数
def download_file(url, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    local_filename = os.path.join(dest_folder, url.split('/')[-1])
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total = int(r.headers.get('content-length', 0))
        with open(local_filename, 'wb') as f, tqdm(
            desc=local_filename,
            total=total,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for chunk in r.iter_content(chunk_size=1024):
                size = f.write(chunk)
                bar.update(size)
    return local_filename

# 数据集链接
urls = [
    "https://dl.cv.ethz.ch/bdd100k/data/bdd100k_det_20_labels_trainval.zip",
    "https://dl.cv.ethz.ch/bdd100k/data/100k_images_val.zip",
    "https://dl.cv.ethz.ch/bdd100k/data/100k_images_train.zip",
    "https://dl.cv.ethz.ch/bdd100k/data/100k_images_test.zip"
]

destination_folder = "datasets"

# 使用线程池同时下载
with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(download_file, url, destination_folder) for url in urls]
    for future in as_completed(futures):
        try:
            file = future.result()
            print(f"{file} 下载完成.")
        except Exception as e:
            print(f"下载失败: {e}")