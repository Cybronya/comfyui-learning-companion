---
key: 平台全量/【遇见AI】FLUX2-klein-4b，object-remove移除万物，重绘，fal版lora_2013541060743532546.json
name: 【遇见AI】FLUX2-klein-4b，object-remove移除万物，重绘，fal版lora_2013541060743532546
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【遇见AI】FLUX2-klein-4b，object-remove移除万物，重绘，fal版lora_2013541060743532546.json
hash: dab05e07dde6ebc4
coverage: 0.884615
learned_at: 2026-11-14 01:25:33
nodes: [RandomNoise, BasicGuider, KSamplerSelect, SamplerCustomAdvanced, Flux2Scheduler, FluxGuidance, VAEDecode, ReferenceLatent, VAEEncode, BlockifyMask, Mask Fill Holes, LayerMask: MaskPreview, ImpactImageInfo, LayerUtility: ColorImage V2, LayerUtility: ImageBlendAdvance, PreviewImage, UNETLoader, CLIPLoader, VAELoader, LoadImage, 取色器_孤海, CLIPTextEncode, Note, LoraLoader, Image Comparer (rgthree), SaveImage]
patterns: [lora]
missing: []
parameters: {"lora_name": "flux-object-remove-lora-fal.safetensors", "strength_clip": 1.1, "strength_model": 1.1}
---

# 平台全量/【遇见AI】FLUX2-klein-4b，object-remove移除万物，重绘，fal版lora_2013541060743532546.json

> 来源文件 `comfyui_library/workflows/平台全量/【遇见AI】FLUX2-klein-4b，object-remove移除万物，重绘，fal版lora_2013541060743532546.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `Flux2Scheduler`
- `FluxGuidance`
- `VAEDecode` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `BlockifyMask`
- `Mask Fill Holes`
- `LayerMask: MaskPreview`
- `ImpactImageInfo`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlendAdvance`
- `PreviewImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `取色器_孤海`
- `CLIPTextEncode` ★核心
- `Note`
- `LoraLoader` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `flux-object-remove-lora-fal.safetensors`
- `strength_model` = `1.1`
- `strength_clip` = `1.1`

## 知识

覆盖率 **88%**（23/26）

**有卡**：`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`Flux2Scheduler`、`FluxGuidance`、`VAEDecode`、`ReferenceLatent`、`VAEEncode`、`BlockifyMask`、`Mask Fill Holes`、`LayerMask: MaskPreview`、`ImpactImageInfo`、`LayerUtility: ColorImage V2`、`LayerUtility: ImageBlendAdvance`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`取色器_孤海`、`CLIPTextEncode`、`LoraLoader`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect
