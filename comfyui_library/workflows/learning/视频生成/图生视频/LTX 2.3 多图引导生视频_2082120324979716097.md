---
key: 视频生成/图生视频/LTX 2.3 多图引导生视频_2082120324979716097.json
name: LTX 2.3 多图引导生视频_2082120324979716097.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2082120324979716097.json
hash: 19641718d47cfd61
coverage: 0.824324
learned_at: 2026-10-15 22:42:27
nodes: [LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, KSamplerSelect, Reroute, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, PrimitiveInt, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, CreateVideo, CLIPTextEncode, VAEDecodeTiled, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, SamplerCustomAdvanced, LayerUtility: PurgeVRAM V2, PrimitiveInt, PrimitiveInt, LayerUtility: PurgeVRAM V2, CFGGuider, MarkdownNote, PrimitiveInt, MathExpression|pysssss, Reroute, PrimitiveBoolean, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, RandomNoise, RandomNoise, Int, LTXVEmptyLatentAudio, LTXVConditioning, LTXVConcatAVLatent, ResizeImageMaskNode, ResizeImagesByLongerEdge, LTXVPreprocess, ResizeImageMaskNode, ResizeImagesByLongerEdge, LTXVPreprocess, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, Float, Note, ResizeImageMaskNode, ResizeImagesByLongerEdge, LTXVPreprocess, ResizeImageMaskNode, ResizeImagesByLongerEdge, LTXVPreprocess, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, LTXVAddGuideMulti, MarkdownNote, SaveVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX 2.3 多图引导生视频_2082120324979716097.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2082120324979716097.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（74 个）：
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `KSamplerSelect` ★核心
- `Reroute`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveInt`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CreateVideo`
- `CLIPTextEncode` ★核心
- `VAEDecodeTiled` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `SamplerCustomAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `PrimitiveInt`
- `PrimitiveInt`
- `LayerUtility: PurgeVRAM V2`
- `CFGGuider`
- `MarkdownNote`
- `PrimitiveInt`
- `MathExpression|pysssss`
- `Reroute`
- `PrimitiveBoolean`
- `Note`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `RandomNoise`
- `Int`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly` ★核心
- `Float`
- `Note`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `LTXVAddGuideMulti`
- `MarkdownNote`
- `SaveVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（61/74）

**有卡**：`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`CreateVideo`、`CLIPTextEncode`、`VAEDecodeTiled`、`ComfyMathExpression`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`LayerUtility: PurgeVRAM V2`、`MathExpression|pysssss`、`PrimitiveBoolean`、`LayerUtility: ImageScaleByAspectRatio V2`、`RandomNoise`、`Int`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LoraLoaderModelOnly`、`Float`、`LoadImage`、`LTXVAddGuideMulti`、`SaveVideo`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
