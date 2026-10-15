# AFL:ImageSwitch

## 节点类型

`AFL:ImageSwitch`

## 分类

Control Flow

## 作用

分支类节点：按条件选择输入（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image1:IMAGE`（2 次）
- `image2:IMAGE`（2 次）
- `manual_choice:COMBO`（2 次）

## 输出

- `image_auto:IMAGE`（2 次）
- `image_manual:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["image1"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
