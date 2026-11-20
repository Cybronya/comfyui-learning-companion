# workflow>四分镜拆分

## 节点类型

`workflow>四分镜拆分`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `input_text:STRING`（1 次）
- `delimiter:STRING`（1 次）
- `index:INT`（1 次）
- `ExtractLinesByIndex input_text:STRING`（1 次）
- `ExtractLinesByIndex delimiter:STRING`（1 次）
- `ExtractLinesByIndex index:INT`（1 次）
- `ExtractLinesByIndex 2 input_text:STRING`（1 次）
- `ExtractLinesByIndex 2 delimiter:STRING`（1 次）
- `ExtractLinesByIndex 2 index:INT`（1 次）
- `ExtractLinesByIndex 3 input_text:STRING`（1 次）

## 输出

- `ExtractLinesByIndex 1 STRING:STRING`（5 次）
- `ExtractLinesByIndex 2 STRING:STRING`（5 次）
- `ExtractLinesByIndex 3 STRING:STRING`（5 次）
- `ExtractLinesByIndex 0 STRING:STRING`（3 次）
- `STRING:STRING`（1 次）
- `ExtractLinesByIndex STRING:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "~", 1, "", "~", 2, "", "~", 3, "", "~", 4]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
