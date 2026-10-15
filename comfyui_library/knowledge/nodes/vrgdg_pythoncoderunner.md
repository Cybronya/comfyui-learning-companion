# VRGDG_PythonCodeRunner

## 节点类型

`VRGDG_PythonCodeRunner`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `input_text:STRING`（3 次）
- `input_json:STRING`（3 次）
- `python_code:STRING`（3 次）

## 输出

- `result_text:STRING`（3 次）
- `result_json:STRING`（3 次）
- `has_error:BOOLEAN`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["# 仅去除文本中的空行，不修改其他内容，不限制行数\nimport re\n\n# 初始化变量\nresult = \"\"\nresult_text = \"\"\nhas_error = False\n\ntry:\n    if `（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
