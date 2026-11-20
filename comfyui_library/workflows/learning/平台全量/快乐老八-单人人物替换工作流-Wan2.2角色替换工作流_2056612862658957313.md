---
key: 平台全量/快乐老八-单人人物替换工作流-Wan2.2角色替换工作流_2056612862658957313.json
name: 快乐老八-单人人物替换工作流-Wan2.2角色替换工作流_2056612862658957313
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/快乐老八-单人人物替换工作流-Wan2.2角色替换工作流_2056612862658957313.json
hash: 47d0038693e9153f
coverage: 0.417476
learned_at: 2026-11-14 02:04:13
nodes: [GetNode, GetNode, GetNode, PixelPerfectResolution, LoraLoaderModelOnly, GetNode, GetNode, SetNode, LoraLoaderModelOnly, GetNode, GetNode, ModelSamplingSD3, SetNode, CLIPTextEncode, SetNode, CLIPTextEncode, SetNode, SetNode, GetNode, CLIPLoader, VAELoader, SetNode, UNETLoader, CLIPVisionLoader, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, ImageCropByMaskAndResize, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, TrimVideoLatent, GetNode, SetNode, DrawMaskOnImage, VAEDecode, SetNode, SetNode, MaskToImage, GetNode, SetNode, GrowMaskWithBlur, GetNode, GetNode, BlockifyMask, Sam2VideoSegmentationAddPoints, GetNode, GetNode, Sam2VideoSegmentation, GetNode, LayerUtility: ColorImage V2, LayerUtility: ImageBlendAdvance, SetNode, ImageResizeKJv2, GetNode, WanAnimateToVideo, DownloadAndLoadSAM2Model, KSampler, GetNode, GetNode, SetNode, DWPreprocessor, GetNode, GetNode, GetNode, FaceMaskFromPoseKeypoints, GetNode, Note, SetNode, SetNode, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, MarkdownNote, PreviewImage, ImageResize+, PreviewAny, LoadImage, PreviewImage, PointsEditor, LoadImage, Int, CLIPVisionEncode, INTConstant, INTConstant, SetNode, SetNode, VHS_LoadVideo, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModel]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 182505181983086, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/快乐老八-单人人物替换工作流-Wan2.2角色替换工作流_2056612862658957313.json

> 来源文件 `comfyui_library/workflows/平台全量/快乐老八-单人人物替换工作流-Wan2.2角色替换工作流_2056612862658957313.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（103 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `PixelPerfectResolution`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `ModelSamplingSD3`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `UNETLoader` ★核心
- `CLIPVisionLoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageCropByMaskAndResize`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `TrimVideoLatent`
- `GetNode`
- `SetNode`
- `DrawMaskOnImage`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `MaskToImage`
- `GetNode`
- `SetNode`
- `GrowMaskWithBlur`
- `GetNode`
- `GetNode`
- `BlockifyMask`
- `Sam2VideoSegmentationAddPoints`
- `GetNode`
- `GetNode`
- `Sam2VideoSegmentation`
- `GetNode`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlendAdvance`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `WanAnimateToVideo`
- `DownloadAndLoadSAM2Model`
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `DWPreprocessor`
- `GetNode`
- `GetNode`
- `GetNode`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `Note`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MarkdownNote`
- `PreviewImage`
- `ImageResize+`
- `PreviewAny`
- `LoadImage`
- `PreviewImage`
- `PointsEditor`
- `LoadImage`
- `Int`
- `CLIPVisionEncode`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModel`

## 关键参数

- `seed` = `182505181983086`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **42%**（43/103）

**有卡**：`PixelPerfectResolution`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`CLIPVisionLoader`、`ImageCropByMaskAndResize`、`TrimVideoLatent`、`DrawMaskOnImage`、`VAEDecode`、`MaskToImage`、`GrowMaskWithBlur`、`BlockifyMask`、`Sam2VideoSegmentationAddPoints`、`Sam2VideoSegmentation`、`LayerUtility: ColorImage V2`、`LayerUtility: ImageBlendAdvance`、`ImageResizeKJv2`、`WanAnimateToVideo`、`DownloadAndLoadSAM2Model`、`KSampler`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`VHS_VideoCombine`、`ImageResize+`、`LoadImage`、`PointsEditor`、`Int`、`CLIPVisionEncode`、`INTConstant`、`VHS_LoadVideo`、`LayerMask: BiRefNetUltraV2`、`LayerMask: LoadBiRefNetModel`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
