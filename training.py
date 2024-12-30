# %%
from ultralytics import YOLO

# %%
# model = YOLO("yolo11m.pt")
model = YOLO("yolo11l.pt")
# %%
# results = model.train(data="datasets/bdd100k_det/bdd100K_det_yolo11.yaml", epochs=50,device='0,1',plots=True, name = 'yolo11m1229')
results = model.train(data="datasets/bdd100k_det/bdd100K_det_yolo11.yaml", epochs=10,device='0,1',plots=True,name = 'yolo11l1230')


