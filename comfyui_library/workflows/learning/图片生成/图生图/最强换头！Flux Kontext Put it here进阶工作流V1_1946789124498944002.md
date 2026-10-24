---
key: 图片生成/图生图/最强换头！Flux Kontext Put it here进阶工作流V1_1946789124498944002.json
name: 最强换头！Flux Kontext Put it here进阶工作流V1_1946789124498944002
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/最强换头！Flux Kontext Put it here进阶工作流V1_1946789124498944002.json
hash: 6967bcc6b2ed7093
coverage: 0.864865
learned_at: 2026-10-23 13:06:23
nodes: [VAELoader, ConditioningZeroOut, LoadImageOutput, VAEEncode, MarkdownNote, ImageStitch, GoogleTranslateTextNode, ImageConcanate, FastCanvasTool, LoadImage, LoadImage, PreviewImage, RMBG, SaveImage, SaveImage, Note, Note, PDIMAGE_LongerSize, LoadImage, Note, LayerUtility: PurgeVRAM, FluxGuidance, ReferenceLatent, CLIPTextEncode, GoogleTranslateTextNode, CLIPTextEncode, ReferenceLatent, ConditioningZeroOut, FluxGuidance, KSampler, CR Prompt Text, SaveImage, DualCLIPLoader, CR Prompt Text, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageConcanate, PMRF, ImageConcanate, PulidFluxEvaClipLoader, PrimitiveInt, easy cleanGpuUsed, TTP_Expand_And_Mask, UnetLoaderGGUF, SaveImage, ImageCropper, FluxKontextImageScale, PreviewImage, FastCanvas, LoraLoaderModelOnly, PDIMAGE_LongerSize, PDIMAGE_LongerSize, SaveImage, PulidFluxModelLoader, PulidFluxInsightFaceLoader, ApplyPulidFlux, TeaCache, LoraLoaderModelOnly, LayerUtility: PurgeVRAM, VAEDecode, KSampler, SaveImage, Note, Note, SaveImage, Note, SaveImage, SaveImage, SaveImage, SaveImage, SaveImage, SaveImage, ApplyPulidFlux, VAEDecode]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 470980558160963, "steps": 30}
---

# 图片生成/图生图/最强换头！Flux Kontext Put it here进阶工作流V1_1946789124498944002.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/最强换头！Flux Kontext Put it here进阶工作流V1_1946789124498944002.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（74 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `LoadImageOutput`
- `VAEEncode` ★核心
- `MarkdownNote`
- `ImageStitch`
- `GoogleTranslateTextNode`
- `ImageConcanate`
- `FastCanvasTool`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `RMBG`
- `SaveImage`
- `SaveImage`
- `Note`
- `Note`
- `PDIMAGE_LongerSize`
- `LoadImage`
- `Note`
- `LayerUtility: PurgeVRAM`
- `FluxGuidance`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `GoogleTranslateTextNode`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `FluxGuidance`
- `KSampler` ★核心
- `CR Prompt Text`
- `SaveImage`
- `DualCLIPLoader`
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageConcanate`
- `PMRF`
- `ImageConcanate`
- `PulidFluxEvaClipLoader`
- `PrimitiveInt`
- `easy cleanGpuUsed`
- `TTP_Expand_And_Mask`
- `UnetLoaderGGUF` ★核心
- `SaveImage`
- `ImageCropper`
- `FluxKontextImageScale`
- `PreviewImage`
- `FastCanvas`
- `LoraLoaderModelOnly` ★核心
- `PDIMAGE_LongerSize`
- `PDIMAGE_LongerSize`
- `SaveImage`
- `PulidFluxModelLoader`
- `PulidFluxInsightFaceLoader`
- `ApplyPulidFlux`
- `TeaCache`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `Note`
- `Note`
- `SaveImage`
- `Note`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `ApplyPulidFlux`
- `VAEDecode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `470980558160963`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（64/74）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`LoadImageOutput`、`VAEEncode`、`ImageStitch`、`GoogleTranslateTextNode`、`ImageConcanate`、`FastCanvasTool`、`LoadImage`、`RMBG`、`SaveImage`、`PDIMAGE_LongerSize`、`LayerUtility: PurgeVRAM`、`FluxGuidance`、`ReferenceLatent`、`CLIPTextEncode`、`KSampler`、`CR Prompt Text`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`PMRF`、`PulidFluxEvaClipLoader`、`easy cleanGpuUsed`、`TTP_Expand_And_Mask`、`UnetLoaderGGUF`、`ImageCropper`、`FluxKontextImageScale`、`FastCanvas`、`PulidFluxModelLoader`、`PulidFluxInsightFaceLoader`、`ApplyPulidFlux`、`TeaCache`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage
