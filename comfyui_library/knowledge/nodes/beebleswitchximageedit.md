# BeebleSwitchXImageEdit

## 节点类型

`BeebleSwitchXImageEdit`

## 分类

Control Flow

## 作用

分支类节点：按条件选择输入（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `reference_image:IMAGE`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `alpha:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Characters listening to music in the scene, product photography", "auto", "720p", 1784980040, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
