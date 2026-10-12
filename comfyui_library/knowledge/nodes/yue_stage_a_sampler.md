# YUE_Stage_A_Sampler

## 节点类型

`YUE_Stage_A_Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL_YUE_A`（1 次）
- `run_n_segment:INT`（1 次）
- `prompt_end_time:FLOAT`（1 次）
- `genres_prompt:STRING`（1 次）
- `lyrics_prompt:STRING`（1 次）

## 输出

- `stage1_set:STAGE_SET`（1 次）
- `info:quantization_model`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["female Cantonese Melancholic Classical airy vocal Piano bright vocal Pop Nostalgic Violin", "", 1501924109, "randomize`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
