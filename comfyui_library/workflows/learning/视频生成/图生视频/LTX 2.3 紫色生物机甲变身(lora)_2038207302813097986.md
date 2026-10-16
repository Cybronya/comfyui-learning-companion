---
key: 视频生成/图生视频/LTX 2.3 紫色生物机甲变身(lora)_2038207302813097986.json
name: LTX 2.3 紫色生物机甲变身(lora)_2038207302813097986.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2038207302813097986.json
hash: 15af4e3eae02cdb2
coverage: 0.833333
learned_at: 2026-10-15 22:36:01
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, LTXVCropGuides, ResizeImagesByLongerEdge, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVPreprocess, ResizeImageMaskNode, KSamplerSelect, Reroute, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVAudioVAEDecode, PrimitiveInt, PrimitiveBoolean, LTXVConcatAVLatent, LTXVEmptyLatentAudio, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, CreateVideo, CLIPTextEncode, VAEDecodeTiled, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, SamplerCustomAdvanced, PrimitiveInt, PrimitiveInt, LayerUtility: PurgeVRAM V2, CFGGuider, MarkdownNote, Note, CLIPTextEncode, LTXVConditioning, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LayerUtility: TextBox, YC_textReplaceNode, LayerUtility: TextBox, PrimitiveInt, LayerUtility: PurgeVRAM V2, LayerUtility: ImageScaleByAspectRatio V2, Int, LayerUtility: PurgeVRAM V2, MarkdownNote, PrimitiveStringMultiline, SaveVideo, Note, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX 2.3 紫色生物机甲变身(lora)_2038207302813097986.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2038207302813097986.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
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
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveInt`
- `PrimitiveBoolean`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
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
- `PrimitiveInt`
- `PrimitiveInt`
- `LayerUtility: PurgeVRAM V2`
- `CFGGuider`
- `MarkdownNote`
- `Note`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: TextBox`
- `YC_textReplaceNode`
- `LayerUtility: TextBox`
- `PrimitiveInt`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `LayerUtility: PurgeVRAM V2`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `SaveVideo`
- `Note`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **83%**（50/60）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`LTXVCropGuides`、`ResizeImagesByLongerEdge`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVPreprocess`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`PrimitiveBoolean`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`CreateVideo`、`CLIPTextEncode`、`VAEDecodeTiled`、`ComfyMathExpression`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`LayerUtility: PurgeVRAM V2`、`LTXVConditioning`、`LoraLoaderModelOnly`、`LayerUtility: TextBox`、`YC_textReplaceNode`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`SaveVideo`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
