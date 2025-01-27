from mmdet3d.apis import init_detector, inference_detector

config_file = 'configs/pointpillars/hv_pointpillars_secfpn_6x8_160e_kitti-3d-car.py'
checkpoint_file = 'checkpoints/hv_pointpillars_secfpn_6x8_160e_kitti-3d-car_20200620_230614-77663cd6.pth'

# build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device='cuda:0')

# test a single image and show the results
# point_cloud = 'demo/kitti_000008.bin'
point_cloud = 'demo/000004.bin'
result, data = inference_detector(model, point_cloud)
# visualize the results and save the results in 'results' folder
model.show_results(data, result, out_dir='results')