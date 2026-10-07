# Storydiffusion_Sampler

## 节点类型

`Storydiffusion_Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:STORY_DICT`（1 次）
- `control_image:IMAGE`（1 次）
- `scene_prompts:STRING`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `prompt_array:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "bad anatomy, bad hands, missing fingers, extra fingers, three hands, three legs, bad arms, missing legs, missing a`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
