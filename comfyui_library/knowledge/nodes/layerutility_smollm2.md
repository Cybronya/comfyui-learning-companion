# LayerUtility: SmolLM2

## 节点类型

`LayerUtility: SmolLM2`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `smolLM2_model:SmolLM2_MODEL`（2 次）
- `user_prompt:STRING`（2 次）
- `max_new_tokens:INT`（1 次）
- `do_sample:BOOLEAN`（1 次）
- `temperature:FLOAT`（1 次）
- `top_p:FLOAT`（1 次）
- `system_prompt:STRING`（1 次）

## 输出

- `text:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1024, true, 0.6000000000000001, 0.9, "You are an AI drawing prompt word assistant, the user gives you the prompt word t`（1 次）
- `[4048, true, 0.5, 0.9, "填充主体的信息和 背景  固定词为no hands, no tools, no effects 例如：输入为 玉米、厨房台面 输出：Photo of a whole corn cob with`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
