# MultipleLoraLoader5|cgem156

## 节点类型

`MultipleLoraLoader5|cgem156`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `clip_optional:CLIP`（2 次）
- `normalize:BOOLEAN`（2 次）
- `normalize_sum:FLOAT`（2 次）
- `lora_name_0:COMBO`（2 次）
- `strength_model_0:FLOAT`（2 次）
- `apply_0:BOOLEAN`（2 次）
- `lora_name_1:COMBO`（2 次）
- `strength_model_1:FLOAT`（2 次）
- `apply_1:BOOLEAN`（2 次）

## 输出

- `MODEL:MODEL`（2 次）
- `CLIP:CLIP`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, 1, "None", 0.8000000000000002, true, "None", 0.6000000000000001, false, "None", 0.7300000000000001, false, "None`（1 次）
- `[false, 1, "None", 0.8000000000000002, true, "None", 0.6000000000000001, false, "None", 0.5000000000000001, false, "None`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
