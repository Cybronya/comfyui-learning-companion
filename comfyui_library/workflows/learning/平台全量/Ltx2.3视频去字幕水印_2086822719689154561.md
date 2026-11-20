---
key: 平台全量/Ltx2.3视频去字幕水印_2086822719689154561.json
name: Ltx2.3视频去字幕水印_2086822719689154561
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Ltx2.3视频去字幕水印_2086822719689154561.json
hash: 4b37fb30af2f9efd
coverage: 0.568966
learned_at: 2026-11-14 00:39:29
nodes: [VAELoaderKJ, SetNode, VAELoaderKJ, SetNode, SetNode, DualCLIPLoader, GetNode, GetNode, LTXFloatToInt, LTXVEmptyLatentAudio, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPTextEncode, GetNode, LTXAddVideoICLoRAGuide, GetNode, VHS_VideoInfo, SetNode, LTXVConditioning, GetNode, GetNode, GetNode, Reroute, Reroute, SetNode, GetNode, SolidMask, MaskPreview, ImageFromBatch, SetNode, SetNode, SetNode, GetNode, VAEEncodeForInpaint, LTXVImgToVideoConditionOnly, GetNode, LTXVCropGuides, VAEDecodeTiled, easy cleanGpuUsed, CFGGuider, LayerUtility: ImageScaleByAspectRatio V2, ResizeImageMaskNode, GetNode, LTXVConcatAVLatent, LTXVPreprocess, GetNode, GetNode, SetNode, SetNode, CLIPTextEncode, RandomNoise, VHS_VideoCombine, VHS_LoadVideo, LoraLoaderModelOnly, DiffusionModelLoaderKJ, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/Ltx2.3视频去字幕水印_2086822719689154561.json

> 来源文件 `comfyui_library/workflows/平台全量/Ltx2.3视频去字幕水印_2086822719689154561.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（58 个）：
- `VAELoaderKJ`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `DualCLIPLoader`
- `GetNode`
- `GetNode`
- `LTXFloatToInt`
- `LTXVEmptyLatentAudio` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `GetNode`
- `LTXAddVideoICLoRAGuide`
- `GetNode`
- `VHS_VideoInfo`
- `SetNode`
- `LTXVConditioning`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `Reroute`
- `SetNode`
- `GetNode`
- `SolidMask`
- `MaskPreview`
- `ImageFromBatch`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `VAEEncodeForInpaint` ★核心
- `LTXVImgToVideoConditionOnly`
- `GetNode`
- `LTXVCropGuides`
- `VAEDecodeTiled` ★核心
- `easy cleanGpuUsed`
- `CFGGuider`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ResizeImageMaskNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVPreprocess`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoraLoaderModelOnly` ★核心
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **57%**（33/58）

**有卡**：`VAELoaderKJ`、`DualCLIPLoader`、`LTXFloatToInt`、`LTXVEmptyLatentAudio`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`CLIPTextEncode`、`LTXAddVideoICLoRAGuide`、`VHS_VideoInfo`、`LTXVConditioning`、`SolidMask`、`MaskPreview`、`ImageFromBatch`、`VAEEncodeForInpaint`、`LTXVImgToVideoConditionOnly`、`LTXVCropGuides`、`VAEDecodeTiled`、`easy cleanGpuUsed`、`CFGGuider`、`LayerUtility: ImageScaleByAspectRatio V2`、`ResizeImageMaskNode`、`LTXVConcatAVLatent`、`LTXVPreprocess`、`RandomNoise`、`VHS_VideoCombine`、`VHS_LoadVideo`、`LoraLoaderModelOnly`、`DiffusionModelLoaderKJ`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVEmptyLatentAudio
