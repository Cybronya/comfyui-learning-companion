# workflow>模型加载区

## 节点类型

`workflow>模型加载区`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_path:COMBO`（1 次）
- `cache_threshold:FLOAT`（1 次）
- `attention:COMBO`（1 次）
- `cpu_offload:COMBO`（1 次）
- `device_id:INT`（1 次）
- `data_type:COMBO`（1 次）
- `i2f_mode:COMBO`（1 次）
- `model_type:COMBO`（1 次）
- `text_encoder1:COMBO`（1 次）
- `text_encoder2:COMBO`（1 次）

## 输出

- `MODEL:MODEL`（1 次）
- `CLIP:CLIP`（1 次）
- `噪波生成:NOISE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["svdq-int4_r32-flux.1-kontext-dev.safetensors", 0, "nunchaku-fp16", "auto", 0, "bfloat16", "enabled", "flux.1", "clip_l`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
