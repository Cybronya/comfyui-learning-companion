# LayerMask: SegformerClothesSetting

## 节点类型

`LayerMask: SegformerClothesSetting`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `face:BOOLEAN`（2 次）
- `hair:BOOLEAN`（2 次）
- `hat:BOOLEAN`（2 次）
- `sunglass:BOOLEAN`（2 次）
- `left_arm:BOOLEAN`（2 次）
- `right_arm:BOOLEAN`（2 次）
- `left_leg:BOOLEAN`（2 次）
- `right_leg:BOOLEAN`（2 次）
- `left_shoe:BOOLEAN`（2 次）
- `right_shoe:BOOLEAN`（2 次）

## 输出

- `segformer_clothes_setting:LS_SEGFORMER_SETTING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, true, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
