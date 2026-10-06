# RHLLMChatNode

## 节点类型

`RHLLMChatNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `image1:IMAGE`（5 次）
- `image2:IMAGE`（5 次）
- `image3:IMAGE`（5 次）
- `image4:IMAGE`（5 次）
- `image5:IMAGE`（5 次）
- `image6:IMAGE`（5 次）
- `image7:IMAGE`（5 次）
- `image8:IMAGE`（5 次）
- `video:VIDEO`（5 次）
- `api_config:RH_OPENAPI_CONFIG`（5 次）

## 输出

- `response:STRING`（5 次）
- `raw_response:STRING`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["openai/gpt-6-luna", "# 角色设定\n你是一位资深影视分镜预处理专家，精通小说改编、剧本可视化。你的任务是将任意小说文本转化为可用于AI视频生成的分镜预处理JSON。你的核心原则：**所有描述必须\"视觉可渲染、听觉`（2 次）
- `["deepseek/deepseek-v4.1-flash", "You are a helpful assistant", "把图2里的人物替换成图1", 0.6, 4096, 1, 0, 0, "none", 2078936937, `（1 次）
- `["deepseek/deepseek-v4.1-flash", "You are a helpful assistant", "把图2里的人物替换成图1", 0.6, 4096, 1, 0, 0, "none", 1588791961, `（1 次）
- `["google/gemini-3.5-flash", "You are a helpful assistant", "欧美经典男装的模特角色16:9设定图，要求面部细节丰富,白色背景，简单衣服，不展示衣服细节。", 0.6, 4096, `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
