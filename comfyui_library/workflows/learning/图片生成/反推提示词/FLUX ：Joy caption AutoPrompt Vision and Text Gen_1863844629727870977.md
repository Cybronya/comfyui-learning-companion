---
key: 图片生成/反推提示词/FLUX ：Joy caption AutoPrompt Vision and Text Gen_1863844629727870977.json
name: FLUX ：Joy caption AutoPrompt Vision and Text Gen_1863844629727870977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/FLUX ：Joy caption AutoPrompt Vision and Text Gen_1863844629727870977.json
hash: 97f8e2447da70c36
coverage: 1
learned_at: 2026-10-26 01:45:02
nodes: [RandomNoise, KSamplerSelect, BasicGuider, FluxGuidance, Joy_caption_load, Joy_caption, Text to Conditioning, EG_WB_KSH, SamplerCustomAdvanced, VAEDecode, SaveImage, EmptyLatentImage, BasicScheduler, CheckpointLoaderNF4, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "nf4Flux1_nf4Bnb.safetensors", "height": 1344, "width": 896}
---

# 图片生成/反推提示词/FLUX ：Joy caption AutoPrompt Vision and Text Gen_1863844629727870977.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/FLUX ：Joy caption AutoPrompt Vision and Text Gen_1863844629727870977.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `FluxGuidance`
- `Joy_caption_load`
- `Joy_caption`
- `Text to Conditioning`
- `EG_WB_KSH`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `BasicScheduler`
- `CheckpointLoaderNF4` ★核心
- `LoadImage`

## 关键参数

- `width` = `896`
- `height` = `1344`
- `batch_size` = `1`
- `checkpoint` = `nf4Flux1_nf4Bnb.safetensors`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`RandomNoise`、`KSamplerSelect`、`BasicGuider`、`FluxGuidance`、`Joy_caption_load`、`Joy_caption`、`Text to Conditioning`、`EG_WB_KSH`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`EmptyLatentImage`、`BasicScheduler`、`CheckpointLoaderNF4`、`LoadImage`

**用到的条目**：VAEDecode、EmptyLatentImage、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、CheckpointLoaderNF4、Text to Conditioning
