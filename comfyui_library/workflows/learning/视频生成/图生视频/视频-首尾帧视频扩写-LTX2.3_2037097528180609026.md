---
key: 视频生成/图生视频/视频-首尾帧视频扩写-LTX2.3_2037097528180609026.json
name: 视频-首尾帧视频扩写-LTX2.3_2037097528180609026.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/视频-首尾帧视频扩写-LTX2.3_2037097528180609026.json
hash: a6fcbdc7456219be
coverage: 0.736842
learned_at: 2026-10-15 22:35:55
nodes: [easy showAnything, GetNode, GetNode, GetNode, GetNode, PreviewImage, GetImageSizeAndCount, GetNode, SetNode, SetNode, GetNode, SetNode, StringFunction|pysssss, LayerUtility: ImageScaleByAspectRatio V2, SetNode, MemoryCleaner, SetNode, MathExpression|pysssss, SetNode, SetNode, easy showAnything, GetNode, StringFunction|pysssss, GetImageSizeAndCount, GetImageSizeAndCount, RH_LLMAPI_NODE, SetNode, ImageResizeKJ, GetImageSizeAndCount, PreviewImage, easy positive, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, KSamplerSelect, Reroute, CLIPTextEncode, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAELoader, CFGGuider, LTXVConditioning, RandomNoise, RandomNoise, LTXAVTextEncoderLoader, CLIPTextEncode, LatentUpscaleModelLoader, CheckpointLoaderSimple, LTXVConcatAVLatent, LTXVLatentUpsampler, LTXVImgToVideoInplace, FloatConstant, PathchSageAttentionKJ, LTXVChunkFeedForward, ModelPatchTorchSettings, LoraLoaderModelOnly, ManualSigmas, LTXVImgToVideoInplaceKJ, EmptyLTXVLatentVideo, GetImageSizeAndCount, easy seed, Reroute, INTConstant, LTXVPreprocess, GetImageSizeAndCount, LTXVPreprocess, GetImageSizeAndCount, GetNode, LTXVAudioVAEDecode, VAEDecodeTiled, VHS_VideoCombine, easy imageSize, GetImageSizeAndCount, GetNode, GetNode, easy anythingIndexSwitch, GetImageSizeAndCount, ImageScaleBy, ImpactFloat, GetImageSizeAndCount, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, ImageLoader, ImageLoader, easy int, PrimitiveFloat, easy positive, easy int, ComfyMathExpression, LTXVEmptyLatentAudio, ComfyMathExpression]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/视频-首尾帧视频扩写-LTX2.3_2037097528180609026.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037097528180609026.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（95 个）：
- `easy showAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `GetImageSizeAndCount`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `StringFunction|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `MemoryCleaner`
- `SetNode`
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `GetNode`
- `StringFunction|pysssss`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `RH_LLMAPI_NODE`
- `SetNode`
- `ImageResizeKJ`
- `GetImageSizeAndCount`
- `PreviewImage`
- `easy positive`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `KSamplerSelect` ★核心
- `Reroute`
- `CLIPTextEncode` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAELoader`
- `CFGGuider`
- `LTXVConditioning`
- `RandomNoise`
- `RandomNoise`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `LatentUpscaleModelLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `FloatConstant`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `ModelPatchTorchSettings`
- `LoraLoaderModelOnly` ★核心
- `ManualSigmas`
- `LTXVImgToVideoInplaceKJ`
- `EmptyLTXVLatentVideo`
- `GetImageSizeAndCount`
- `easy seed`
- `Reroute`
- `INTConstant`
- `LTXVPreprocess`
- `GetImageSizeAndCount`
- `LTXVPreprocess`
- `GetImageSizeAndCount`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `easy imageSize`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `easy anythingIndexSwitch`
- `GetImageSizeAndCount`
- `ImageScaleBy`
- `ImpactFloat`
- `GetImageSizeAndCount`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `ImageLoader`
- `ImageLoader`
- `easy int`
- `PrimitiveFloat`
- `easy positive`
- `easy int`
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `ComfyMathExpression`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **74%**（70/95）

**有卡**：`GetImageSizeAndCount`、`StringFunction|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`MemoryCleaner`、`MathExpression|pysssss`、`RH_LLMAPI_NODE`、`ImageResizeKJ`、`easy positive`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`CLIPTextEncode`、`LTXVSeparateAVLatent`、`LTXVAudioVAELoader`、`LTXVConditioning`、`RandomNoise`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`CheckpointLoaderSimple`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`FloatConstant`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`LoraLoaderModelOnly`、`LTXVImgToVideoInplaceKJ`、`EmptyLTXVLatentVideo`、`easy seed`、`INTConstant`、`LTXVPreprocess`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`VHS_VideoCombine`、`easy imageSize`、`easy anythingIndexSwitch`、`ImageScaleBy`、`ImpactFloat`、`ResizeImagesByLongerEdge`、`ImageLoader`、`easy int`、`ComfyMathExpression`、`LTXVEmptyLatentAudio`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
