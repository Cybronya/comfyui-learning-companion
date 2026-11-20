---
key: 平台全量/【遇见AI】FLUX2-klein-4b，background-remove去背景，fal版lora_2013531368650711041.json
name: 【遇见AI】FLUX2-klein-4b，background-remove去背景，fal版lora_2013531368650711041
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【遇见AI】FLUX2-klein-4b，background-remove去背景，fal版lora_2013531368650711041.json
hash: 2597343ba7210e11
coverage: 1
learned_at: 2026-11-14 01:25:33
nodes: [RandomNoise, BasicGuider, KSamplerSelect, SamplerCustomAdvanced, Flux2Scheduler, FluxGuidance, VAEDecode, VAEEncode, ImpactImageInfo, ReferenceLatent, SaveImage, UNETLoader, CLIPLoader, VAELoader, LoadImage, CLIPTextEncode, LoraLoader]
patterns: [lora]
missing: []
parameters: {"lora_name": "flux-background-remove-lora-fal.safetensors", "strength_clip": 1.1, "strength_model": 1.1}
---

# 平台全量/【遇见AI】FLUX2-klein-4b，background-remove去背景，fal版lora_2013531368650711041.json

> 来源文件 `comfyui_library/workflows/平台全量/【遇见AI】FLUX2-klein-4b，background-remove去背景，fal版lora_2013531368650711041.json`

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
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心

**识别到的模式**：lora

## 关键参数

- `lora_name` = `flux-background-remove-lora-fal.safetensors`
- `strength_model` = `1.1`
- `strength_clip` = `1.1`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`Flux2Scheduler`、`FluxGuidance`、`VAEDecode`、`VAEEncode`、`ImpactImageInfo`、`ReferenceLatent`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`CLIPTextEncode`、`LoraLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect
