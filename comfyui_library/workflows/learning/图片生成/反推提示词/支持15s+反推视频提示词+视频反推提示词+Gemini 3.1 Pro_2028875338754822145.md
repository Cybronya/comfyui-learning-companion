---
key: 图片生成/反推提示词/支持15s+反推视频提示词+视频反推提示词+Gemini 3.1 Pro_2028875338754822145.json
name: 支持15s+反推视频提示词+视频反推提示词+Gemini 3.1 Pro_2028875338754822145
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/支持15s+反推视频提示词+视频反推提示词+Gemini 3.1 Pro_2028875338754822145.json
hash: 08f8d0c195aeeb95
coverage: 0.666667
learned_at: 2026-10-26 01:48:15
nodes: [ShowText|pysssss, easy saveText, ShowText|pysssss, RH_LLMAPI_Pro_Node, easy positive, LoadVideo]
patterns: []
missing: []
---

# 图片生成/反推提示词/支持15s+反推视频提示词+视频反推提示词+Gemini 3.1 Pro_2028875338754822145.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/支持15s+反推视频提示词+视频反推提示词+Gemini 3.1 Pro_2028875338754822145.json`

## 结构

**生成流程**：Output → Other

**节点**（6 个）：
- `ShowText|pysssss`
- `easy saveText`
- `ShowText|pysssss`
- `RH_LLMAPI_Pro_Node`
- `easy positive`
- `LoadVideo`

## 知识

覆盖率 **67%**（4/6）

**有卡**：`easy saveText`、`RH_LLMAPI_Pro_Node`、`easy positive`、`LoadVideo`

**用到的条目**：easy saveText、LoadVideo、RH_LLMAPI_Pro_Node、easy positive、sd15-t2i-basic、sd15-t2i-lora、sd1_5_text2image_sampler_clip_checkpoint、sdxl_portrait_controlnet_lora_sampler
