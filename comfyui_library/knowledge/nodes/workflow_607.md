# workflow>情感控制

## 节点类型

`workflow>情感控制`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `高兴:FLOAT`（1 次）
- `惊喜:FLOAT`（1 次）
- `低落:FLOAT`（1 次）
- `厌烦:FLOAT`（1 次）
- `悲伤:FLOAT`（1 次）
- `恐惧:FLOAT`（1 次）
- `愤怒:FLOAT`（1 次）
- `情感权重:FLOAT`（1 次）
- `语气补充:STRING`（1 次）

## 输出

- `int:FLOAT`（1 次）
- `惊喜 int:FLOAT`（1 次）
- `低落 int:FLOAT`（1 次）
- `厌烦 int:FLOAT`（1 次）
- `悲伤 int:FLOAT`（1 次）
- `恐惧 int:FLOAT`（1 次）
- `愤怒 int:FLOAT`（1 次）
- `情感权重 int:FLOAT`（1 次）
- `文本:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0, 0, 0, 0, 0, 0, 1, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
