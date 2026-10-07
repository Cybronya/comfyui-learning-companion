# SUPIR_model_loader_v2

## 节点类型

`SUPIR_model_loader_v2`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `clip:CLIP`（1 次）
- `vae:VAE`（1 次）

## 输出

- `SUPIR_model:SUPIRMODEL`（1 次）
- `SUPIR_VAE:SUPIRVAE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["SUPIR-v0Q_fp16.safetensors", false, "auto", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
