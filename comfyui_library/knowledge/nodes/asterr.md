# ASTERR

## 节点类型

`ASTERR`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `a:*`（17 次）
- `b:*`（17 次）
- `c:*`（17 次）
- `d:*`（17 次）
- `e:*`（17 次）
- `f:*`（17 次）
- `g:*`（17 次）
- `h:*`（17 次）
- `i:*`（17 次）
- `j:*`（17 次）

## 输出

- `result:*`（17 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["asterr_result = 0 if b is True else a + 2 * c", 0, "None", "false"]`（2 次）
- `["asterr_result = 0 if c is True else a + 2 * b", 0, "None", "false"]`（2 次）
- `["asterr_result = int(a / 2) - d", 0, "None", "false"]`（1 次）
- `["asterr_result = int(a / 2) - d if b is False else a", 0, "None", "false"]`（1 次）
- `["asterr_result = a * 2 if a != 0 else 1", 0, "None", "false"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
