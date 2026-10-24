# OSMLoraLoader

## 节点类型

`OSMLoraLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（36 次）
- `clip:CLIP`（36 次）
- `enable_flag:INT`（36 次）
- `lora_name:COMBO`（36 次）
- `weight_min:FLOAT`（36 次）
- `weight_max:FLOAT`（36 次）
- `seed:INT`（36 次）

## 输出

- `model:MODEL`（36 次）
- `clip:CLIP`（36 次）
- `applied_weight:FLOAT`（36 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, "klein\\klein-电影海报.safetensors", 0.1, 1, 4036730380, "randomize"]`（1 次）
- `[1, "klein\\klein废土科幻.safetensors", 0.1, 1, 5287422717, "randomize"]`（1 次）
- `[1, "klein\\klein-衍月-4.safetensors", 0.1, 1, 5232721166, "randomize"]`（1 次）
- `[1, "qwen-大长腿_resized_from_64_to_16_00001_.safetensors", 0.1, 0.8, 7493929531, "randomize"]`（1 次）
- `[1, "QWEN-国漫风格.safetensors", 1, 2, 4115955066, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
