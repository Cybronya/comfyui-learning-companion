# NunchakuFluxDiTLoader

## 节点类型

`NunchakuFluxDiTLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model_path:COMBO`（2 次）
- `cache_threshold:FLOAT`（2 次）
- `attention:COMBO`（2 次）
- `cpu_offload:COMBO`（2 次）
- `device_id:INT`（2 次）
- `data_type:COMBO`（2 次）
- `i2f_mode:COMBO`（2 次）

## 输出

- `MODEL:MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["svdq-int4_r32-flux.1-krea-dev.safetensors", 0.15000000000000002, "nunchaku-fp16", "auto", 0, "bfloat16", "enabled"]`（1 次）
- `["svdq-int4-flux.1-dev", 0, "nunchaku-fp16", "auto", 0, "bfloat16", "enabled"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
