---
key: 图片生成/文生图/Y-image_chroma1_radiance_text_to_image_1971904444222926850.json
name: Y-image_chroma1_radiance_text_to_image_1971904444222926850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Y-image_chroma1_radiance_text_to_image_1971904444222926850.json
hash: 0480f29fd8cd61a6
coverage: 0.8
learned_at: 2026-10-15 22:27:38
nodes: [CLIPLoader, T5TokenizerOptions, ModelSamplingAuraFlow, VAEDecode, Note, MarkdownNote, VAELoader, CLIPTextEncode, KSampler, Note, SDXL Resolutions (JPS), EmptyChromaRadianceLatentImage, UNETLoader, CLIPTextEncode, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 566931473184963, "steps": 30}
---

# 图片生成/文生图/Y-image_chroma1_radiance_text_to_image_1971904444222926850.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Y-image_chroma1_radiance_text_to_image_1971904444222926850.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `CLIPLoader`
- `T5TokenizerOptions`
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `Note`
- `MarkdownNote`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `Note`
- `SDXL Resolutions (JPS)`
- `EmptyChromaRadianceLatentImage`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `566931473184963`
- `steps` = `30`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`CLIPLoader`、`T5TokenizerOptions`、`ModelSamplingAuraFlow`、`VAEDecode`、`VAELoader`、`CLIPTextEncode`、`KSampler`、`SDXL Resolutions (JPS)`、`EmptyChromaRadianceLatentImage`、`UNETLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyChromaRadianceLatentImage、SDXL Resolutions (JPS)
