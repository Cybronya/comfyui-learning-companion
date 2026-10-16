---
key: 视频生成/图生视频/LTX 2.3 首尾帧视频｜ 丝滑转场｜+转场 LoRA （强化运动连贯性）+VBVR 理解复杂运_2044451540315938817.json
name: LTX 2.3 首尾帧视频｜ 丝滑转场｜+转场 LoRA （强化运动连贯性）+VBVR 理解复杂运_2044451540315938817.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2044451540315938817.json
hash: 314e86860b92540d
coverage: 0.694118
learned_at: 2026-10-15 22:36:38
nodes: [LTXVCropGuides, RandomNoise, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, ResizeImagesByLongerEdge, EmptyLTXVLatentVideo, CFGGuider, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LTXVConcatAVLatent, ManualSigmas, KSamplerSelect, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVAudioVAEDecode, ResizeImagesByLongerEdge, Note, LTXVPreprocess, LTXVPreprocess, VAEDecodeTiled, CreateVideo, Note, Note, Note, Note, easy showAnything, Note, PrimitiveInt, ComfyMathExpression, ImageResizeKJv2, ImageResizeKJv2, Note, Note, Note, Note, Note, Note, MultiplePathsInput, Qwen3_VQA, ImageLoader, RandomNoise, CFGGuider, Note, PrimitiveFloat, PrimitiveFloat, SimpleCalculatorKJ, SimpleCalculatorKJ, SeedGenerator, easy cleanGpuUsed, SamplerCustomAdvanced, ComfyMathExpression, Note, ttN concat, Note, CR Text, easy showAnything, SamplerCustomAdvanced, easy cleanGpuUsed, LTXVSeparateAVLatent, LTX2_NAG, LTXVConditioning, CLIPTextEncode, Note, MemoryCleaner, JoinStrings, ShowText|pysssss, MemoryCleaner, ImageLoader, easy cleanGpuUsed, Note, Note, easy cleanGpuUsed, Note, easy cleanGpuUsed, LTXVAddGuideMulti, UNETLoader, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, LatentUpscaleModelLoader, CLIPTextEncode, LoraLoaderModelOnly, VHS_VideoCombine, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX 2.3 首尾帧视频｜ 丝滑转场｜+转场 LoRA （强化运动连贯性）+VBVR 理解复杂运_2044451540315938817.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044451540315938817.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（85 个）：
- `LTXVCropGuides`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `ResizeImagesByLongerEdge`
- `EmptyLTXVLatentVideo`
- `CFGGuider`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `LTXVAudioVAEDecode` ★核心
- `ResizeImagesByLongerEdge`
- `Note`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `Note`
- `Note`
- `Note`
- `Note`
- `easy showAnything`
- `Note`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `MultiplePathsInput`
- `Qwen3_VQA`
- `ImageLoader`
- `RandomNoise`
- `CFGGuider`
- `Note`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `SimpleCalculatorKJ`
- `SimpleCalculatorKJ`
- `SeedGenerator`
- `easy cleanGpuUsed`
- `SamplerCustomAdvanced` ★核心
- `ComfyMathExpression`
- `Note`
- `ttN concat`
- `Note`
- `CR Text`
- `easy showAnything`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `LTX2_NAG`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `Note`
- `MemoryCleaner`
- `JoinStrings`
- `ShowText|pysssss`
- `MemoryCleaner`
- `ImageLoader`
- `easy cleanGpuUsed`
- `Note`
- `Note`
- `easy cleanGpuUsed`
- `Note`
- `easy cleanGpuUsed`
- `LTXVAddGuideMulti`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `Note`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **69%**（59/85）

**有卡**：`LTXVCropGuides`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`ResizeImagesByLongerEdge`、`EmptyLTXVLatentVideo`、`CFGGuider`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`LTXVPreprocess`、`VAEDecodeTiled`、`CreateVideo`、`ComfyMathExpression`、`ImageResizeKJv2`、`MultiplePathsInput`、`Qwen3_VQA`、`ImageLoader`、`SimpleCalculatorKJ`、`SeedGenerator`、`easy cleanGpuUsed`、`SamplerCustomAdvanced`、`ttN concat`、`CR Text`、`LTX2_NAG`、`LTXVConditioning`、`CLIPTextEncode`、`MemoryCleaner`、`JoinStrings`、`LTXVAddGuideMulti`、`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`VHS_VideoCombine`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、SeedGenerator
