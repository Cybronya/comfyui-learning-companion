---
key: 视频生成/图生视频/ltx2.3 控制视频_2037918767392493570.json
name: ltx2.3 控制视频_2037918767392493570.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2037918767392493570.json
hash: e4a471383b8f29d4
coverage: 0.898305
learned_at: 2026-10-15 22:36:00
nodes: [ManualSigmas, RandomNoise, Reroute, Reroute, DWPreprocessor, SamplerCustomAdvanced, CFGGuider, LTXVConcatAVLatent, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, ImageResizeKJv2, VAEDecodeTiled, CFGGuider, LTXVScheduler, VHS_VideoCombine, LTXVCropGuides, SamplerCustomAdvanced, RandomNoise, LTXAddVideoICLoRAGuide, LTXVConcatAVLatent, CannyEdgePreprocessor, PrimitiveNode, PrimitiveNode, KSamplerSelect, KSamplerSelect, ImageResizeKJv2, LTXVImgToVideoInplace, VAEDecodeTiled, LTXVSeparateAVLatent, LTXVSeparateAVLatent, LatentUpscaleModelLoader, DownloadAndLoadDepthCrafterModel, Reroute, CLIPTextEncode, VHS_VideoInfo, LTXVPreprocess, CM_FloatToInt, GetImageSize, LTXVEmptyLatentAudio, DualCLIPLoader, VHS_VideoCombine, EmptyLTXVLatentVideo, LTXVConditioning, ImpactExecutionOrderController, Reroute, SimpleMath+, VHS_LoadVideo, LoadImage, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, VAELoader, VAELoaderKJ, VHS_VideoCombine, UnetLoaderGGUF, DepthCrafter, ResizeImageMaskNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/ltx2.3 控制视频_2037918767392493570.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037918767392493570.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（59 个）：
- `ManualSigmas`
- `RandomNoise`
- `Reroute`
- `Reroute`
- `DWPreprocessor`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `ImageResizeKJv2`
- `VAEDecodeTiled` ★核心
- `CFGGuider`
- `LTXVScheduler`
- `VHS_VideoCombine`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTXAddVideoICLoRAGuide`
- `LTXVConcatAVLatent`
- `CannyEdgePreprocessor`
- `PrimitiveNode`
- `PrimitiveNode`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `ImageResizeKJv2`
- `LTXVImgToVideoInplace`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `DownloadAndLoadDepthCrafterModel`
- `Reroute`
- `CLIPTextEncode` ★核心
- `VHS_VideoInfo`
- `LTXVPreprocess`
- `CM_FloatToInt`
- `GetImageSize`
- `LTXVEmptyLatentAudio` ★核心
- `DualCLIPLoader`
- `VHS_VideoCombine`
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `ImpactExecutionOrderController`
- `Reroute`
- `SimpleMath+`
- `VHS_LoadVideo`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `UnetLoaderGGUF` ★核心
- `DepthCrafter`
- `ResizeImageMaskNode`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（53/59）

**有卡**：`ManualSigmas`、`RandomNoise`、`DWPreprocessor`、`SamplerCustomAdvanced`、`CFGGuider`、`LTXVConcatAVLatent`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`ImageResizeKJv2`、`VAEDecodeTiled`、`LTXVScheduler`、`VHS_VideoCombine`、`LTXAddVideoICLoRAGuide`、`CannyEdgePreprocessor`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`DownloadAndLoadDepthCrafterModel`、`CLIPTextEncode`、`VHS_VideoInfo`、`LTXVPreprocess`、`CM_FloatToInt`、`GetImageSize`、`LTXVEmptyLatentAudio`、`DualCLIPLoader`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`ImpactExecutionOrderController`、`SimpleMath+`、`VHS_LoadVideo`、`LoadImage`、`LoraLoaderModelOnly`、`LTXICLoRALoaderModelOnly`、`VAELoader`、`VAELoaderKJ`、`UnetLoaderGGUF`、`DepthCrafter`、`ResizeImageMaskNode`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、CannyEdgePreprocessor、DepthCrafter、DownloadAndLoadDepthCrafterModel、CFGGuider
