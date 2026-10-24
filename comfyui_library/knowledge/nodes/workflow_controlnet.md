# workflow/ControlNet

## 节点类型

`workflow/ControlNet`

## 分类

Conditioning

## 作用

ControlNet 控制类节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `正面条件:CONDITIONING`（2 次）
- `负面条件:CONDITIONING`（2 次）
- `图像:IMAGE`（2 次）
- `vae:VAE`（2 次）
- `image:IMAGE`（1 次）
- `AV_ControlNetPreprocessor image:IMAGE`（1 次）
- `AV_ControlNetPreprocessor 2 image:IMAGE`（1 次）
- `AV_ControlNetPreprocessor 3 image:IMAGE`（1 次）
- `AV_ControlNetPreprocessor 4 image:IMAGE`（1 次）
- `AV_ControlNetPreprocessor 5 image:IMAGE`（1 次）

## 输出

- `正面条件:CONDITIONING`（2 次）
- `负面条件:CONDITIONING`（2 次）
- `CNET_NAME:STRING`（1 次）
- `AV_ControlNetPreprocessor CNET_NAME:STRING`（1 次）
- `IMAGE:IMAGE`（1 次）
- `AV_ControlNetPreprocessor 2 CNET_NAME:STRING`（1 次）
- `AV_ControlNetPreprocessor 3 CNET_NAME:STRING`（1 次）
- `AV_ControlNetPreprocessor 4 CNET_NAME:STRING`（1 次）
- `AV_ControlNetPreprocessor 5 CNET_NAME:STRING`（1 次）
- `AV_ControlNetPreprocessor 6 CNET_NAME:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["normalmap_bae", "sdxl", 512, "None", "scribble", "sdxl", 512, "None", "hed", "sdxl", 512, "None", "openpose", "sdxl", `（1 次）
- `["control_v11f1e_sd15_tile_fp16.safetensors", 0.5, 0, 0.8]`（1 次）
- `["control-lora-depth-rank256.safetensors", "control-lora-canny-rank256.safetensors", 6.283185307179586, 0.1, 1024, "disa`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
