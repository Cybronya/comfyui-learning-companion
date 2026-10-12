# LowVRAMLatentUpscaleModelLoader

## 节点类型

`LowVRAMLatentUpscaleModelLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `dependencies:*`（3 次）
- `model_name:COMBO`（3 次）

## 输出

- `LATENT_UPSCALE_MODEL:LATENT_UPSCALE_MODEL`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ltx-2-spatial-upscaler-x2-1.0.safetensors"]`（2 次）
- `["ltx-2.3-spatial-upscaler-x2-1.1.safetensors"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
