---
key: 平台全量/LTX-2.3_ICLoRA_cameraman_v2-3D草图生成视频_2078240780807925761.json
name: LTX-2.3_ICLoRA_cameraman_v2-3D草图生成视频_2078240780807925761
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX-2.3_ICLoRA_cameraman_v2-3D草图生成视频_2078240780807925761.json
hash: afc3b038b3238213
coverage: 0.759494
learned_at: 2026-11-14 00:37:09
nodes: [CFGGuider, KSamplerSelect, LTXVAudioVAEDecode, VAEDecodeTiled, RandomNoise, SetNode, SetNode, SetNode, SetNode, LTXVSeparateAVLatent, LTXVCropGuides, SetNode, LTXVConcatAVLatent, ManualSigmas, SetNode, SetNode, SetNode, SetNode, LTXVConditioning, CLIPTextEncode, SetNode, GetNode, SimpleMath+, SetNode, VAELoaderKJ, DualCLIPLoader, LatentUpscaleModelLoader, ImageResizeKJv2, SamplerCustomAdvanced, VAELoaderKJ, SetNode, PrimitiveBoolean, LTXVEmptyLatentAudio, GetImageSize, EmptyLTXVLatentVideo, LTXVPreprocess, UNETLoader, LTXVImgToVideoConditionOnly, LTXAddVideoICLoRAGuide, ReferenceLatent, CFGGuider, SamplerCustomAdvanced, KSamplerSelect, ConditioningZeroOut, CLIPLoader, VAELoader, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), UNETLoader, LoraLoaderModelOnly, RandomNoise, VAEEncode, LayerUtility: PurgeVRAM V2, VAEDecode, easy cleanGpuUsed, SetNode, ReferenceLatent, Flux2Scheduler, ImageFromBatch, Fast Groups Bypasser (rgthree), VHS_VideoCombine, LTXICLoRALoaderModelOnly, SaveImage, EmptyFlux2LatentImage, CLIPTextEncode, Int, SimpleMath+, INTConstant, VHS_LoadVideo, CLIPTextEncode, ImageResizeKJv2, VHS_VideoInfo, ImageFromBatch, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, SetNode, INTConstant, Int, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/LTX-2.3_ICLoRA_cameraman_v2-3D草图生成视频_2078240780807925761.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX-2.3_ICLoRA_cameraman_v2-3D草图生成视频_2078240780807925761.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（79 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `RandomNoise`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `SetNode`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `SimpleMath+`
- `SetNode`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `ImageResizeKJv2`
- `SamplerCustomAdvanced` ★核心
- `VAELoaderKJ`
- `SetNode`
- `PrimitiveBoolean`
- `LTXVEmptyLatentAudio` ★核心
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `UNETLoader` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTXAddVideoICLoRAGuide`
- `ReferenceLatent`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `CLIPLoader`
- `VAELoader`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `VAEEncode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `SetNode`
- `ReferenceLatent`
- `Flux2Scheduler`
- `ImageFromBatch`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `LTXICLoRALoaderModelOnly` ★核心
- `SaveImage`
- `EmptyFlux2LatentImage`
- `CLIPTextEncode` ★核心
- `Int`
- `SimpleMath+`
- `INTConstant`
- `VHS_LoadVideo`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `VHS_VideoInfo`
- `ImageFromBatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SimpleMath+`
- `SetNode`
- `INTConstant`
- `Int`
- `PreviewImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **76%**（60/79）

**有卡**：`CFGGuider`、`KSamplerSelect`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVConcatAVLatent`、`ManualSigmas`、`LTXVConditioning`、`CLIPTextEncode`、`SimpleMath+`、`VAELoaderKJ`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`ImageResizeKJv2`、`SamplerCustomAdvanced`、`PrimitiveBoolean`、`LTXVEmptyLatentAudio`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`UNETLoader`、`LTXVImgToVideoConditionOnly`、`LTXAddVideoICLoRAGuide`、`ReferenceLatent`、`ConditioningZeroOut`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`VAEEncode`、`LayerUtility: PurgeVRAM V2`、`VAEDecode`、`easy cleanGpuUsed`、`Flux2Scheduler`、`ImageFromBatch`、`VHS_VideoCombine`、`LTXICLoRALoaderModelOnly`、`SaveImage`、`EmptyFlux2LatentImage`、`Int`、`INTConstant`、`VHS_LoadVideo`、`VHS_VideoInfo`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LayerUtility: ImageScaleByAspectRatio V2
