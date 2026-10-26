---
key: 图片生成/反推提示词/图像反推提示词_qwen3.5_2063048577647202305.json
name: 图像反推提示词_qwen3.5_2063048577647202305
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/图像反推提示词_qwen3.5_2063048577647202305.json
hash: ea612bb81f09be6e
coverage: 0.8
learned_at: 2026-10-26 01:47:46
nodes: [CLIPLoader, PreviewAny, LoadImage, easy saveText, TextGenerate]
patterns: []
missing: []
---

# 图片生成/反推提示词/图像反推提示词_qwen3.5_2063048577647202305.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/图像反推提示词_qwen3.5_2063048577647202305.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（5 个）：
- `CLIPLoader`
- `PreviewAny`
- `LoadImage`
- `easy saveText`
- `TextGenerate`

## 知识

覆盖率 **80%**（4/5）

**有卡**：`CLIPLoader`、`LoadImage`、`easy saveText`、`TextGenerate`

**用到的条目**：CLIPLoader、LoadImage、easy saveText、TextGenerate、sd15-t2i-basic、sd15-t2i-lora、sd1_5_text2image_sampler_clip_checkpoint、sdxl_portrait_controlnet_lora_sampler
