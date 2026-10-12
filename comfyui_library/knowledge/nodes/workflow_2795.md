# workflow/视频

## 节点类型

`workflow/视频`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `audio:AUDIO`（1 次）
- `visualizer:MODEL_VISUAL_E`（1 次）
- `video_images:IMAGE`（1 次）
- `批次管理:VHS_BatchManager`（1 次）
- `VHS_VideoCombine vae:VAE`（1 次）
- `video:IMAGE`（1 次）
- `插值规则(可选):INTERPOLATION_STATES`（1 次）

## 输出

- `visualizer:MODEL_VISUAL_E`（1 次）
- `IMAGE:IMAGE`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `文件名:VHS_FILENAMES`（1 次）
- `poses:IMAGE`（1 次）
- `图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["stabilityai/sd-vae-ft-mse", true, "audio_drived", false, false, false, "V2", 768, 768, "nearest", "fill / crop", "alwa`（1 次）
- `[7, "fixed", 30, false, false, 2, 32, 1, 8, 180, 512, 0.8, "rife47.pth", 10, 2, true, true, 1, "nearest-exact", 900, 160`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
