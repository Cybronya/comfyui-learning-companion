---
key: 图片生成/图生图/【阡陌】 Comfyui Qwen-Image调用deepseek反推提示词生图 洗图_1960224788335767553.json
name: 【阡陌】 Comfyui Qwen-Image调用deepseek反推提示词生图 洗图_1960224788335767553
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【阡陌】 Comfyui Qwen-Image调用deepseek反推提示词生图 洗图_1960224788335767553.json
hash: dd9d04d61867515e
coverage: 0.6
learned_at: 2026-10-23 11:52:33
nodes: [SaveImage, ShowText|pysssss, LoadImage, JanusModelLoader, Note, Note, JanusImageUnderstanding, LoadImage, Note, QwenImageNode]
patterns: []
missing: []
---

# 图片生成/图生图/【阡陌】 Comfyui Qwen-Image调用deepseek反推提示词生图 洗图_1960224788335767553.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【阡陌】 Comfyui Qwen-Image调用deepseek反推提示词生图 洗图_1960224788335767553.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（10 个）：
- `SaveImage`
- `ShowText|pysssss`
- `LoadImage`
- `JanusModelLoader`
- `Note`
- `Note`
- `JanusImageUnderstanding`
- `LoadImage`
- `Note`
- `QwenImageNode`

## 知识

覆盖率 **60%**（6/10）

**有卡**：`SaveImage`、`LoadImage`、`JanusModelLoader`、`JanusImageUnderstanding`、`QwenImageNode`

**用到的条目**：LoadImage、SaveImage、JanusModelLoader、JanusImageUnderstanding、QwenImageNode、sd15-t2i-basic、sd15-t2i-lora、sd1_5_text2image_sampler_clip_checkpoint
