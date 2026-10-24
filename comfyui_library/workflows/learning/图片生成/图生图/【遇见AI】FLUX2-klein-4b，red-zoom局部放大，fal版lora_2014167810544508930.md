---
key: 图片生成/图生图/【遇见AI】FLUX2-klein-4b，red-zoom局部放大，fal版lora_2014167810544508930.json
name: 【遇见AI】FLUX2-klein-4b，red-zoom局部放大，fal版lora_2014167810544508930
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】FLUX2-klein-4b，red-zoom局部放大，fal版lora_2014167810544508930.json
hash: 5a0eec2063bdc0b0
coverage: 0.954545
learned_at: 2026-10-23 11:51:53
nodes: [RandomNoise, BasicGuider, KSamplerSelect, SamplerCustomAdvanced, Flux2Scheduler, FluxGuidance, VAEDecode, ReferenceLatent, VAEEncode, CLIPTextEncode, SaveImage, LayerUtility: ColorImage V2, LayerUtility: ImageBlendAdvance, LayerMask: MaskPreview, PreviewImage, ImpactImageInfo, 取色器_孤海, LoraLoader, UNETLoader, CLIPLoader, VAELoader, LoadImage]
patterns: [lora]
missing: []
parameters: {"lora_name": "flux-red-zoom-lora-fal.safetensors", "strength_clip": 1.1, "strength_model": 1.1}
---

# 图片生成/图生图/【遇见AI】FLUX2-klein-4b，red-zoom局部放大，fal版lora_2014167810544508930.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】FLUX2-klein-4b，red-zoom局部放大，fal版lora_2014167810544508930.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `Flux2Scheduler`
- `FluxGuidance`
- `VAEDecode` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlendAdvance`
- `LayerMask: MaskPreview`
- `PreviewImage`
- `ImpactImageInfo`
- `取色器_孤海`
- `LoraLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `flux-red-zoom-lora-fal.safetensors`
- `strength_model` = `1.1`
- `strength_clip` = `1.1`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`Flux2Scheduler`、`FluxGuidance`、`VAEDecode`、`ReferenceLatent`、`VAEEncode`、`CLIPTextEncode`、`SaveImage`、`LayerUtility: ColorImage V2`、`LayerUtility: ImageBlendAdvance`、`LayerMask: MaskPreview`、`ImpactImageInfo`、`取色器_孤海`、`LoraLoader`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
