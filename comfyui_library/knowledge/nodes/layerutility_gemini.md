# LayerUtility: Gemini

## 节点类型

`LayerUtility: Gemini`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image_1:IMAGE`（1 次）
- `image_2:IMAGE`（1 次）
- `model:COMBO`（1 次）
- `max_output_tokens:INT`（1 次）
- `temperature:FLOAT`（1 次）
- `words_limit:INT`（1 次）
- `response_language:COMBO`（1 次）
- `system_prompt:STRING`（1 次）
- `user_prompt:STRING`（1 次）

## 输出

- `text:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["gemini-1.5-pro", 4096, 0.5, 200, "zh-CN", "系统提示词 角色： 你是一名专业的图像内容分析大师和图像生成提示词工程师。  核心任务： 分析用户所提供的图像，并根据图像中人物的特征执行以下精确指令`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
