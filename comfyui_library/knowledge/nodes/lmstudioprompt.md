# LMStudioPrompt

## 节点类型

`LMStudioPrompt`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `input_prompt:STRING`（2 次）
- `mode:COMBO`（2 次）
- `custom_history:STRING`（2 次）
- `server_address:STRING`（2 次）
- `server_port:INT`（2 次）
- `seed:INT`（2 次）

## 输出

- `text:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Prompt Text Here", "prompt", "path to history.json", "localhost", 1234, 264526016872054, "randomize"]`（1 次）
- `["Prompt Text Here", "prompt", "path to history.json", "localhost", 1234, 168168597185255, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
