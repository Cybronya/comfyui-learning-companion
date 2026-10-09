# RemoveBackgroundWithMask

## 节点类型

`RemoveBackgroundWithMask`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（2 次）
- `遮罩:MASK`（2 次）
- `遮罩填充漏洞:BOOLEAN`（2 次）
- `遮罩裁剪:BOOLEAN`（2 次）
- `裁剪系数:FLOAT`（2 次）
- `图像描边:INT`（2 次）
- `描边颜色:COLORCODE`（2 次）

## 输出

- `RGBA图像:IMAGE`（2 次）
- `RGB图像:IMAGE`（2 次）
- `遮罩:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, false, 1.2, 0, "#ffffff"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
