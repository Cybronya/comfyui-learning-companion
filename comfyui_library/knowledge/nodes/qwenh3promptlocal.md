# QwenH3PromptLocal

## 节点类型

`QwenH3PromptLocal`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `reference_images.reference_image_0:IMAGE`（6 次）
- `reference_images.reference_image_1:IMAGE`（6 次）
- `reference_images.reference_image_2:IMAGE`（6 次）
- `reference_videos.reference_video_0:IMAGE`（6 次）
- `prompt:STRING`（6 次）
- `skill:COMBO`（6 次）
- `duration:FLOAT`（6 次）
- `llm_model:COMBO`（6 次）
- `vision_model:COMBO`（6 次）
- `think_mode:BOOLEAN`（6 次）

## 输出

- `h3_prompt:STRING`（6 次）
- `selected_skill:STRING`（6 次）
- `detected_mode:STRING`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "auto", 12, "Qwen3.8-27B-Q4_K_M.gguf", "mmproj-F16.gguf", false, "xhigh", 1088240457981748, "randomize", 8192, 2, t`（3 次）
- `["第一人称一镜到底的镜头，图1的二次元卡通角色拿着图2的显卡从图3的店铺跑向主视角然后说：帅哥要显卡么？5090！只要5万！", "auto", 12, "Qwen3.8-27B-Q4_K_M.gguf", "mmproj-F16.ggu`（2 次）
- `["Describe the video or production task.", "auto", 10, "Qwen3.8-27B-Q4_K_M.gguf", "mmproj-F16.gguf", false, "medium", 52`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
