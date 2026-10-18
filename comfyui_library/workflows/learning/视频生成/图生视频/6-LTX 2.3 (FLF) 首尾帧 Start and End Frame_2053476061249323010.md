---
key: 视频生成/图生视频/6-LTX 2.3 (FLF) 首尾帧 Start and End Frame_2053476061249323010.json
name: 6-LTX 2.3 (FLF) 首尾帧 Start and End Frame_2053476061249323010.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/6-LTX 2.3 (FLF) 首尾帧 Start and End Frame_2053476061249323010.json
hash: 390b4eeb7e3dea7d
coverage: 0.882353
learned_at: 2026-10-15 22:37:39
nodes: [PrimitiveInt, PrimitiveInt, KSamplerSelect, ImageResizeKJv2, ResizeImagesByLongerEdge, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, CLIPTextEncode, LTXVConditioning, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, ManualSigmas, LTXVPreprocess, KSamplerSelect, CFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, Reroute, RandomNoise, CFGGuider, ManualSigmas, LTXVLatentUpsampler, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVConcatAVLatent, LTXVAudioVAEDecode, RandomNoise, PrimitiveInt, PrimitiveInt, LTXVImgToVideoInplaceKJ, LTXVImgToVideoInplaceKJ, ImageResizeKJv2, ResizeImagesByLongerEdge, LTXVPreprocess, VAEDecode, CreateVideo, easy cleanGpuUsed, easy clearCacheAll, SaveVideo, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LatentUpscaleModelLoader, Note, LoraLoaderModelOnly, CLIPTextEncode, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/6-LTX 2.3 (FLF) 首尾帧 Start and End Frame_2053476061249323010.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2053476061249323010.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `PrimitiveInt`
- `PrimitiveInt`
- `KSamplerSelect` ★核心
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `ManualSigmas`
- `LTXVPreprocess`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `Reroute`
- `RandomNoise`
- `CFGGuider`
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `RandomNoise`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVImgToVideoInplaceKJ`
- `LTXVImgToVideoInplaceKJ`
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `VAEDecode` ★核心
- `CreateVideo`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `SaveVideo`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **88%**（45/51）

**有卡**：`KSamplerSelect`、`ImageResizeKJv2`、`ResizeImagesByLongerEdge`、`ComfyMathExpression`、`CLIPTextEncode`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`ManualSigmas`、`LTXVPreprocess`、`CFGGuider`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`RandomNoise`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`LTXVImgToVideoInplaceKJ`、`VAEDecode`、`CreateVideo`、`easy cleanGpuUsed`、`easy clearCacheAll`、`SaveVideo`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`LoadImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
