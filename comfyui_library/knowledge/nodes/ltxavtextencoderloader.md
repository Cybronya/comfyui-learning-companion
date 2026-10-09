# LTXAVTextEncoderLoader

## 节点类型

`LTXAVTextEncoderLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `text_encoder:COMBO`（2 次）
- `ckpt_name:COMBO`（2 次）
- `device:COMBO`（1 次）

## 输出

- `CLIP:CLIP`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["gemma_3_12B_it.safetensors", "ltx-2-19b-dev-fp8.safetensors"]`（1 次）
- `["gemma_3_12B_it_fp8_e4m3fn.safetensors", "ltx-2.3-22b-dev.safetensors", "default"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
