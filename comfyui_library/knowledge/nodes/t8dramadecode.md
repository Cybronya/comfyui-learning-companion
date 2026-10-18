# T8DramaDecode

## 节点类型

`T8DramaDecode`

## 分类

Decoding

## 作用

解码类节点：把编码数据还原（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `engine:DRAMA3_T8_ENGINE`（1 次）
- `session:DRAMA3_T8_SESSION`（1 次）
- `take_index:INT`（1 次）
- `all_takes:BOOLEAN`（1 次）

## 输出

- `AUDIO:AUDIO`（1 次）
- `STRING:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[-1, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
