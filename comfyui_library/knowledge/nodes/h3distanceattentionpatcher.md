# H3DistanceAttentionPatcher

## 节点类型

`H3DistanceAttentionPatcher`

## 分类

Optimization

## 作用

注意力/加速优化节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（4 次）
- `receptive_field_scale:FLOAT`（4 次）
- `temporal_weight:FLOAT`（4 次）
- `start_at_sigma:FLOAT`（4 次）
- `end_at_sigma:FLOAT`（4 次）
- `num_frames:INT`（4 次）
- `original_width:INT`（4 次）
- `original_height:INT`（4 次）

## 输出

- `model:MODEL`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 3, 2.5, 0, 17, 864, 480]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
