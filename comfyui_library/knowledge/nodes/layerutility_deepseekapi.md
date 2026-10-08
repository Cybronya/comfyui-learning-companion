# LayerUtility: DeepSeekAPI

## 节点类型

`LayerUtility: DeepSeekAPI`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `history:DEEPSEEK_HISTORY`（2 次）
- `model:COMBO`（2 次）
- `max_tokens:INT`（2 次）
- `temperature:FLOAT`（2 次）
- `top_p:FLOAT`（2 次）
- `presence_penalty:FLOAT`（2 次）
- `frequency_penalty:FLOAT`（2 次）
- `history_length:INT`（2 次）
- `system_prompt:STRING`（2 次）
- `user_prompt:STRING`（2 次）

## 输出

- `text:STRING`（2 次）
- `history:DEEPSEEK_HISTORY`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["deepseek-chat", 4096, 1, 1, 0, 0, 8, "You are a helpful assistant.", "", "sk-47518ef4d0a9408086dccdfb02228453"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
