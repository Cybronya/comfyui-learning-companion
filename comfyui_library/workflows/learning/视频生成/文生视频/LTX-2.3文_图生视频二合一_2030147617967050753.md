---
key: 视频生成/文生视频/LTX-2.3文_图生视频二合一_2030147617967050753.json
name: LTX-2.3文_图生视频二合一_2030147617967050753
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3文_图生视频二合一_2030147617967050753.json
hash: 258d5ba147589c9b
coverage: 0.865385
learned_at: 2026-10-15 22:44:43
nodes: [RandomNoise, LTXVConcatAVLatent, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVPreprocess, Reroute, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, PrimitiveInt, PrimitiveInt, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LoraLoaderModelOnly, PrimitiveInt, PrimitiveInt, PreviewAny, LTXVConcatAVLatent, KSamplerSelect, RandomNoise, MathExpression|pysssss, MathExpression|pysssss, CreateVideo, ResizeImageMaskNode, ResizeImagesByLongerEdge, LTXVImgToVideoInplace, ManualSigmas, CFGGuider, CLIPTextEncode, LTXVConditioning, MathExpression|pysssss, LTX2_NAG, CLIPTextEncode, PrimitiveStringMultiline, SaveVideo, SaveVideo, Label (rgthree), Label (rgthree), LoadImage, RH_LLMAPI_Pro_Node, PrimitiveBoolean, KSamplerSelect, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, ManualSigmas]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX-2.3文_图生视频二合一_2030147617967050753.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3文_图生视频二合一_2030147617967050753.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `RandomNoise`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `Reroute`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `PreviewAny`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `CreateVideo`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `LTXVImgToVideoInplace`
- `ManualSigmas`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `MathExpression|pysssss`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `SaveVideo`
- `SaveVideo`
- `Label (rgthree)`
- `Label (rgthree)`
- `LoadImage`
- `RH_LLMAPI_Pro_Node`
- `PrimitiveBoolean`
- `KSamplerSelect` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `ManualSigmas`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled.safetensors`

## 知识

覆盖率 **87%**（45/52）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LoraLoaderModelOnly`、`KSamplerSelect`、`MathExpression|pysssss`、`CreateVideo`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`ManualSigmas`、`CLIPTextEncode`、`LTXVConditioning`、`LTX2_NAG`、`SaveVideo`、`Label (rgthree)`、`LoadImage`、`RH_LLMAPI_Pro_Node`、`PrimitiveBoolean`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
