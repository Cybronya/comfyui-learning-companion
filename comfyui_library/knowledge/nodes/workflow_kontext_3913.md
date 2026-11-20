# workflow>双截棍kontext

## 节点类型

`workflow>双截棍kontext`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `图像:IMAGE`（3 次）
- `vae_name:COMBO`（3 次）
- `model_path:COMBO`（3 次）
- `cache_threshold:FLOAT`（3 次）
- `attention:COMBO`（3 次）
- `cpu_offload:COMBO`（3 次）
- `device_id:INT`（3 次）
- `data_type:COMBO`（3 次）
- `i2f_mode:COMBO`（3 次）
- `model_type:COMBO`（3 次）

## 输出

- `图像:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ae.safetensors", "svdq-int4_r32-flux.1-kontext-dev.safetensors", 0.12000000000000002, "nunchaku-fp16", "auto", 0, "bfl`（1 次）
- `["ae.safetensors", "svdq-int4_r32-flux.1-kontext-dev.safetensors", 0.12000000000000002, "nunchaku-fp16", "auto", 0, "bfl`（1 次）
- `["ae.safetensors", "svdq-int4_r32-flux.1-kontext-dev.safetensors", 0.12000000000000002, "nunchaku-fp16", "auto", 0, "bfl`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
