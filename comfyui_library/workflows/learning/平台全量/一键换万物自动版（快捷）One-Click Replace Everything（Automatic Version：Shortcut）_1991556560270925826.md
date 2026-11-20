---
key: 平台全量/一键换万物自动版（快捷）One-Click Replace Everything（Automatic Version：Shortcut）_1991556560270925826.json
name: 一键换万物自动版（快捷）One-Click Replace Everything（Automatic Version：Shortcut）_1991556560270925826
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/一键换万物自动版（快捷）One-Click Replace Everything（Automatic Version：Shortcut）_1991556560270925826.json
hash: 7dbb11bd6d29d246
coverage: 0.540541
learned_at: 2026-11-14 01:28:09
nodes: [LoraLoaderModelOnly, PreviewImage, Note, Note, ImageScaleToTotalPixels, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, LayerMask: BiRefNetUltraV2, Reroute, Reroute, Reroute, Reroute, TextEncodeQwenImageEditPlusCustom_lrzjason, KSampler, VAEDecode, LayerUtility: ImageReelComposit, CLIPLoader, Reroute, VAELoader, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, LoraLoaderModelOnly, Reroute, Reroute, LayerUtility: ImageBlendAdvance, QwenEditAdaptiveLongestEdge, Reroute, Reroute, QwenEditConfigPreparer, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, SetUnionControlNetType, Reroute, Reroute, MaskFastGrow, MaskToImage, MaskFillHoles, PreviewImage, LayerMask: MaskPreview, LayerUtility: ImageReel, QwenEditAdaptiveLongestEdge, Reroute, PreviewImage, AIO_Preprocessor, LoadImage, SaveImage, LoadImage, LayerMask: PersonMaskUltra V2, LayerMask: MaskGrow, Fast Groups Bypasser (rgthree), ControlNetApplySD3, Reroute, ConcatTextOfUtils, QwenEditConfigPreparer, Note, LayerUtility: ColorImage V2, LayerMask: LoadBiRefNetModelV2, easy clearCacheAll, ControlNetLoader, easy clearCacheAll, ConditioningZeroOut, LayerUtility: ImageScaleByAspectRatio V2, Int, ImageCompositeMasked]
patterns: []
missing: []
parameters: {"cfg": 1, "controlnet_strength": 2, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 913200677084871, "steps": 10}
---

# 平台全量/一键换万物自动版（快捷）One-Click Replace Everything（Automatic Version：Shortcut）_1991556560270925826.json

> 来源文件 `comfyui_library/workflows/平台全量/一键换万物自动版（快捷）One-Click Replace Everything（Automatic Version：Shortcut）_1991556560270925826.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（74 个）：
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `Note`
- `Note`
- `ImageScaleToTotalPixels`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerMask: BiRefNetUltraV2`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageReelComposit`
- `CLIPLoader`
- `Reroute`
- `VAELoader`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `Reroute`
- `LayerUtility: ImageBlendAdvance`
- `QwenEditAdaptiveLongestEdge`
- `Reroute`
- `Reroute`
- `QwenEditConfigPreparer`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `SetUnionControlNetType`
- `Reroute`
- `Reroute`
- `MaskFastGrow`
- `MaskToImage`
- `MaskFillHoles`
- `PreviewImage`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageReel`
- `QwenEditAdaptiveLongestEdge`
- `Reroute`
- `PreviewImage`
- `AIO_Preprocessor`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: MaskGrow`
- `Fast Groups Bypasser (rgthree)`
- `ControlNetApplySD3` ★核心
- `Reroute`
- `ConcatTextOfUtils`
- `QwenEditConfigPreparer`
- `Note`
- `LayerUtility: ColorImage V2`
- `LayerMask: LoadBiRefNetModelV2`
- `easy clearCacheAll`
- `ControlNetLoader`
- `easy clearCacheAll`
- `ConditioningZeroOut`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `ImageCompositeMasked`

## 关键参数

- `seed` = `913200677084871`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`
- `controlnet_strength` = `2`

## 知识

覆盖率 **54%**（40/74）

**有卡**：`LoraLoaderModelOnly`、`ImageScaleToTotalPixels`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerMask: BiRefNetUltraV2`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`KSampler`、`VAEDecode`、`LayerUtility: ImageReelComposit`、`CLIPLoader`、`VAELoader`、`LayerUtility: ImageBlendAdvance`、`QwenEditAdaptiveLongestEdge`、`QwenEditConfigPreparer`、`SetUnionControlNetType`、`MaskFastGrow`、`MaskToImage`、`MaskFillHoles`、`LayerMask: MaskPreview`、`LayerUtility: ImageReel`、`AIO_Preprocessor`、`LoadImage`、`SaveImage`、`LayerMask: PersonMaskUltra V2`、`LayerMask: MaskGrow`、`ControlNetApplySD3`、`ConcatTextOfUtils`、`LayerUtility: ColorImage V2`、`LayerMask: LoadBiRefNetModelV2`、`easy clearCacheAll`、`ControlNetLoader`、`ConditioningZeroOut`、`Int`、`ImageCompositeMasked`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
