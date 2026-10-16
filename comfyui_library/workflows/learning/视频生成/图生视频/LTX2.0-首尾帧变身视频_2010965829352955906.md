---
key: 视频生成/图生视频/LTX2.0-首尾帧变身视频_2010965829352955906.json
name: LTX2.0-首尾帧变身视频_2010965829352955906.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2010965829352955906.json
hash: 408395ee39ed1142
coverage: 0.738462
learned_at: 2026-10-15 22:34:19
nodes: [KSamplerSelect, RandomNoise, Compare, GetImageSize, GetImageSize, ImageScaleBy, GetImageSize, Compare, easy ifElse, PreviewImage, GetImageSize, LTXVScheduler, LTXVPreprocess, PreviewImage, LTXVPreprocess, PreviewImage, easy ifElse, EmptyImage, PreviewImage, GetNode, GetNode, LTXVAudioVAEDecode, CLIPTextEncode, CLIPTextEncode, LTXVEmptyLatentAudio, GetNode, GetNode, LTXVFirstLastFrameControl_TTP, MathExpression|pysssss, Int, Note, GetNode, GetNode, LTXVConditioning, Seed_, LTXVConcatAVLatent, LTXVSeparateAVLatent, SamplerCustomAdvanced, Note, EmptyLTXVLatentVideo, CFGGuider, VAEDecode, LayerUtility: PurgeVRAM V2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, RHHiddenNodes, SetNode, easy cleanGpuUsed, CheckpointLoaderSimple, LTXVAudioVAELoader, SetNode, SetNode, LTXAVTextEncoderLoader, LoraLoaderModelOnly, LatentUpscaleModelLoader, LoraLoaderModelOnly, easy cleanGpuUsed, LoadImage, LoadImage, CR Text, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp4.safetensors", "height": 24, "width": 97}
---

# 视频生成/图生视频/LTX2.0-首尾帧变身视频_2010965829352955906.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2010965829352955906.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（65 个）：
- `KSamplerSelect` ★核心
- `RandomNoise`
- `Compare`
- `GetImageSize`
- `GetImageSize`
- `ImageScaleBy`
- `GetImageSize`
- `Compare`
- `easy ifElse`
- `PreviewImage`
- `GetImageSize`
- `LTXVScheduler`
- `LTXVPreprocess`
- `PreviewImage`
- `LTXVPreprocess`
- `PreviewImage`
- `easy ifElse`
- `EmptyImage`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `LTXVFirstLastFrameControl_TTP`
- `MathExpression|pysssss`
- `Int`
- `Note`
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `Seed_`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `Note`
- `EmptyLTXVLatentVideo`
- `CFGGuider`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `RHHiddenNodes`
- `SetNode`
- `easy cleanGpuUsed`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `SetNode`
- `SetNode`
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `easy cleanGpuUsed`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp4.safetensors`

## 知识

覆盖率 **74%**（48/65）

**有卡**：`KSamplerSelect`、`RandomNoise`、`Compare`、`GetImageSize`、`ImageScaleBy`、`LTXVScheduler`、`LTXVPreprocess`、`EmptyImage`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`LTXVEmptyLatentAudio`、`LTXVFirstLastFrameControl_TTP`、`MathExpression|pysssss`、`Int`、`LTXVConditioning`、`Seed_`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`EmptyLTXVLatentVideo`、`CFGGuider`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`ImageResizeKJv2`、`ResizeImagesByLongerEdge`、`RHHiddenNodes`、`easy cleanGpuUsed`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`LoadImage`、`CR Text`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
