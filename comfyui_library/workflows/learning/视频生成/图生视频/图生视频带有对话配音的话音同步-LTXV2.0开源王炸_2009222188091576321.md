---
key: 视频生成/图生视频/图生视频带有对话配音的话音同步-LTXV2.0开源王炸_2009222188091576321.json
name: 图生视频带有对话配音的话音同步-LTXV2.0开源王炸_2009222188091576321.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2009222188091576321.json
hash: 14828ac33d67fbc4
coverage: 0.754098
learned_at: 2026-10-15 22:34:11
nodes: [CFGGuider, LTXVEmptyLatentAudio, LatentUpscaleModelLoader, CFGGuider, RandomNoise, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, MemoryCleaner, CLIPTextEncode, Reroute, LoraLoaderModelOnly, LoraLoaderModelOnly, Reroute, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXVConditioning, KSamplerSelect, LTXVScheduler, ManualSigmas, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXVLatentUpsampler, RandomNoise, Reroute, LTXAVTextEncoderLoader, MarkdownNote, MarkdownNote, LTXVAudioVAEDecode, CLIPTextEncode, GetNode, LTXVCropGuides, MemoryCleaner, EmptyLTXVLatentVideo, MarkdownNote, SimpleMath+, MarkdownNote, PrimitiveInt, Reroute, Int, PrimitiveFloat, Reroute, Reroute, PrimitiveInt, EmptyImage, ImageScaleBy, GetImageSize, ResizeImagesByLongerEdge, LTXVPreprocess, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Int, LTXVImgToVideoInplace, LTXVConcatAVLatent, SamplerCustomAdvanced, VHS_VideoCombine, SetNode, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/图生视频带有对话配音的话音同步-LTXV2.0开源王炸_2009222188091576321.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2009222188091576321.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（61 个）：
- `CFGGuider`
- `LTXVEmptyLatentAudio` ★核心
- `LatentUpscaleModelLoader`
- `CFGGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `MemoryCleaner`
- `CLIPTextEncode` ★核心
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXVLatentUpsampler` ★核心
- `RandomNoise`
- `Reroute`
- `LTXAVTextEncoderLoader`
- `MarkdownNote`
- `MarkdownNote`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `LTXVCropGuides`
- `MemoryCleaner`
- `EmptyLTXVLatentVideo`
- `MarkdownNote`
- `SimpleMath+`
- `MarkdownNote`
- `PrimitiveInt`
- `Reroute`
- `Int`
- `PrimitiveFloat`
- `Reroute`
- `Reroute`
- `PrimitiveInt`
- `EmptyImage`
- `ImageScaleBy`
- `GetImageSize`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Int`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `SetNode`
- `CR Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **75%**（46/61）

**有卡**：`CFGGuider`、`LTXVEmptyLatentAudio`、`LatentUpscaleModelLoader`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`MemoryCleaner`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`LTXVConditioning`、`KSamplerSelect`、`LTXVScheduler`、`ManualSigmas`、`LTXVConcatAVLatent`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXVLatentUpsampler`、`LTXAVTextEncoderLoader`、`LTXVAudioVAEDecode`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`SimpleMath+`、`Int`、`EmptyImage`、`ImageScaleBy`、`GetImageSize`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`LTXVImgToVideoInplace`、`VHS_VideoCombine`、`CR Text`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
