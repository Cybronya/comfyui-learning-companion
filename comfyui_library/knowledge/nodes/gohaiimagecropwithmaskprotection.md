# GohaiImageCropWithMaskProtection

## 节点类型

`GohaiImageCropWithMaskProtection`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `图像:IMAGE`（8 次）
- `保护遮罩:MASK`（8 次）
- `宽度:INT`（8 次）
- `高度:INT`（8 次）
- `保护扩展系数:FLOAT`（8 次）
- `填充模式:COMBO`（8 次）
- `整除数:INT`（8 次）

## 输出

- `图像:IMAGE`（8 次）
- `扩展遮罩:MASK`（8 次）
- `是否扩展:BOOLEAN`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1024, 1024, 1.1, "灰色", 0]`（4 次）
- `[1024, 1024, 1, "灰色", 0]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
