---
key: 平台全量/LTX-2.3 视频去字幕_动态水印_2062353654644043778.json
name: LTX-2.3 视频去字幕_动态水印_2062353654644043778
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX-2.3 视频去字幕_动态水印_2062353654644043778.json
hash: 251a656b77387fe5
coverage: 0.554054
learned_at: 2026-11-14 00:36:52
nodes: [SetNode, SetNode, LTXVPreprocess, GetNode, GetNode, GetNode, LTXVImgToVideoConditionOnly, CLIPTextEncode, LTXVEmptyLatentAudio, GetNode, CFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, GetNode, SetNode, VAELoaderKJ, GetNode, GetNode, Float to Int, SetNode, SetNode, ImageFromBatch, ResizeImageMaskNode, SetNode, SolidMask, SetNode, SolidMask, SetNode, GetNode, GetNode, VAEEncodeForInpaint, VAELoaderKJ, SetNode, SetNode, GetNode, CLIPTextEncode, GetNode, LTXAddVideoICLoRAGuide, GetNode, RandomNoise, LTXVConcatAVLatent, Reroute, Reroute, GetNode, VAEDecodeTiled, easy cleanGpuUsed, GetNode, GetNode, Reroute, LTXVConditioning, Reroute, Reroute, Reroute, DiffusionModelLoaderKJ, LTXVCropGuides, DualCLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, LayerUtility: ColorImage, VHS_VideoInfo, LoraLoaderModelOnly, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, MaskPreview, RepeatImageBatch, Image To Mask, GetImageSize, SimpleMath+, MaskComposite, SetNode, VHS_LoadVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/LTX-2.3 视频去字幕_动态水印_2062353654644043778.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX-2.3 视频去字幕_动态水印_2062353654644043778.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（74 个）：
- `SetNode`
- `SetNode`
- `LTXVPreprocess`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoConditionOnly`
- `CLIPTextEncode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `SetNode`
- `VAELoaderKJ`
- `GetNode`
- `GetNode`
- `Float to Int`
- `SetNode`
- `SetNode`
- `ImageFromBatch`
- `ResizeImageMaskNode`
- `SetNode`
- `SolidMask`
- `SetNode`
- `SolidMask`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAEEncodeForInpaint` ★核心
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `LTXAddVideoICLoRAGuide`
- `GetNode`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `Reroute`
- `Reroute`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `Reroute`
- `LTXVConditioning`
- `Reroute`
- `Reroute`
- `Reroute`
- `DiffusionModelLoaderKJ`
- `LTXVCropGuides`
- `DualCLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `LayerUtility: ColorImage`
- `VHS_VideoInfo`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MaskPreview`
- `RepeatImageBatch`
- `Image To Mask`
- `GetImageSize`
- `SimpleMath+`
- `MaskComposite`
- `SetNode`
- `VHS_LoadVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **55%**（41/74）

**有卡**：`LTXVPreprocess`、`LTXVImgToVideoConditionOnly`、`CLIPTextEncode`、`LTXVEmptyLatentAudio`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`VAELoaderKJ`、`Float to Int`、`ImageFromBatch`、`ResizeImageMaskNode`、`SolidMask`、`VAEEncodeForInpaint`、`LTXAddVideoICLoRAGuide`、`RandomNoise`、`LTXVConcatAVLatent`、`VAEDecodeTiled`、`easy cleanGpuUsed`、`LTXVConditioning`、`DiffusionModelLoaderKJ`、`LTXVCropGuides`、`DualCLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`LayerUtility: ColorImage`、`VHS_VideoInfo`、`LoraLoaderModelOnly`、`MaskPreview`、`RepeatImageBatch`、`Image To Mask`、`GetImageSize`、`SimpleMath+`、`MaskComposite`、`VHS_LoadVideo`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVEmptyLatentAudio
