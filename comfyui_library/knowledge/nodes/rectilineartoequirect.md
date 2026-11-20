# RectilinearToEquirect

## 节点类型

`RectilinearToEquirect`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `hfov_deg:FLOAT`（1 次）
- `equirect_width:INT`（1 次）
- `equirect_height:INT`（1 次）
- `yaw_deg:FLOAT`（1 次）
- `pitch_deg:FLOAT`（1 次）
- `shape:COMBO`（1 次）
- `fill_value:FLOAT`（1 次）
- `feather_px:INT`（1 次）
- `strip_letterbox:BOOLEAN`（1 次）

## 输出

- `equirect_image:IMAGE`（1 次）
- `outpaint_mask:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[90, 1920, 960, 180, 0, "pincushion", 0, 0, true, 0.06, false, "center"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
