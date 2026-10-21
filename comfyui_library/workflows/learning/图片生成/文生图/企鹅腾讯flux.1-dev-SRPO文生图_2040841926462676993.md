---
key: 图片生成/文生图/企鹅腾讯flux.1-dev-SRPO文生图_2040841926462676993.json
name: 企鹅腾讯flux.1-dev-SRPO文生图_2040841926462676993
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/企鹅腾讯flux.1-dev-SRPO文生图_2040841926462676993.json
hash: 4c86501d59f3f023
coverage: 1
learned_at: 2026-10-21 02:58:44
nodes: [KSamplerSelect, RandomNoise, UNETLoader, SaveImage, CLIPTextEncode, CR SDXL Aspect Ratio, EmptySD3LatentImage, VAEDecode, SamplerCustomAdvanced, BasicScheduler, BasicGuider, FluxGuidance, DualCLIPLoader, VAELoader, ModelSamplingFlux, TextInputNode, RH_Translator]
patterns: []
missing: []
---

# 图片生成/文生图/企鹅腾讯flux.1-dev-SRPO文生图_2040841926462676993.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/企鹅腾讯flux.1-dev-SRPO文生图_2040841926462676993.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
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
- `ModelSamplingFlux`
- `TextInputNode`
- `RH_Translator`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`KSamplerSelect`、`RandomNoise`、`UNETLoader`、`SaveImage`、`CLIPTextEncode`、`CR SDXL Aspect Ratio`、`EmptySD3LatentImage`、`VAEDecode`、`SamplerCustomAdvanced`、`BasicScheduler`、`BasicGuider`、`FluxGuidance`、`DualCLIPLoader`、`VAELoader`、`ModelSamplingFlux`、`TextInputNode`、`RH_Translator`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、DualCLIPLoader
