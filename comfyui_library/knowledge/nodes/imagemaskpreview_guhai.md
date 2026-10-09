# ImageMaskPreview_Guhai

## 节点类型

`ImageMaskPreview_Guhai`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `图像:IMAGE`（3 次）
- `遮罩:MASK`（3 次）
- `遮罩不透明:FLOAT`（3 次）
- `遮罩颜色:COLORCODE`（3 次）
- `显示序号:BOOLEAN`（3 次）
- `序号不透明:FLOAT`（3 次）
- `序号缩放:COMBO`（3 次）
- `字号比例:FLOAT`（3 次）
- `序号字体:COMBO`（3 次）
- `序号颜色:COLORCODE`（3 次）

## 输出

- `IMAGE:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.9, "#ff0000", false, 0.8, "跟随遮罩缩放", 0.6, "苹方特粗.ttf", "#ffffff"]`（1 次）
- `[0.4, "#00ffff", false, 0.8, "跟随遮罩缩放", 0.5, "苹方特粗.ttf", "#ffffff"]`（1 次）
- `[0.4, "#ff00a2", true, 0.8, "跟随遮罩缩放", 0.5, "苹方特粗.ttf", "#ffffff"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
