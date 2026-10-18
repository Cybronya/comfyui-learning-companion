---
key: 视频生成/图生视频/音画同处LTX2.0！【又快又好】_2015590078243938306.json
name: 音画同处LTX2.0！【又快又好】_2015590078243938306.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/音画同处LTX2.0！【又快又好】_2015590078243938306.json
hash: e361bdedb7df48e5
coverage: 0.88
learned_at: 2026-10-15 22:34:39
nodes: [KSamplerSelect, LTXVScheduler, LTXAVTextEncoderLoader, KSamplerSelect, ManualSigmas, LatentUpscaleModelLoader, LTXVCropGuides, CFGGuider, LTXVEmptyLatentAudio, LTXVConditioning, CLIPTextEncode, EmptyImage, SamplerCustomAdvanced, RandomNoise, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVLatentUpsampler, ImageScaleBy, PrimitiveNode, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVImgToVideoInplace, CFGGuider, LoraLoaderModelOnly, LoraLoaderModelOnly, CheckpointLoaderSimple, LoraLoaderModelOnly, LTXVSeparateAVLatent, VAEDecode, CreateVideo, RandomNoise, SamplerCustomAdvanced, SaveVideo, LTXVPreprocess, GetImageSize, GetImageSize, ResizeImagesByLongerEdge, PrimitiveInt, SimpleMath+, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, ImageResizeKJv2, LoadImage, ImpactInt, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/音画同处LTX2.0！【又快又好】_2015590078243938306.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2015590078243938306.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `LTXAVTextEncoderLoader`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LatentUpscaleModelLoader`
- `LTXVCropGuides`
- `CFGGuider`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `EmptyImage`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `ImageScaleBy`
- `PrimitiveNode`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `CreateVideo`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `SaveVideo`
- `LTXVPreprocess`
- `GetImageSize`
- `GetImageSize`
- `ResizeImagesByLongerEdge`
- `PrimitiveInt`
- `SimpleMath+`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `ImageResizeKJv2`
- `LoadImage`
- `ImpactInt`
- `CLIPTextEncode` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **88%**（44/50）

**有卡**：`KSamplerSelect`、`LTXVScheduler`、`LTXAVTextEncoderLoader`、`ManualSigmas`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`CFGGuider`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`CLIPTextEncode`、`EmptyImage`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LTXVAudioVAELoader`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`ImageScaleBy`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`VAEDecode`、`CreateVideo`、`SaveVideo`、`LTXVPreprocess`、`GetImageSize`、`ResizeImagesByLongerEdge`、`SimpleMath+`、`ImageResizeKJv2`、`LoadImage`、`ImpactInt`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
