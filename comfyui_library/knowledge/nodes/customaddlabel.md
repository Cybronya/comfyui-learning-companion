# CustomAddLabel

## 节点类型

`CustomAddLabel`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `caption:STRING`（1 次）
- `enable_resize:BOOLEAN`（1 次）
- `longer_size:INT`（1 次）
- `text_x:INT`（1 次）
- `text_y:INT`（1 次）
- `height:INT`（1 次）
- `font_size:INT`（1 次）
- `font:COMBO`（1 次）
- `text:STRING`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, 1024, 50, 50, 90, 40, "Alibaba-PuHuiTi-Heavy.ttf", "水印区，自己用剪映或PS裁剪掉", "light", "up"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
