# YUAN_TXTJsonSwitch

## 节点类型

`YUAN_TXTJsonSwitch`

## 分类

Control Flow

## 作用

分支类节点：按条件选择输入（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `角色开关:BOOLEAN`（2 次）
- `音色开关:BOOLEAN`（2 次）
- `道具开关:BOOLEAN`（2 次）
- `场景开关:BOOLEAN`（2 次）
- `BGM开关:BOOLEAN`（2 次）
- `情节开关:BOOLEAN`（2 次）
- `台词开关:BOOLEAN`（2 次）
- `情节衔接开关:BOOLEAN`（2 次）

## 输出

- `开关配置:*`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, false, true, true, false, false, true, true]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
