---
key: 图片生成/图生图/【遇见AI】FLUX2-klein-4b，spritesheet四视图，fal版lora_2014170035505340418.json
name: 【遇见AI】FLUX2-klein-4b，spritesheet四视图，fal版lora_2014170035505340418
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】FLUX2-klein-4b，spritesheet四视图，fal版lora_2014170035505340418.json
hash: 0c78586dc4cc6d05
coverage: 1
learned_at: 2026-10-23 11:51:53
nodes: [RandomNoise, BasicGuider, KSamplerSelect, SamplerCustomAdvanced, Flux2Scheduler, FluxGuidance, VAEDecode, VAEEncode, ImpactImageInfo, ReferenceLatent, CLIPTextEncode, SaveImage, UNETLoader, CLIPLoader, VAELoader, LoraLoader, LoadImage]
patterns: [lora]
missing: []
parameters: {"lora_name": "flux-spritesheet-lora-fal.safetensors", "strength_clip": 1.1, "strength_model": 1.1}
---

# 图片生成/图生图/【遇见AI】FLUX2-klein-4b，spritesheet四视图，fal版lora_2014170035505340418.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】FLUX2-klein-4b，spritesheet四视图，fal版lora_2014170035505340418.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `Flux2Scheduler`
- `FluxGuidance`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `ImpactImageInfo`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoader` ★核心
- `LoadImage`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `flux-spritesheet-lora-fal.safetensors`
- `strength_model` = `1.1`
- `strength_clip` = `1.1`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`Flux2Scheduler`、`FluxGuidance`、`VAEDecode`、`VAEEncode`、`ImpactImageInfo`、`ReferenceLatent`、`CLIPTextEncode`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
