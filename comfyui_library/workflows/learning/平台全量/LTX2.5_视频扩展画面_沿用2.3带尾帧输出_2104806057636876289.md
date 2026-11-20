---
key: 平台全量/LTX2.5_视频扩展画面_沿用2.3带尾帧输出_2104806057636876289.json
name: LTX2.5_视频扩展画面_沿用2.3带尾帧输出_2104806057636876289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.5_视频扩展画面_沿用2.3带尾帧输出_2104806057636876289.json
hash: 22e77943a8f924cc
coverage: 0.935484
learned_at: 2026-11-14 00:39:09
nodes: [VAELoader, VAELoader, UNETLoader, CLIPLoader, LTXICLoRALoaderModelOnly, ResizeImageMaskNode, ResizeImageMaskNode, ResizeImageMaskNode, ResizeImageMaskNode, LTXVConditioning, EmptyLTXVLatentVideo, GetImageSize, LTXVInpaintPreprocess, LTXVImgToVideoConditionOnly, LTXAddVideoICLoRAGuideAdvanced, LTXVConcatAVLatent, LTXVPreprocess, RandomNoise, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, ManualSigmas, KSamplerSelect, ResizeImageMaskNode, VAEEncodeTiled, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, ManualSigmas, CFGGuider, RandomNoise, SamplerCustomAdvanced, LTXVSeparateAVLatent, KSamplerSelect, VAEDecodeTiled, LTXVLaplacianPyramidBlend, VAEDecodeTiled, LTXVLaplacianPyramidBlend, LTXVInpaintPreprocess, ImageScaleBy, ycImageCropBatchApply, LoadImage, PrimitiveBoolean, VHS_VideoInfo, LTXVEmptyLatentAudio, CM_FloatToInt, CLIPTextEncode, ImageFromBatch, ResizeImageMaskNode, ResizeImageMaskNode, PrimitiveFloat, ImageFromBatch, PreviewImage, MaskToImage, PreviewImage, CLIPTextEncode, ycImageCropInteractive, VHS_LoadVideo, Note, VHS_VideoCombine, ImageFromBatch, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/LTX2.5_视频扩展画面_沿用2.3带尾帧输出_2104806057636876289.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.5_视频扩展画面_沿用2.3带尾帧输出_2104806057636876289.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LTXICLoRALoaderModelOnly` ★核心
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `LTXVInpaintPreprocess`
- `LTXVImgToVideoConditionOnly`
- `LTXAddVideoICLoRAGuideAdvanced`
- `LTXVConcatAVLatent`
- `LTXVPreprocess`
- `RandomNoise`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ResizeImageMaskNode`
- `VAEEncodeTiled` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `CFGGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVLaplacianPyramidBlend`
- `VAEDecodeTiled` ★核心
- `LTXVLaplacianPyramidBlend`
- `LTXVInpaintPreprocess`
- `ImageScaleBy`
- `ycImageCropBatchApply`
- `LoadImage`
- `PrimitiveBoolean`
- `VHS_VideoInfo`
- `LTXVEmptyLatentAudio` ★核心
- `CM_FloatToInt`
- `CLIPTextEncode` ★核心
- `ImageFromBatch`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `PrimitiveFloat`
- `ImageFromBatch`
- `PreviewImage`
- `MaskToImage`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `ycImageCropInteractive`
- `VHS_LoadVideo`
- `Note`
- `VHS_VideoCombine`
- `ImageFromBatch`
- `SaveImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（58/62）

**有卡**：`VAELoader`、`UNETLoader`、`CLIPLoader`、`LTXICLoRALoaderModelOnly`、`ResizeImageMaskNode`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`GetImageSize`、`LTXVInpaintPreprocess`、`LTXVImgToVideoConditionOnly`、`LTXAddVideoICLoRAGuideAdvanced`、`LTXVConcatAVLatent`、`LTXVPreprocess`、`RandomNoise`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`ManualSigmas`、`KSamplerSelect`、`VAEEncodeTiled`、`VAEDecodeTiled`、`LTXVLaplacianPyramidBlend`、`ImageScaleBy`、`ycImageCropBatchApply`、`LoadImage`、`PrimitiveBoolean`、`VHS_VideoInfo`、`LTXVEmptyLatentAudio`、`CM_FloatToInt`、`CLIPTextEncode`、`ImageFromBatch`、`MaskToImage`、`ycImageCropInteractive`、`VHS_LoadVideo`、`VHS_VideoCombine`、`SaveImage`

**用到的条目**：VAELoader、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
