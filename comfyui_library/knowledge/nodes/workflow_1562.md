# workflow>创意图片处理

## 节点类型

`workflow>创意图片处理`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `裁剪框:BOX`（1 次）
- `参考图像:IMAGE`（1 次）
- `ImageResize+ image:IMAGE`（1 次）
- `背景图像:IMAGE`（1 次）
- `invert_mask:BOOLEAN`（1 次）
- `detect:COMBO`（1 次）
- `top_reserve:INT`（1 次）
- `bottom_reserve:INT`（1 次）

## 输出

- `裁剪框预览:IMAGE`（1 次）
- `X:INT`（1 次）
- `Y:INT`（1 次）
- `image_urls:STRING`（1 次）
- `宽度:INT`（1 次）
- `高度:INT`（1 次）
- `IMAGE:IMAGE`（1 次）
- `图像:IMAGE`（1 次）
- `遮罩:MASK`（1 次）
- `ImageResize+ 宽度:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, "mask_area", 200, 200, 200, 200, "8", 60, "auto", 40, false, 1152, 1152, "lanczos", "keep proportion", "always",`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
