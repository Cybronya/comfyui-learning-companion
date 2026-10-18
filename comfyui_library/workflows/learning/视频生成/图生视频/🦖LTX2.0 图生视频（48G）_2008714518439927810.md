---
key: 视频生成/图生视频/🦖LTX2.0 图生视频（48G）_2008714518439927810.json
name: 🦖LTX2.0 图生视频（48G）_2008714518439927810.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/🦖LTX2.0 图生视频（48G）_2008714518439927810.json
hash: d1ce4d84a5ddac58
coverage: 0.90566
learned_at: 2026-10-15 22:34:08
nodes: [KSamplerSelect, LTXVScheduler, KSamplerSelect, ManualSigmas, LatentUpscaleModelLoader, LTXVCropGuides, CFGGuider, LTXVEmptyLatentAudio, LTXVConditioning, CLIPTextEncode, RandomNoise, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVLatentUpsampler, ImageScaleBy, GetImageSize, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, CFGGuider, MarkdownNote, LTXVPreprocess, LoraLoaderModelOnly, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVConcatAVLatent, MarkdownNote, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, EmptyImage, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, VAEDecode, SamplerCustomAdvanced, LTXVAudioVAEDecode, LTXVSeparateAVLatent, VHS_VideoCombine, VAEDecode, LTXVAudioVAEDecode, VHS_VideoCombine, RandomNoise, ResizeImagesByLongerEdge, ImageResizeKJv2, GetImageSize, ResizeLongestToNode, GetImageSize, LoadImage, CLIPTextEncode, MarkdownNote, MathExpression|pysssss, PrimitiveInt, JWInteger]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/🦖LTX2.0 图生视频（48G）_2008714518439927810.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2008714518439927810.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（53 个）：
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LatentUpscaleModelLoader`
- `LTXVCropGuides`
- `CFGGuider`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `ImageScaleBy`
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `MarkdownNote`
- `LTXVPreprocess`
- `LoraLoaderModelOnly` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVConcatAVLatent`
- `MarkdownNote`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `EmptyImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `ImageResizeKJv2`
- `GetImageSize`
- `ResizeLongestToNode`
- `GetImageSize`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `MathExpression|pysssss`
- `PrimitiveInt`
- `JWInteger`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **91%**（48/53）

**有卡**：`KSamplerSelect`、`LTXVScheduler`、`ManualSigmas`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`CFGGuider`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`CLIPTextEncode`、`RandomNoise`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`ImageScaleBy`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LTXVPreprocess`、`LoraLoaderModelOnly`、`LTXVConcatAVLatent`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`EmptyImage`、`VAEDecode`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`ResizeImagesByLongerEdge`、`ImageResizeKJv2`、`ResizeLongestToNode`、`LoadImage`、`MathExpression|pysssss`、`JWInteger`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
