# StringFormat

## 节点类型

`StringFormat`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `values.a:*`（5 次）
- `values.b:*`（5 次）
- `values.c:*`（5 次）
- `values.d:*`（5 次）
- `f_string:STRING`（5 次）

## 输出

- `STRING:STRING`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Dress {a} in image 1 in {b}. Keep their face, hair, hands, pose and the background exactly the same. {c}"]`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
