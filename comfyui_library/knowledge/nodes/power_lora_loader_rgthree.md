# Power Lora Loader (rgthree)

## 节点类型

`Power Lora Loader (rgthree)`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（3 次）
- `clip:CLIP`（3 次）
- `Power Lora Loader:Power Lora Loader`（2 次）
- `model_weight_1:FLOAT`（1 次）
- `clip_weight_1:FLOAT`（1 次）
- `lora_name_1:COMBO`（1 次）
- `model_weight_2:FLOAT`（1 次）
- `clip_weight_2:FLOAT`（1 次）
- `lora_name_2:COMBO`（1 次）
- `model_weight_3:FLOAT`（1 次）

## 输出

- `MODEL:MODEL`（3 次）
- `CLIP:CLIP`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.4000000000000001, true, "Krea2snowFstyle_c1-st8000.safetensors", 0.20000000000000004, 1.0000000000000002, "Krea2SnowZ`（1 次）
- `[1, 1, "FLUX.1-Turbo-Alpha.safetensors", 0.33, 0.33, "openflux1-v0.1.0-fast-lora.safetensors", 0.5, 0.5, "realism_lora.s`（1 次）
- `[1, 1, "FLUX.1-Turbo-Alpha.safetensors", 0.33, 0.33, "openflux1-v0.1.0-fast-lora.safetensors", 0, 0, "openflux1-v0.1.0-f`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
