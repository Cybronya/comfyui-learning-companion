---
key: 图片生成/图生图/【15 秒极速版】Flux-ICEdit-MoE Lora-人物一致性图像编辑-StarAI_1918335426757591041.json
name: 【15 秒极速版】Flux-ICEdit-MoE Lora-人物一致性图像编辑-StarAI_1918335426757591041
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【15 秒极速版】Flux-ICEdit-MoE Lora-人物一致性图像编辑-StarAI_1918335426757591041.json
hash: 0440281a15fc2391
coverage: 0.967742
learned_at: 2026-10-23 11:48:09
nodes: [easy cleanGpuUsed, Note, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, GetImageSizeAndCount, SolidMask, easy makeImageForICLora, MaskPreview+, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, Note Plus (mtb), DeepTranslatorTextNode, easy cleanGpuUsed, DualCLIPLoader, easy cleanGpuUsed, VAELoader, easy seed, InpaintModelConditioning, FluxGuidance, ConditioningZeroOut, CLIPTextEncode, LoadImage, NunchakuFluxDiTLoader, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, SaveImage, SaveImage, GetImageSizeAndCount, CR Upscale Image, ImageCrop]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 图片生成/图生图/【15 秒极速版】Flux-ICEdit-MoE Lora-人物一致性图像编辑-StarAI_1918335426757591041.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【15 秒极速版】Flux-ICEdit-MoE Lora-人物一致性图像编辑-StarAI_1918335426757591041.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `easy cleanGpuUsed`
- `Note`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSizeAndCount`
- `SolidMask`
- `easy makeImageForICLora`
- `MaskPreview+`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `Note Plus (mtb)`
- `DeepTranslatorTextNode`
- `easy cleanGpuUsed`
- `DualCLIPLoader`
- `easy cleanGpuUsed`
- `VAELoader`
- `easy seed`
- `InpaintModelConditioning`
- `FluxGuidance`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `SaveImage`
- `GetImageSizeAndCount`
- `CR Upscale Image`
- `ImageCrop`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **97%**（30/31）

**有卡**：`easy cleanGpuUsed`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSizeAndCount`、`SolidMask`、`easy makeImageForICLora`、`MaskPreview+`、`LayerUtility: PurgeVRAM`、`Note Plus (mtb)`、`DeepTranslatorTextNode`、`DualCLIPLoader`、`VAELoader`、`easy seed`、`InpaintModelConditioning`、`FluxGuidance`、`ConditioningZeroOut`、`CLIPTextEncode`、`LoadImage`、`NunchakuFluxDiTLoader`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`SaveImage`、`CR Upscale Image`、`ImageCrop`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、KSamplerAdvanced
