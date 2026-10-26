# workflow>反推节点

## 节点类型

`workflow>反推节点`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `source_path:PATH`（1 次）
- `image:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `seed:INT`（1 次）
- `attention:COMBO`（1 次）
- `text:STRING`（1 次）
- `model:COMBO`（1 次）
- `quantization:COMBO`（1 次）
- `keep_model_loaded:BOOLEAN`（1 次）
- `temperature:FLOAT`（1 次）

## 输出

- `show_help:STRING`（1 次）
- `STRING:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["将图片保持产品原有角度一模一样，背景是", 1990, "fixed", "flash_attention_2", "你是一位专业的AI图像生成提示词工程师。请详细描述这张图像主体、前景、中景、背景、构图、视觉引导、色调、光影氛围等细节`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
