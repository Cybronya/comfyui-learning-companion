---
key: 视频生成/文生视频/【LTX2.3官方工作流优化】文生视频+图生视频_含提示词扩写模板_2033142799469649922.json
name: 【LTX2.3官方工作流优化】文生视频+图生视频_含提示词扩写模板_2033142799469649922
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【LTX2.3官方工作流优化】文生视频+图生视频_含提示词扩写模板_2033142799469649922.json
hash: 560765a9aa1ab0b2
coverage: 0.767857
learned_at: 2026-10-15 22:47:39
nodes: [RandomNoise, KSamplerSelect, ManualSigmas, CFGGuider, CLIPTextEncode, SamplerCustomAdvanced, LatentUpscaleModelLoader, LoraLoaderModelOnly, LTXVAudioVAELoader, RandomNoise, CFGGuider, KSamplerSelect, LTXVConcatAVLatent, LTXVEmptyLatentAudio, ComfyMathExpression, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, LTXVImgToVideoInplace, LTXVConcatAVLatent, Note, ResizeImageMaskNode, ResizeImagesByLongerEdge, LTXVPreprocess, LTXAVTextEncoderLoader, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, CLIPTextEncode, LTXVConditioning, Reroute, LTXVSeparateAVLatent, LTXVCropGuides, SamplerCustomAdvanced, ManualSigmas, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, MarkdownNote, Note, Note, CheckpointLoaderSimple, PrimitiveBoolean, Note, RH_LLMAPI_Pro_Node, LoadImage, CreateVideo, PlaySound|pysssss, Text, easy showAnything, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, SaveVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/【LTX2.3官方工作流优化】文生视频+图生视频_含提示词扩写模板_2033142799469649922.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/【LTX2.3官方工作流优化】文生视频+图生视频_含提示词扩写模板_2033142799469649922.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `Note`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LTXAVTextEncoderLoader`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `Reroute`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `MarkdownNote`
- `Note`
- `Note`
- `CheckpointLoaderSimple` ★核心
- `PrimitiveBoolean`
- `Note`
- `RH_LLMAPI_Pro_Node`
- `LoadImage`
- `CreateVideo`
- `PlaySound|pysssss`
- `Text`
- `easy showAnything`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `SaveVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **77%**（43/56）

**有卡**：`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`LTXVAudioVAELoader`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LTXAVTextEncoderLoader`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CheckpointLoaderSimple`、`PrimitiveBoolean`、`RH_LLMAPI_Pro_Node`、`LoadImage`、`CreateVideo`、`PlaySound|pysssss`、`Text`、`SaveVideo`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
