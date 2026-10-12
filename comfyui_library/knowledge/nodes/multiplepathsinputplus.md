# MultiplePathsInputPlus

## 节点类型

`MultiplePathsInputPlus`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `path_1:PATH`（4 次）
- `inputcount:INT`（4 次）
- `sample_fps:INT`（4 次）
- `max_frames:INT`（4 次）
- `use_total_frames:BOOLEAN`（4 次）
- `use_original_fps_as_sample_fps:BOOLEAN`（4 次）
- `path_2:PATH`（1 次）

## 输出

- `paths:PATH`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 1, 2, true, true, 1, null]`（3 次）
- `[2, 1, 2, true, true, 1, null]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
