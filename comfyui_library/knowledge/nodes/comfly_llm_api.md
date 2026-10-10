# Comfly_LLm_API

## 节点类型

`Comfly_LLm_API`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `ref_image:IMAGE`（1 次）
- `video:VIDEO`（1 次）
- `api_baseurl:STRING`（1 次）
- `api_key:STRING`（1 次）
- `model:STRING`（1 次）
- `role:STRING`（1 次）
- `prompt:STRING`（1 次）
- `temperature:FLOAT`（1 次）
- `seed:INT`（1 次）

## 输出

- `describe:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["https://coding.dashscope.aliyuncs.com/v1", "", "qwen3.5-plus", "你是一个视频提示词写作专家，在视频中一个主体依次出现在三个相关的场景中，描写3个场景，每个场景描述在100字`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
