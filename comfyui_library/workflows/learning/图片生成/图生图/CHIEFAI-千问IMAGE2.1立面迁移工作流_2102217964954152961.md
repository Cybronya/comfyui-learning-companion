---
key: 图片生成/图生图/CHIEFAI-千问IMAGE2.1立面迁移工作流_2102217964954152961.json
name: CHIEFAI-千问IMAGE2.1立面迁移工作流_2102217964954152961.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/CHIEFAI-千问IMAGE2.1立面迁移工作流_2102217964954152961.json
hash: ad6640acbba68f89
coverage: 0.909091
learned_at: 2026-10-09 22:19:27
nodes: [VAELoader, AIO_Preprocessor, LoadImage, LoadImage, CLIPLoader, UNETLoader, VAEDecode, SaveImage, TextEncodeQwenImage21, PrimitiveStringMultiline, KSampler]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1069087666117095, "steps": 25}
---

# 图片生成/图生图/CHIEFAI-千问IMAGE2.1立面迁移工作流_2102217964954152961.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102217964954152961.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（11 个）：
- `VAELoader`
- `AIO_Preprocessor`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `TextEncodeQwenImage21`
- `PrimitiveStringMultiline`
- `KSampler` ★核心

## 关键参数

- `seed` = `1069087666117095`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`VAELoader`、`AIO_Preprocessor`、`LoadImage`、`CLIPLoader`、`UNETLoader`、`VAEDecode`、`SaveImage`、`TextEncodeQwenImage21`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、SaveImage
