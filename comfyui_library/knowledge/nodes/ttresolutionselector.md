# TTResolutionSelector

## 节点类型

`TTResolutionSelector`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `use_custom_resolution:BOOLEAN`（16 次）
- `resolution:COMBO`（16 次）
- `custom_width:INT`（16 次）
- `custom_height:INT`（16 次）

## 输出

- `width:INT`（16 次）
- `height:INT`（16 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, "1080x1920 (9:16) (竖屏)", 1024, 1024]`（12 次）
- `[false, "1024x1024 (1:1) (方形)", 1024, 1024]`（3 次）
- `[false, "720x1280 (9:16) (竖屏)", 480, 320]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
