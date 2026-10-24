# LayerMask: SegformerFashionSetting

## 节点类型

`LayerMask: SegformerFashionSetting`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `shirt:BOOLEAN`（1 次）
- `top:BOOLEAN`（1 次）
- `sweater:BOOLEAN`（1 次）
- `cardigan:BOOLEAN`（1 次）
- `jacket:BOOLEAN`（1 次）
- `vest:BOOLEAN`（1 次）
- `pants:BOOLEAN`（1 次）
- `shorts:BOOLEAN`（1 次）
- `skirt:BOOLEAN`（1 次）
- `coat:BOOLEAN`（1 次）

## 输出

- `segformer_fashion_setting:LS_SEGFORMER_SETTING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, true, false, false, false, true, true, true, true, true, true, false, false, false, false, true, true, false, fal`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
