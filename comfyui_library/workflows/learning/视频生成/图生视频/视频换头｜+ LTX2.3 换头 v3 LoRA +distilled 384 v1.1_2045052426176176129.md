---
key: 视频生成/图生视频/视频换头｜+ LTX2.3 换头 v3 LoRA +distilled 384 v1.1_2045052426176176129.json
name: 视频换头｜+ LTX2.3 换头 v3 LoRA +distilled 384 v1.1_2045052426176176129.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/视频换头｜+ LTX2.3 换头 v3 LoRA +distilled 384 v1.1_2045052426176176129.json
hash: 92b86c86acb33493
coverage: 0.654321
learned_at: 2026-10-15 22:36:45
nodes: [PrimitiveFloat, SimpleCalculatorKJ, ImageConcanate, Note, Note, Note, Note, Note, Note, Note, VAEDecode, VHS_VideoCombine, KSamplerSelect, SetLatentNoiseMask, LTXVAudioVAEEncode, LTXVConcatAVLatent, BasicScheduler, LTXVCropGuides, RandomNoise, CFGGuider, GetImageSize, SolidMask, CLIPTextEncode, VAEEncode, ReservedRegionFrameComposer, PrimitiveInt, CLIPTextEncode, ImageResizeKJv2, Note, Qwen3_VQA, Note, Note, Note, ttN concat, CR Text, LTXVSeparateAVLatent, SamplerCustomAdvanced, easy cleanGpuUsed, PrimitiveStringMultiline, CLIPTextEncode, easy cleanGpuUsed, MemoryCleaner, JoinStrings, ShowText|pysssss, easy cleanGpuUsed, MultiplePathsInputPlus, Note, VideoLoaderPlus, LoadImage, Note, easy cleanGpuUsed, LTXVChunkFeedForward, PathchSageAttentionKJ, ModelPatchTorchSettings, easy cleanGpuUsed, LoraLoaderModelOnly, LoraLoaderModelOnly, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, CreateVideo, PrimitiveFloat, SimpleCalculatorKJ, VHS_LoadVideo, LoadAudio, Note, LTXVConditioning, LTX2_NAG, TrimAudioDuration, Note, Note, Note, Note, Note, Note, Note, SaveVideo, VHS_VideoCombine, easy showAnything, LTXVAddGuideMulti, Note]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev.safetensors"}
---

# 视频生成/图生视频/视频换头｜+ LTX2.3 换头 v3 LoRA +distilled 384 v1.1_2045052426176176129.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2045052426176176129.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（81 个）：
- `PrimitiveFloat`
- `SimpleCalculatorKJ`
- `ImageConcanate`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `KSamplerSelect` ★核心
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `LTXVConcatAVLatent`
- `BasicScheduler`
- `LTXVCropGuides`
- `RandomNoise`
- `CFGGuider`
- `GetImageSize`
- `SolidMask`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `ReservedRegionFrameComposer`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `Note`
- `Qwen3_VQA`
- `Note`
- `Note`
- `Note`
- `ttN concat`
- `CR Text`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `MemoryCleaner`
- `JoinStrings`
- `ShowText|pysssss`
- `easy cleanGpuUsed`
- `MultiplePathsInputPlus`
- `Note`
- `VideoLoaderPlus`
- `LoadImage`
- `Note`
- `easy cleanGpuUsed`
- `LTXVChunkFeedForward`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `CreateVideo`
- `PrimitiveFloat`
- `SimpleCalculatorKJ`
- `VHS_LoadVideo`
- `LoadAudio`
- `Note`
- `LTXVConditioning`
- `LTX2_NAG`
- `TrimAudioDuration`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `SaveVideo`
- `VHS_VideoCombine`
- `easy showAnything`
- `LTXVAddGuideMulti`
- `Note`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **65%**（53/81）

**有卡**：`SimpleCalculatorKJ`、`ImageConcanate`、`VAEDecode`、`VHS_VideoCombine`、`KSamplerSelect`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`LTXVConcatAVLatent`、`BasicScheduler`、`LTXVCropGuides`、`RandomNoise`、`CFGGuider`、`GetImageSize`、`SolidMask`、`CLIPTextEncode`、`VAEEncode`、`ReservedRegionFrameComposer`、`ImageResizeKJv2`、`Qwen3_VQA`、`ttN concat`、`CR Text`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`easy cleanGpuUsed`、`MemoryCleaner`、`JoinStrings`、`MultiplePathsInputPlus`、`VideoLoaderPlus`、`LoadImage`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`CreateVideo`、`VHS_LoadVideo`、`LoadAudio`、`LTXVConditioning`、`LTX2_NAG`、`TrimAudioDuration`、`SaveVideo`、`LTXVAddGuideMulti`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
