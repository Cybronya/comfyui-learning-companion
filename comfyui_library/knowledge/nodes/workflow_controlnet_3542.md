# workflow/ControlNet加载器

## 节点类型

`workflow/ControlNet加载器`

## 分类

Conditioning

## 作用

ControlNet 控制类节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）

## 输出

- `ControlNet:CONTROL_NET`（2 次）
- `ControlNetLoader ControlNet:CONTROL_NET`（2 次）
- `ControlNetLoader 2 ControlNet:CONTROL_NET`（1 次）
- `图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["controlnet-tile-sdxl-1.0-xinsir.safetensors", "controlnet-depth-sdxl-1.0-xinsir.safetensors", "controlnet-openpose-sdx`（1 次）
- `["MistoLine/mistoLine_rank256.safetensors", "control-lora-depth-rank256.safetensors", "DepthAnythingV2Preprocessor", 102`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
