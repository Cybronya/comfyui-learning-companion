# RH_LLMAPI_Pro_Node

## 节点类型

`RH_LLMAPI_Pro_Node`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `image1:IMAGE`（11 次）
- `image2:IMAGE`（11 次）
- `image3:IMAGE`（11 次）
- `image4:IMAGE`（11 次）
- `video:VIDEO`（11 次）
- `image5:IMAGE`（11 次）
- `image6:IMAGE`（11 次）
- `image7:IMAGE`（11 次）
- `image8:IMAGE`（11 次）
- `api_config:RH_OPENAPI_CONFIG`（11 次）

## 输出

- `response:STRING`（11 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["deepseek/deepseek-v4.1-flash", "", "你是一位享誉全球的顶级电商创意总监，拥有为奢侈品、高科技、快消品、服饰等全品类产品策划详情页的深厚背景。你擅长拆解品牌调性，并将其转化为极其精准的 AI 图像描述词`（3 次）
- `["deepseek/deepseek-v4.1-flash", "", "", 0.6000000000000001, 549146746, "randomize", 4096, 1, 0, 0, "none", false]`（3 次）
- `["gemini-3-flash-preview", "你是专业的AI图像生成提示词工程师，需严格遵循以下要求，基于输入图像创作精准、可落地的中文图像生成提示词：\n\n一、核心目标\n完整还原输入图像的视觉细节，并确保提示词符合AI图像生`（2 次）
- `["gemini-3.1-pro-preview", "You are a helpful assistant", "Hello", 0.6, 1740896909, "randomize", 4096, 1, 0, 0, "none", `（1 次）
- `["gemini-3-pro-preview", "拉片解析输入视频，全程中文输出。忽略画面字幕、水印、文字标识，只解析视觉画面。\n自动识别镜头切换、人物动作变化、场景变化，**自动拆分多个分镜，严禁只输出单个分镜**。\n当镜头、场景、`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
