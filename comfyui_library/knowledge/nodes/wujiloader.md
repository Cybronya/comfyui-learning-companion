# WujiLoader

## 节点类型

`WujiLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `外部模型:MODEL`（2 次）
- `unet模型:COMBO`（2 次）
- `权重精度:COMBO`（2 次）
- `计算精度:COMBO`（2 次）
- `ckpt模型:COMBO`（2 次）
- `clip模型1:COMBO`（2 次）
- `clip模型2:COMBO`（2 次）
- `clip类型:COMBO`（2 次）
- `vae模型:COMBO`（2 次）
- `视觉模型:COMBO`（2 次）

## 输出

- `model:MODEL`（2 次）
- `clip:CLIP`（2 次）
- `vae:VAE`（2 次）
- `clip_vision:CLIP_VISION`（2 次）
- `control_net:CONTROL_NET`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Qwen-Image_2512.safetensors", "自动 (Auto)", "bf16", "关闭", "qwen_2.5_vl_7b_fp8_scaled.safetensors", "关闭", "qwen_image", `（1 次）
- `["RedZDX-ZIB-Distilled-nocfg-10steps-fp8-e4m3fn.safetensors", "自动 (Auto)", "bf16", "关闭", "qwen_3_4b.safetensors", "关闭", `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
