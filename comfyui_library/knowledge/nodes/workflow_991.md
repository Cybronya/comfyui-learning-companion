# workflow>裁剪遮罩

## 节点类型

`workflow>裁剪遮罩`

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
- `颜色:STRING`（1 次）

## 输出

- `裁剪图像:IMAGE`（1 次）
- `裁剪框:BOX`（1 次）
- `裁剪框预览:IMAGE`（1 次）
- `图像:IMAGE`（1 次）
- `LayerUtility: ImageBlend 图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, "mask_area", 32, 32, 32, 32, "None", "custom", 512, 512, true, "normal", 100, "#FFFFFF"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
