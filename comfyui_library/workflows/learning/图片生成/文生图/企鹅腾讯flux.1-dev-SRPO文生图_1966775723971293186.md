---
key: 企鹅腾讯flux.1-dev-SRPO文生图_1966775723971293186.json
name: 企鹅腾讯flux.1-dev-SRPO文生图_1966775723971293186
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/企鹅腾讯flux.1-dev-SRPO文生图_1966775723971293186.json
hash: 51c26fc27c1f603e
coverage: 0.9375
learned_at: 2026-10-10 20:59:35
nodes: [KSamplerSelect, RandomNoise, UNETLoader, SaveImage, CLIPTextEncode, CR SDXL Aspect Ratio, EmptySD3LatentImage, VAEDecode, SamplerCustomAdvanced, BasicScheduler, BasicGuider, FluxGuidance, DualCLIPLoader, VAELoader, RH_Translator, ModelSamplingFlux]
patterns: []
missing: [CR SDXL Aspect Ratio]
discoveries: [次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明]
---

# 企鹅腾讯flux.1-dev-SRPO文生图_1966775723971293186.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/企鹅腾讯flux.1-dev-SRPO文生图_1966775723971293186.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `KSamplerSelect` ★核心
- `RandomNoise`
- `UNETLoader` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CR SDXL Aspect Ratio`
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `BasicGuider`
- `FluxGuidance`
- `DualCLIPLoader`
- `VAELoader`
- `RH_Translator`
- `ModelSamplingFlux`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`KSamplerSelect`、`RandomNoise`、`UNETLoader`、`SaveImage`、`CLIPTextEncode`、`EmptySD3LatentImage`、`VAEDecode`、`SamplerCustomAdvanced`、`BasicScheduler`、`BasicGuider`、`FluxGuidance`、`DualCLIPLoader`、`VAELoader`、`RH_Translator`、`ModelSamplingFlux`

**缺卡**（1）：`CR SDXL Aspect Ratio`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、DualCLIPLoader

## 学习发现

- 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明
