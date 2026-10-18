---
key: 视频生成/图生视频/LTXV2.0图生视频+对话配音_2010611172453654529.json
name: LTXV2.0图生视频+对话配音_2010611172453654529.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTXV2.0图生视频+对话配音_2010611172453654529.json
hash: 82ec32f0086caf6f
coverage: 0.505618
learned_at: 2026-10-15 22:34:17
nodes: [SetNode, CFGGuider, SetNode, SetNode, GetNode, SetNode, SetNode, GetImageSize, VAEDecodeTiled, CLIPTextEncode, EmptyLTXVLatentVideo, ImageScaleBy, SimpleMath+, GetNode, GetNode, SetNode, PrimitiveInt, GetNode, GetNode, GetNode, GetNode, GetNode, ResizeImagesByLongerEdge, LTXVPreprocess, ManualSigmas, LTXVConditioning, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, LTXVEmptyLatentAudio, GetNode, SetNode, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, PrimitiveFloat, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, PrimitiveInt, SetNode, Int, MarkdownNote, SetNode, MarkdownNote, MarkdownNote, LTXVAudioVAEDecode, LatentUpscaleModelLoader, VHS_VideoCombine, EmptyImage, GetNode, CLIPTextEncode, MarkdownNote, MarkdownNote, MarkdownNote, LTXVLatentUpsampler, easy cleanGpuUsed, GetNode, CR Text, LTXVAudioVAELoader, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LayerUtility: ImageScaleByAspectRatio V2, CFGGuider, RandomNoise, RandomNoise, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, GetNode, GetNode, easy cleanGpuUsed, KSamplerSelect, KSamplerSelect, LTXVScheduler, LTXVImgToVideoInplace, LTXVConcatAVLatent, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTXV2.0图生视频+对话配音_2010611172453654529.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2010611172453654529.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（89 个）：
- `SetNode`
- `CFGGuider`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetImageSize`
- `VAEDecodeTiled` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLTXVLatentVideo`
- `ImageScaleBy`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `SetNode`
- `PrimitiveInt`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ManualSigmas`
- `LTXVConditioning`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `SetNode`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `PrimitiveInt`
- `SetNode`
- `Int`
- `MarkdownNote`
- `SetNode`
- `MarkdownNote`
- `MarkdownNote`
- `LTXVAudioVAEDecode` ★核心
- `LatentUpscaleModelLoader`
- `VHS_VideoCombine`
- `EmptyImage`
- `GetNode`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LTXVLatentUpsampler` ★核心
- `easy cleanGpuUsed`
- `GetNode`
- `CR Text`
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CFGGuider`
- `RandomNoise`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **51%**（45/89）

**有卡**：`CFGGuider`、`GetImageSize`、`VAEDecodeTiled`、`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`ImageScaleBy`、`SimpleMath+`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`ManualSigmas`、`LTXVConditioning`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`Int`、`LTXVAudioVAEDecode`、`LatentUpscaleModelLoader`、`VHS_VideoCombine`、`EmptyImage`、`LTXVLatentUpsampler`、`easy cleanGpuUsed`、`CR Text`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`RandomNoise`、`LTXVCropGuides`、`KSamplerSelect`、`LTXVScheduler`、`LTXVImgToVideoInplace`、`LoraLoaderModelOnly`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
