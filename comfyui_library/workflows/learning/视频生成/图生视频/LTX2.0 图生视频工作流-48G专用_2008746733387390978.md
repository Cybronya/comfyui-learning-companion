---
key: 视频生成/图生视频/LTX2.0 图生视频工作流-48G专用_2008746733387390978.json
name: LTX2.0 图生视频工作流-48G专用_2008746733387390978.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2008746733387390978.json
hash: b00b1e69243182ac
coverage: 0.907407
learned_at: 2026-10-15 22:34:08
nodes: [MarkdownNote, KSamplerSelect, LTXVScheduler, KSamplerSelect, ManualSigmas, LatentUpscaleModelLoader, CFGGuider, LTXVEmptyLatentAudio, CLIPTextEncode, RandomNoise, SamplerCustomAdvanced, LTXVLatentUpsampler, CFGGuider, LoraLoaderModelOnly, LTXVConcatAVLatent, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, CLIPTextEncode, RandomNoise, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, SamplerCustomAdvanced, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVPreprocess, LTXVSeparateAVLatent, VAEDecode, LTXVSeparateAVLatent, LTXVCropGuides, VAEDecode, EmptyImage, GetImageSize, ImageScaleBy, ResizeImagesByLongerEdge, GetImageSize, PrimitiveInt, LTXVConditioning, MarkdownNote, LoadImage, MathExpression|pysssss, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, MarkdownNote, JWInteger, LTXVAudioVAEDecode, LTXVAudioVAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, CR Text, VHS_VideoCombine, VHS_VideoCombine, RH_LLMAPI_NODE, easy showAnything]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.0 图生视频工作流-48G专用_2008746733387390978.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2008746733387390978.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（54 个）：
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LatentUpscaleModelLoader`
- `CFGGuider`
- `LTXVEmptyLatentAudio` ★核心
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `CFGGuider`
- `LoraLoaderModelOnly` ★核心
- `LTXVConcatAVLatent`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `VAEDecode` ★核心
- `EmptyImage`
- `GetImageSize`
- `ImageScaleBy`
- `ResizeImagesByLongerEdge`
- `GetImageSize`
- `PrimitiveInt`
- `LTXVConditioning`
- `MarkdownNote`
- `LoadImage`
- `MathExpression|pysssss`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MarkdownNote`
- `JWInteger`
- `LTXVAudioVAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `RH_LLMAPI_NODE`
- `easy showAnything`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **91%**（49/54）

**有卡**：`KSamplerSelect`、`LTXVScheduler`、`ManualSigmas`、`LatentUpscaleModelLoader`、`CFGGuider`、`LTXVEmptyLatentAudio`、`CLIPTextEncode`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`LoraLoaderModelOnly`、`LTXVConcatAVLatent`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LTXVPreprocess`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVCropGuides`、`EmptyImage`、`GetImageSize`、`ImageScaleBy`、`ResizeImagesByLongerEdge`、`LTXVConditioning`、`LoadImage`、`MathExpression|pysssss`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVAudioVAEDecode`、`CR Text`、`VHS_VideoCombine`、`RH_LLMAPI_NODE`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
