# workflow>遮罩裁剪

## 节点类型

`workflow>遮罩裁剪`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `遮罩1:MASK`（1 次）
- `遮罩2:MASK`（1 次）
- `背景图像:IMAGE`（1 次）
- `图像层:IMAGE`（1 次）
- `裁剪框:BOX`（1 次）
- `顶端保留:INT`（1 次）
- `底部保留:INT`（1 次）
- `左侧保留:INT`（1 次）
- `右侧保留:INT`（1 次）

## 输出

- `裁剪图像:IMAGE`（1 次）
- `裁剪遮罩:MASK`（1 次）
- `裁剪框:BOX`（1 次）
- `裁剪框预览:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, "normal", 100, false, "mask_area", "None", 32, 32, 203, 216]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
