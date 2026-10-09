# QwenImage21PromptEnhancerT8

## 节点类型

`QwenImage21PromptEnhancerT8`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `reference_images.reference_image_0:IMAGE`（1 次）
- `reference_images.reference_image_1:IMAGE`（1 次）
- `reference_images.reference_image_2:IMAGE`（1 次）
- `reference_images.reference_image_3:IMAGE`（1 次）
- `reference_images.reference_image_4:IMAGE`（1 次）
- `reference_images.reference_image_5:IMAGE`（1 次）
- `api_key:STRING`（1 次）
- `provider_config:T8_LLM_PROVIDER_CONFIG`（1 次）
- `prompt:STRING`（1 次）
- `input_mode:COMBO`（1 次）

## 输出

- `rewritten_prompt:STRING`（1 次）
- `wh_ratio:STRING`（1 次）
- `qwen_image_request_json:STRING`（1 次）
- `enhancement_report_json:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["只修改红色区域，其他区域不动！！！！！！！\n图1的设计改为图2的设计，拉链头，并修复红色区域。\n图1的角度禁止改变！！！！！\n完成后删除和红色区域。\n要求1：1复刻同时不改变图1全部特征（模特、光影、背景、构图等均保持一致）",`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
