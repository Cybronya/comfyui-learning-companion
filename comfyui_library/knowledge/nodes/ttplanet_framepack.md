# TTPlanet_FramePack

## 节点类型

`TTPlanet_FramePack`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `ref_image:IMAGE`（2 次）
- `end_image:IMAGE`（2 次）
- `prompt:STRING`（2 次）
- `total_second_length:INT`（2 次）

## 输出

- `frames:IMAGE`（2 次）
- `fps:FLOAT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["A girl slowly turns around and sits down", 8, 865843158393921, "randomize", 25, true, "480p", "optimized", 1, true, 1,`（1 次）
- `["A girl slowly turns around and sits down", 8, 490614290613443, "randomize", 25, true, "480p", "optimized", 0.800000000`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
