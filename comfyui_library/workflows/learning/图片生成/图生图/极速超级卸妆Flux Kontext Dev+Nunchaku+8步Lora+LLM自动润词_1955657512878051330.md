---
key: 图片生成/图生图/极速超级卸妆Flux Kontext Dev+Nunchaku+8步Lora+LLM自动润词_1955657512878051330.json
name: 极速超级卸妆Flux Kontext Dev+Nunchaku+8步Lora+LLM自动润词_1955657512878051330
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/极速超级卸妆Flux Kontext Dev+Nunchaku+8步Lora+LLM自动润词_1955657512878051330.json
hash: eccb9e07dee567df
coverage: 1
learned_at: 2026-10-23 13:09:43
nodes: [VAEEncode, ReferenceLatent, FluxGuidance, CLIPTextEncode, KSampler, VAELoader, RH_LLMAPI_NODE, FluxKontextImageScale, ConditioningZeroOut, GetImageSize+, EmptySD3LatentImage, VAEDecode, DualCLIPLoader, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, LoadImage, Text Multiline, UpscaleModelLoader, ImageUpscaleWithModel, LayerUtility: PurgeVRAM V2, ImageScaleByAspectRatio_UTK, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 913885470740781, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/极速超级卸妆Flux Kontext Dev+Nunchaku+8步Lora+LLM自动润词_1955657512878051330.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/极速超级卸妆Flux Kontext Dev+Nunchaku+8步Lora+LLM自动润词_1955657512878051330.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `VAEEncode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `RH_LLMAPI_NODE`
- `FluxKontextImageScale`
- `ConditioningZeroOut`
- `GetImageSize+`
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `DualCLIPLoader`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `LoadImage`
- `Text Multiline`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `LayerUtility: PurgeVRAM V2`
- `ImageScaleByAspectRatio_UTK`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `913885470740781`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（24/24）

**有卡**：`VAEEncode`、`ReferenceLatent`、`FluxGuidance`、`CLIPTextEncode`、`KSampler`、`VAELoader`、`RH_LLMAPI_NODE`、`FluxKontextImageScale`、`ConditioningZeroOut`、`GetImageSize+`、`EmptySD3LatentImage`、`VAEDecode`、`DualCLIPLoader`、`NunchakuFluxDiTLoader`、`NunchakuFluxLoraLoader`、`LoadImage`、`Text Multiline`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`LayerUtility: PurgeVRAM V2`、`ImageScaleByAspectRatio_UTK`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、ReferenceLatent

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
