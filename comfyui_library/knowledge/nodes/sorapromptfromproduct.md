# SoraPromptFromProduct

## 节点类型

`SoraPromptFromProduct`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `product_name:STRING`（3 次）
- `product_features:STRING`（3 次）
- `video_type:COMBO`（3 次）
- `duration:COMBO`（3 次）
- `language:COMBO`（3 次）
- `reference_image_url:STRING`（3 次）
- `reference_image_description:STRING`（3 次）
- `system_prompt:STRING`（3 次）
- `user_prompt_template:STRING`（3 次）
- `api_base:STRING`（3 次）

## 输出

- `Sora提示词:STRING`（3 次）
- `视频时长:STRING`（3 次）
- `参考图URL:STRING`（3 次）
- `AI原始响应:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", "商品介绍", "15秒", "简体中文", "", "", "# 身份认定\n你是一位专业的电商视频导演助手，专精于为Sora 2视频生成模型创作分镜脚本。你的核心能力是将产品卖点转化为具有视觉冲击力的电商广告片，兼具高`（1 次）
- `["电动热吹风机", "强劲动力\n负离子干发\n长发护理首选", "商品介绍", "15秒", "简体中文", "", "", "# 身份认定\n你是一位专业的电商视频导演助手，专精于为Sora 2视频生成模型创作分镜脚本。你的核心能力是`（1 次）
- `["电动热吹风机", "强劲动力\n负离子干发\n长发护理首选", "商品介绍", "15秒", "简体中文", "", "", "# 身份认定\n你是一位专业的电商视频导演助手，专精于为Sora 2视频生成模型创作分镜脚本。你的核心能力是`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
