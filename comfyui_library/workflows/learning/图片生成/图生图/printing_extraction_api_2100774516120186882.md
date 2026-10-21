---
key: 图片生成/图生图/printing_extraction_api_2100774516120186882.json
name: printing_extraction_api_2100774516120186882
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/printing_extraction_api_2100774516120186882.json
hash: 0bb6f1751ed4d989
coverage: 1
learned_at: 2026-10-21 00:45:58
nodes: [CLIPLoader, VAELoader, ModelSamplingAuraFlow, CFGNorm, VAEDecode, FluxKontextMultiReferenceLatentMethod, QwenEditOutputExtractor_EditUtils, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, CropWithPadInfo_EditUtils, TextEncodeQwenImageEditPlusCustom_lrzjason, SaveImage, LoraLoaderModelOnly, KSampler, ImageScale, QwenEditConfigPreparer, LayerUtility: ImageScaleByAspectRatio V2, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 696200972737273, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/printing_extraction_api_2100774516120186882.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/printing_extraction_api_2100774516120186882.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `VAEDecode` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `QwenEditOutputExtractor_EditUtils`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CropWithPadInfo_EditUtils`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `ImageScale`
- `QwenEditConfigPreparer`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`

## 关键参数

- `seed` = `696200972737273`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`VAEDecode`、`FluxKontextMultiReferenceLatentMethod`、`QwenEditOutputExtractor_EditUtils`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`CropWithPadInfo_EditUtils`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`SaveImage`、`KSampler`、`ImageScale`、`QwenEditConfigPreparer`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
