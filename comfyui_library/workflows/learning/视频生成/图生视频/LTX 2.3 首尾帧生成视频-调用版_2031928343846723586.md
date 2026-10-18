---
key: 视频生成/图生视频/LTX 2.3 首尾帧生成视频-调用版_2031928343846723586.json
name: LTX 2.3 首尾帧生成视频-调用版_2031928343846723586.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX 2.3 首尾帧生成视频-调用版_2031928343846723586.json
hash: 69c2c92083654369
coverage: 0.8
learned_at: 2026-10-15 22:35:33
nodes: [LTXVConcatAVLatent, CFGGuider, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVAudioVAEDecode, CLIPTextEncode, LTXVSeparateAVLatent, Note, MarkdownNote, PrimitiveInt, PrimitiveInt, VAEDecodeTiled, LTXVMiddleFrame_TTP, RandomNoise, SamplerCustomAdvanced, LTXVCropGuides, Reroute, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, ResizeImagesByLongerEdge, LTXVPreprocess, ImageResizeKJv2, ResizeImageMaskNode, ResizeImagesByLongerEdge, LTXVEmptyLatentAudio, LTXVPreprocess, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, LTXVFirstLastFrameControl_TTP, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVConcatAVLatent, LayerUtility: PurgeVRAM V2, CreateVideo, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveInt, PrimitiveInt, easy mathInt, RandomNoise, KSamplerSelect, CFGGuider, LTXVConditioning, LoadImage, LoadImage, Int, MarkdownNote, Note, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, ManualSigmas, Note, ManualSigmas, CheckpointLoaderSimple, LoraLoaderModelOnly, LTXVAudioVAELoader, Note, PrimitiveBoolean, LatentUpscaleModelLoader, SaveVideo, PrimitiveStringMultiline, CLIPTextEncode, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX 2.3 首尾帧生成视频-调用版_2031928343846723586.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2031928343846723586.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（65 个）：
- `LTXVConcatAVLatent`
- `CFGGuider`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVSeparateAVLatent`
- `Note`
- `MarkdownNote`
- `PrimitiveInt`
- `PrimitiveInt`
- `VAEDecodeTiled` ★核心
- `LTXVMiddleFrame_TTP`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `Reroute`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect` ★核心
- `LTXAVTextEncoderLoader`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVPreprocess`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVFirstLastFrameControl_TTP`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LayerUtility: PurgeVRAM V2`
- `CreateVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveInt`
- `PrimitiveInt`
- `easy mathInt`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `LTXVConditioning`
- `LoadImage`
- `LoadImage`
- `Int`
- `MarkdownNote`
- `Note`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `ManualSigmas`
- `Note`
- `ManualSigmas`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `Note`
- `PrimitiveBoolean`
- `LatentUpscaleModelLoader`
- `SaveVideo`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **80%**（52/65）

**有卡**：`LTXVConcatAVLatent`、`CFGGuider`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVMiddleFrame_TTP`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`KSamplerSelect`、`LTXAVTextEncoderLoader`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`ImageResizeKJv2`、`ResizeImageMaskNode`、`LTXVEmptyLatentAudio`、`ComfyMathExpression`、`LTXVFirstLastFrameControl_TTP`、`LayerUtility: PurgeVRAM V2`、`CreateVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy mathInt`、`LTXVConditioning`、`LoadImage`、`Int`、`ManualSigmas`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LTXVAudioVAELoader`、`PrimitiveBoolean`、`LatentUpscaleModelLoader`、`SaveVideo`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
