---
key: 平台全量/【遇见AI】FLUX2-klein-4b，outpaint扩图，fal版lora_2013431600855388161.json
name: 【遇见AI】FLUX2-klein-4b，outpaint扩图，fal版lora_2013431600855388161
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【遇见AI】FLUX2-klein-4b，outpaint扩图，fal版lora_2013431600855388161.json
hash: 442835a382049e5e
coverage: 0.869565
learned_at: 2026-11-14 01:25:34
nodes: [RandomNoise, BasicGuider, KSamplerSelect, SamplerCustomAdvanced, Flux2Scheduler, FluxGuidance, CLIPTextEncode, ImagePadForOutpaint, PreviewImage, PreviewImage, VAEEncode, ImpactImageInfo, ReferenceLatent, CLIPLoader, VAELoader, LoraLoader, LoadImage, 取色器_孤海, UNETLoader, DrawMaskOnImage, VAEDecode, SaveImage, Image Comparer (rgthree)]
patterns: [lora]
missing: []
parameters: {"lora_name": "flux-outpaint-lora.safetensors", "strength_clip": 1.1, "strength_model": 1.1}
---

# 平台全量/【遇见AI】FLUX2-klein-4b，outpaint扩图，fal版lora_2013431600855388161.json

> 来源文件 `comfyui_library/workflows/平台全量/【遇见AI】FLUX2-klein-4b，outpaint扩图，fal版lora_2013431600855388161.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `Flux2Scheduler`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `ImagePadForOutpaint`
- `PreviewImage`
- `PreviewImage`
- `VAEEncode` ★核心
- `ImpactImageInfo`
- `ReferenceLatent`
- `CLIPLoader`
- `VAELoader`
- `LoraLoader` ★核心
- `LoadImage`
- `取色器_孤海`
- `UNETLoader` ★核心
- `DrawMaskOnImage`
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `flux-outpaint-lora.safetensors`
- `strength_model` = `1.1`
- `strength_clip` = `1.1`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`Flux2Scheduler`、`FluxGuidance`、`CLIPTextEncode`、`ImagePadForOutpaint`、`VAEEncode`、`ImpactImageInfo`、`ReferenceLatent`、`CLIPLoader`、`VAELoader`、`LoraLoader`、`LoadImage`、`取色器_孤海`、`UNETLoader`、`DrawMaskOnImage`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect
