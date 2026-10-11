# T8_IndexTTS25_SamplingConfig

## 节点类型

`T8_IndexTTS25_SamplingConfig`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `do_sample:BOOLEAN`（1 次）
- `temperature:FLOAT`（1 次）
- `top_p:FLOAT`（1 次）
- `top_k:INT`（1 次）
- `num_beams:INT`（1 次）
- `repetition_penalty:FLOAT`（1 次）
- `length_penalty:FLOAT`（1 次）
- `max_mel_tokens:INT`（1 次）
- `diffusion_steps:INT`（1 次）
- `inference_cfg_rate:FLOAT`（1 次）

## 输出

- `采样设置:T8_INDEXTTS25_SAMPLING`（1 次）
- `采样信息:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, 0.8, 0.8, 30, 3, 10, 0, 1500, 25, 0.7, 1, "auto", 120, 200, "off", 100, 300, 600, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
