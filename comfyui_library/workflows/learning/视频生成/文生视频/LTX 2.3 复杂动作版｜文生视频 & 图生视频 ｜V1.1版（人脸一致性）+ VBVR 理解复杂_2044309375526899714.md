---
key: 视频生成/文生视频/LTX 2.3 复杂动作版｜文生视频 & 图生视频 ｜V1.1版（人脸一致性）+ VBVR 理解复杂_2044309375526899714.json
name: LTX 2.3 复杂动作版｜文生视频 & 图生视频 ｜V1.1版（人脸一致性）+ VBVR 理解复杂_2044309375526899714
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX 2.3 复杂动作版｜文生视频 & 图生视频 ｜V1.1版（人脸一致性）+ VBVR 理解复杂_2044309375526899714.json
hash: 5adf3ee1620b9697
coverage: 0.725
learned_at: 2026-10-15 22:44:32
nodes: [CLIPTextEncode, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, ManualSigmas, KSamplerSelect, CFGGuider, Note, Qwen3_VQA, easy showAnything, Note, ShowText|pysssss, JoinStrings, Note, Note, Note, ComfyMathExpression, Note, SimpleCalculatorKJ, CM_FloatToInt, LTX2_NAG, ComfyMathExpression, LTXVChunkFeedForward, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveFloat, easy cleanGpuUsed, easy cleanGpuUsed, LTXVSeparateAVLatent, Note, MemoryCleaner, easy cleanGpuUsed, PrimitiveFloat, INTConstant, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, ResizeImagesByLongerEdge, LTXVPreprocess, ImageResizeKJv2, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVConcatAVLatent, LTXVEmptyLatentAudio, VAEDecodeTiled, Note, Note, RandomNoise, easy cleanGpuUsed, Note, Note, Note, Note, PrimitiveBoolean, LTXVImgToVideoConditionOnly, LTXVImgToVideoConditionOnly, LTXVConditioning, easy cleanGpuUsed, SamplerCustomAdvanced, SamplerCustomAdvanced, Note, Note, Note, CR Text, ttN concat, Note, MemoryCleaner, Note, SeedGenerator, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, ImageLoader, VHS_VideoCombine, easy imageSize]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX 2.3 复杂动作版｜文生视频 & 图生视频 ｜V1.1版（人脸一致性）+ VBVR 理解复杂_2044309375526899714.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX 2.3 复杂动作版｜文生视频 & 图生视频 ｜V1.1版（人脸一致性）+ VBVR 理解复杂_2044309375526899714.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（80 个）：
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `Note`
- `Qwen3_VQA`
- `easy showAnything`
- `Note`
- `ShowText|pysssss`
- `JoinStrings`
- `Note`
- `Note`
- `Note`
- `ComfyMathExpression`
- `Note`
- `SimpleCalculatorKJ`
- `CM_FloatToInt`
- `LTX2_NAG`
- `ComfyMathExpression`
- `LTXVChunkFeedForward`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `Note`
- `MemoryCleaner`
- `easy cleanGpuUsed`
- `PrimitiveFloat`
- `INTConstant`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode` ★核心
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `VAEDecodeTiled` ★核心
- `Note`
- `Note`
- `RandomNoise`
- `easy cleanGpuUsed`
- `Note`
- `Note`
- `Note`
- `Note`
- `PrimitiveBoolean`
- `LTXVImgToVideoConditionOnly`
- `LTXVImgToVideoConditionOnly`
- `LTXVConditioning`
- `easy cleanGpuUsed`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `Note`
- `Note`
- `Note`
- `CR Text`
- `ttN concat`
- `Note`
- `MemoryCleaner`
- `Note`
- `SeedGenerator`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `ImageLoader`
- `VHS_VideoCombine`
- `easy imageSize`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **72%**（58/80）

**有卡**：`CLIPTextEncode`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`Qwen3_VQA`、`JoinStrings`、`ComfyMathExpression`、`SimpleCalculatorKJ`、`CM_FloatToInt`、`LTX2_NAG`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`easy cleanGpuUsed`、`LTXVSeparateAVLatent`、`MemoryCleaner`、`INTConstant`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`ImageResizeKJv2`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`LTXVEmptyLatentAudio`、`VAEDecodeTiled`、`PrimitiveBoolean`、`LTXVImgToVideoConditionOnly`、`LTXVConditioning`、`SamplerCustomAdvanced`、`CR Text`、`ttN concat`、`SeedGenerator`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`ImageLoader`、`VHS_VideoCombine`、`easy imageSize`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、SeedGenerator
