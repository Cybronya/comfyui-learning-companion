---
key: 平台全量/遮罩编辑&Qwen+Edit-2511.HQ14（修改万物指哪里改哪里）_2024049627607080961.json
name: 遮罩编辑&Qwen+Edit-2511.HQ14（修改万物指哪里改哪里）_2024049627607080961
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/遮罩编辑&Qwen+Edit-2511.HQ14（修改万物指哪里改哪里）_2024049627607080961.json
hash: 78ceaa73b4b8af76
coverage: 0.909091
learned_at: 2026-11-14 02:48:50
nodes: [TextEncodeQwenImageEditPlusCustom_lrzjason, VAEDecode, CropWithPadInfo, ImageScaleBy, VAELoader, CLIPLoader, UNETLoader, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, VAEEncode, SetLatentNoiseMask, easy ifElse, LayerUtility: ImageScaleByAspectRatio V2, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, LayerUtility: ImageScaleByAspectRatio V2, QwenEditConfigPreparer, ToBinaryMask, QwenEditAdaptiveLongestEdge, KSampler, QwenEditOutputExtractor, LoraLoaderModelOnly, ReferenceLatent, ConditioningZeroOut, Mask Fill Holes, easy boolean, SaveImage, LoadImage, LoadImage, PrimitiveStringMultiline, Note, LoadImage, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 1071877229727775, "steps": 14}
---

# 平台全量/遮罩编辑&Qwen+Edit-2511.HQ14（修改万物指哪里改哪里）_2024049627607080961.json

> 来源文件 `comfyui_library/workflows/平台全量/遮罩编辑&Qwen+Edit-2511.HQ14（修改万物指哪里改哪里）_2024049627607080961.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `VAEDecode` ★核心
- `CropWithPadInfo`
- `ImageScaleBy`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `easy ifElse`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditConfigPreparer`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `QwenEditConfigPreparer`
- `ToBinaryMask`
- `QwenEditAdaptiveLongestEdge`
- `KSampler` ★核心
- `QwenEditOutputExtractor`
- `LoraLoaderModelOnly` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `Mask Fill Holes`
- `easy boolean`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `Note`
- `LoadImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1071877229727775`
- `steps` = `14`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **91%**（30/33）

**有卡**：`TextEncodeQwenImageEditPlusCustom_lrzjason`、`VAEDecode`、`CropWithPadInfo`、`ImageScaleBy`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`FluxKontextMultiReferenceLatentMethod`、`VAEEncode`、`SetLatentNoiseMask`、`LayerUtility: ImageScaleByAspectRatio V2`、`QwenEditAdaptiveLongestEdge`、`QwenEditConfigPreparer`、`ToBinaryMask`、`KSampler`、`QwenEditOutputExtractor`、`LoraLoaderModelOnly`、`ReferenceLatent`、`ConditioningZeroOut`、`Mask Fill Holes`、`easy boolean`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、SaveImage
