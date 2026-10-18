---
key: 视频生成/图生视频/LTX 2.3 多图生视频 （V1版 增强人脸一致性，+转场 +VBVR 理解复杂运动，正确物理运动_2049390145010409474.json
name: LTX 2.3 多图生视频 （V1版 增强人脸一致性，+转场 +VBVR 理解复杂运动，正确物理运动_2049390145010409474.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX 2.3 多图生视频 （V1版 增强人脸一致性，+转场 +VBVR 理解复杂运动，正确物理运动_2049390145010409474.json
hash: e617a1865c3aae0c
coverage: 0.698925
learned_at: 2026-10-15 22:37:14
nodes: [Note, LTXVPreprocess, ResizeImagesByLongerEdge, LTXVPreprocess, ResizeImagesByLongerEdge, LTXVCropGuides, LTXVImgToVideoInplace, KSamplerSelect, LTXVEmptyLatentAudio, Note, Note, Note, Note, Note, Note, Note, Note, PrimitiveFloat, Note, ImageResizeKJv2, ComfyMathExpression, easy cleanGpuUsed, Note, easy cleanGpuUsed, LTXVSeparateAVLatent, easy cleanGpuUsed, LTXVAudioVAELoader, CheckpointLoaderSimple, ShowText|pysssss, JoinStrings, MemoryCleaner, easy showAnything, LoraLoaderModelOnly, Note, Note, RandomNoise, Note, ManualSigmas, LTXVConcatAVLatent, LTXVLatentUpsampler, CFGGuider, LoadImage, LoadImage, CM_FloatToInt, CreateVideo, LoraLoaderModelOnly, Note, easy cleanGpuUsed, CR Text, ImageResizeKJv2, ImageStitch, ttN concat, Note, Note, Qwen3_VQA, ComfyMathExpression, INTConstant, INTConstant, easy showAnything, SimpleCalculatorKJ, LoraLoaderModelOnly, SeedGenerator, RandomNoise, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVSeparateAVLatent, SaveVideo, LatentUpscaleModelLoader, Note, Note, Note, Note, LTX2_NAG, SamplerCustomAdvanced, CFGGuider, Note, LTXVChunkFeedForward, LTXAVTextEncoderLoader, CLIPTextEncode, PathchSageAttentionKJ, ModelPatchTorchSettings, easy cleanGpuUsed, LTXVConditioning, Note, EmptyLTXVLatentVideo, Note, PromptRelayEncode, LTXVImgToVideoInplaceKJ, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX 2.3 多图生视频 （V1版 增强人脸一致性，+转场 +VBVR 理解复杂运动，正确物理运动_2049390145010409474.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2049390145010409474.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（93 个）：
- `Note`
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
- `ImageResizeKJv2`
- `ComfyMathExpression`
- `easy cleanGpuUsed`
- `Note`
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `easy cleanGpuUsed`
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `ShowText|pysssss`
- `JoinStrings`
- `MemoryCleaner`
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Note`
- `RandomNoise`
- `Note`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `CFGGuider`
- `LoadImage`
- `LoadImage`
- `CM_FloatToInt`
- `CreateVideo`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `easy cleanGpuUsed`
- `CR Text`
- `ImageResizeKJv2`
- `ImageStitch`
- `ttN concat`
- `Note`
- `Note`
- `Qwen3_VQA`
- `ComfyMathExpression`
- `INTConstant`
- `INTConstant`
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
- `SaveVideo`
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
- `PromptRelayEncode`
- `LTXVImgToVideoInplaceKJ`
- `CR Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **70%**（65/93）

**有卡**：`LTXVPreprocess`、`ResizeImagesByLongerEdge`、`LTXVCropGuides`、`LTXVImgToVideoInplace`、`KSamplerSelect`、`LTXVEmptyLatentAudio`、`ImageResizeKJv2`、`ComfyMathExpression`、`easy cleanGpuUsed`、`LTXVSeparateAVLatent`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`JoinStrings`、`MemoryCleaner`、`LoraLoaderModelOnly`、`RandomNoise`、`ManualSigmas`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`CFGGuider`、`LoadImage`、`CM_FloatToInt`、`CreateVideo`、`CR Text`、`ImageStitch`、`ttN concat`、`Qwen3_VQA`、`INTConstant`、`SimpleCalculatorKJ`、`SeedGenerator`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`SaveVideo`、`LatentUpscaleModelLoader`、`LTX2_NAG`、`LTXVChunkFeedForward`、`LTXAVTextEncoderLoader`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`PromptRelayEncode`、`LTXVImgToVideoInplaceKJ`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
