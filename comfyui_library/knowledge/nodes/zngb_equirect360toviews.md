# ZNGB_Equirect360ToViews

## 节点类型

`ZNGB_Equirect360ToViews`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `num_views:INT`（3 次）
- `fov:FLOAT`（3 次）
- `pitch:FLOAT`（3 次）
- `yaw_offset:FLOAT`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）
- `device:COMBO`（3 次）

## 输出

- `views:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[6, 120, 90, 0, 2048, 1024, "gpu"]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
