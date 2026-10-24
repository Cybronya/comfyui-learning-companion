---
key: 图片生成/图生图/FLUX2-klein-9b——object-remove移除万物+重绘_2013596554896089089.json
name: FLUX2-klein-9b——object-remove移除万物+重绘_2013596554896089089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX2-klein-9b——object-remove移除万物+重绘_2013596554896089089.json
hash: a67353b88d9b4e51
coverage: 0.92
learned_at: 2026-10-23 10:54:34
nodes: [KSamplerSelect, Flux2Scheduler, BasicGuider, SamplerCustomAdvanced, VAEDecode, ReferenceLatent, FluxGuidance, PreviewImage, Mask Fill Holes, BlockifyMask, 取色器_孤海, ImpactImageInfo, LoadImage, LayerMask: MaskPreview, Note, CLIPLoader, RandomNoise, SaveImage, UNETLoader, LoraLoader, LayerUtility: ColorImage V2, LayerUtility: ImageBlendAdvance, VAEEncode, VAELoader, CLIPTextEncode]
patterns: [lora]
missing: []
parameters: {"lora_name": "flux-background-remove-lora.safetensors", "strength_clip": 1.1, "strength_model": 1.1}
---

# 图片生成/图生图/FLUX2-klein-9b——object-remove移除万物+重绘_2013596554896089089.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX2-klein-9b——object-remove移除万物+重绘_2013596554896089089.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `PreviewImage`
- `Mask Fill Holes`
- `BlockifyMask`
- `取色器_孤海`
- `ImpactImageInfo`
- `LoadImage`
- `LayerMask: MaskPreview`
- `Note`
- `CLIPLoader`
- `RandomNoise`
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlendAdvance`
- `VAEEncode` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心

**识别到的模式**：lora

## 关键参数

- `lora_name` = `flux-background-remove-lora.safetensors`
- `strength_model` = `1.1`
- `strength_clip` = `1.1`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`KSamplerSelect`、`Flux2Scheduler`、`BasicGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`ReferenceLatent`、`FluxGuidance`、`Mask Fill Holes`、`BlockifyMask`、`取色器_孤海`、`ImpactImageInfo`、`LoadImage`、`LayerMask: MaskPreview`、`CLIPLoader`、`RandomNoise`、`SaveImage`、`UNETLoader`、`LoraLoader`、`LayerUtility: ColorImage V2`、`LayerUtility: ImageBlendAdvance`、`VAEEncode`、`VAELoader`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
