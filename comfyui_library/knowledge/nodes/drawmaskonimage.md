# DrawMaskOnImage

## 节点类型

`DrawMaskOnImage`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `image:IMAGE`（9 次）
- `mask:MASK`（9 次）
- `color:STRING`（9 次）
- `device:COMBO`（9 次）

## 输出

- `images:IMAGE`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["0, 0, 0", "cpu"]`（3 次）
- `["0, 0, 255", "cpu"]`（2 次）
- `["128, 128, 128", "cpu"]`（2 次）
- `["255, 0, 0", "cpu"]`（1 次）
- `["255, 255, 255", "gpu"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
