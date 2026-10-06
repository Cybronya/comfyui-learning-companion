# H3FrozenVideoCache

## 节点类型

`H3FrozenVideoCache`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `model:MODEL`（5 次）
- `enabled:BOOLEAN`（5 次）
- `cache_contents:COMBO`（5 次）
- `backend:COMBO`（5 次）
- `precision:COMBO`（5 次）
- `refresh_interval:INT`（5 次）
- `verbose:BOOLEAN`（5 次）
- `allow_disk:BOOLEAN`（5 次）
- `vram_margin_gb:FLOAT`（5 次）

## 输出

- `MODEL:MODEL`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, "hidden", "auto", "int4", 0, false, false, 1]`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
