---
key: 视频生成/图生视频/LTX 2.3 首尾帧视频 一致性+转场+VBVR复杂运动_2052747841218596866.json
name: LTX 2.3 首尾帧视频 一致性+转场+VBVR复杂运动_2052747841218596866.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2052747841218596866.json
hash: c9bdf7b27a8bdd16
coverage: 0.698925
learned_at: 2026-10-15 22:37:32
nodes: [LTXVPreprocess, ResizeImagesByLongerEdge, LTXVPreprocess, ResizeImagesByLongerEdge, LTXVCropGuides, LTXVImgToVideoInplace, KSamplerSelect, LTXVEmptyLatentAudio, Note, Note, Note, Note, Note, Note, Note, Note, PrimitiveFloat, Note, ComfyMathExpression, easy cleanGpuUsed, Note, easy cleanGpuUsed, LTXVSeparateAVLatent, easy cleanGpuUsed, LTXVAudioVAELoader, CheckpointLoaderSimple, ShowText|pysssss, LoraLoaderModelOnly, Note, Note, RandomNoise, Note, ManualSigmas, LTXVConcatAVLatent, LTXVLatentUpsampler, CFGGuider, CM_FloatToInt, CreateVideo, LoraLoaderModelOnly, Note, easy cleanGpuUsed, CR Text, ImageResizeKJv2, ImageStitch, Note, Note, ComfyMathExpression, easy showAnything, SimpleCalculatorKJ, LoraLoaderModelOnly, SeedGenerator, RandomNoise, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVSeparateAVLatent, LatentUpscaleModelLoader, Note, Note, Note, Note, LTX2_NAG, SamplerCustomAdvanced, CFGGuider, Note, LTXVChunkFeedForward, LTXAVTextEncoderLoader, CLIPTextEncode, PathchSageAttentionKJ, ModelPatchTorchSettings, easy cleanGpuUsed, LTXVConditioning, Note, EmptyLTXVLatentVideo, Note, LTXVImgToVideoInplaceKJ, SaveVideo, easy showAnything, JoinStrings, MemoryCleaner, ttN concat, Qwen3_VQA, Note, LoadImage, INTConstant, INTConstant, PromptRelayEncode, CR Text, ImageResizeKJv2, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX 2.3 首尾帧视频 一致性+转场+VBVR复杂运动_2052747841218596866.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2052747841218596866.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（93 个）：
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `KSamplerSelect` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `PrimitiveFloat`
- `Note`
- `ComfyMathExpression`
- `easy cleanGpuUsed`
- `Note`
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `easy cleanGpuUsed`
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `ShowText|pysssss`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Note`
- `RandomNoise`
- `Note`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `CFGGuider`
- `CM_FloatToInt`
- `CreateVideo`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `easy cleanGpuUsed`
- `CR Text`
- `ImageResizeKJv2`
- `ImageStitch`
- `Note`
- `Note`
- `ComfyMathExpression`
- `easy showAnything`
- `SimpleCalculatorKJ`
- `LoraLoaderModelOnly` ★核心
- `SeedGenerator`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `Note`
- `Note`
- `Note`
- `Note`
- `LTX2_NAG`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `Note`
- `LTXVChunkFeedForward`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `easy cleanGpuUsed`
- `LTXVConditioning`
- `Note`
- `EmptyLTXVLatentVideo`
- `Note`
- `LTXVImgToVideoInplaceKJ`
- `SaveVideo`
- `easy showAnything`
- `JoinStrings`
- `MemoryCleaner`
- `ttN concat`
- `Qwen3_VQA`
- `Note`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `PromptRelayEncode`
- `CR Text`
- `ImageResizeKJv2`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **70%**（65/93）

**有卡**：`LTXVPreprocess`、`ResizeImagesByLongerEdge`、`LTXVCropGuides`、`LTXVImgToVideoInplace`、`KSamplerSelect`、`LTXVEmptyLatentAudio`、`ComfyMathExpression`、`easy cleanGpuUsed`、`LTXVSeparateAVLatent`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`RandomNoise`、`ManualSigmas`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`CFGGuider`、`CM_FloatToInt`、`CreateVideo`、`CR Text`、`ImageResizeKJv2`、`ImageStitch`、`SimpleCalculatorKJ`、`SeedGenerator`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LatentUpscaleModelLoader`、`LTX2_NAG`、`LTXVChunkFeedForward`、`LTXAVTextEncoderLoader`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplaceKJ`、`SaveVideo`、`JoinStrings`、`MemoryCleaner`、`ttN concat`、`Qwen3_VQA`、`LoadImage`、`INTConstant`、`PromptRelayEncode`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
