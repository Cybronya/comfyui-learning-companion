---
key: 视频生成/图生视频/LTX 2.3 变身特效（亦诚视觉原创）_2041734587340038146.json
name: LTX 2.3 变身特效（亦诚视觉原创）_2041734587340038146.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX 2.3 变身特效（亦诚视觉原创）_2041734587340038146.json
hash: a1dbb8ca6f162575
coverage: 0.862069
learned_at: 2026-10-15 22:36:21
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, LTXVCropGuides, ResizeImagesByLongerEdge, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVPreprocess, ResizeImageMaskNode, KSamplerSelect, Reroute, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, PrimitiveInt, PrimitiveBoolean, LTXVConcatAVLatent, LTXVEmptyLatentAudio, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, SamplerCustomAdvanced, PrimitiveInt, PrimitiveInt, LayerUtility: PurgeVRAM V2, CFGGuider, LTXVConditioning, PrimitiveInt, Note, CheckpointLoaderSimple, CreateVideo, VAEDecodeTiled, LTXVAudioVAEDecode, LayerUtility: PurgeVRAM V2, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveVideo, CLIPTextEncode, CLIPTextEncode, Note, YC_textReplaceNode, PrimitiveStringMultiline, Int, LoadImage, LayerUtility: TextBox, LayerUtility: TextBox]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX 2.3 变身特效（亦诚视觉原创）_2041734587340038146.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041734587340038146.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `LTXVCropGuides`
- `ResizeImagesByLongerEdge`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `ResizeImageMaskNode`
- `KSamplerSelect` ★核心
- `Reroute`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `LayerUtility: PurgeVRAM V2`
- `CFGGuider`
- `LTXVConditioning`
- `PrimitiveInt`
- `Note`
- `CheckpointLoaderSimple` ★核心
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `YC_textReplaceNode`
- `PrimitiveStringMultiline`
- `Int`
- `LoadImage`
- `LayerUtility: TextBox`
- `LayerUtility: TextBox`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-fp8.safetensors`

## 知识

覆盖率 **86%**（50/58）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`LTXVCropGuides`、`ResizeImagesByLongerEdge`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVPreprocess`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`、`PrimitiveBoolean`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`LayerUtility: PurgeVRAM V2`、`LTXVConditioning`、`CheckpointLoaderSimple`、`CreateVideo`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoaderModelOnly`、`SaveVideo`、`CLIPTextEncode`、`YC_textReplaceNode`、`Int`、`LoadImage`、`LayerUtility: TextBox`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
