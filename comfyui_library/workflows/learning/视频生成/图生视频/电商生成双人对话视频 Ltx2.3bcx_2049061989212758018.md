---
key: 视频生成/图生视频/电商生成双人对话视频 Ltx2.3bcx_2049061989212758018.json
name: 电商生成双人对话视频 Ltx2.3bcx_2049061989212758018.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2049061989212758018.json
hash: 6c71ff20c4fc3517
coverage: 0.930556
learned_at: 2026-10-15 22:37:13
nodes: [easy cleanGpuUsed, VRAMReserver, PathchSageAttentionKJ, PromptRelayEncode, CLIPTextEncode, LTX2_NAG, LTXVConditioning, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, PrimitiveBoolean, LTXVConcatAVLatent, LTXAVTextEncoderLoader, SamplerCustomAdvanced, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, LTXVImgToVideoConditionOnly, RandomNoise, KSamplerSelect, LTXVConcatAVLatent, CFGGuider, ManualSigmas, LTXVImgToVideoConditionOnly, SamplerCustomAdvanced, CheckpointLoaderSimple, LTXVAudioVAEDecode, ImageFromBatch, LTXVImgToVideoConditionOnly, LTXVSeparateAVLatent, LTXVAudioVAELoader, Seed Everywhere, LTXVSeparateAVLatent, LTXVPreprocess, LoraLoaderModelOnly, LoraLoaderModelOnly, CreateVideo, LatentUpscaleModelLoader, LoraLoaderModelOnly, TrimAudioDuration, MathExpression|pysssss, SetLatentNoiseMask, LTXVLatentUpsampler, GetLatentSizeAndCount, SetLatentNoiseMask, SolidMask, LTXVLatentUpsampler, GetLatentSizeAndCount, SamplerCustomAdvanced, SolidMask, SetLatentNoiseMask, LTXVSeparateAVLatent, LTXVAudioVAEEncode, VAEDecodeTiled, image_scale_pixel_v2, EmptyLTXVLatentVideo, SolidMask, Image_Resize_longsize, CM_IntToFloat, Int, SaveVideo, LoadAudio, JjkText, JjkText, LoadImage, Note, Note, MathExpression|pysssss, Note]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors"}
---

# 视频生成/图生视频/电商生成双人对话视频 Ltx2.3bcx_2049061989212758018.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2049061989212758018.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
- `easy cleanGpuUsed`
- `VRAMReserver`
- `PathchSageAttentionKJ`
- `PromptRelayEncode`
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `LTXVConditioning`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `PrimitiveBoolean`
- `LTXVConcatAVLatent`
- `LTXAVTextEncoderLoader`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoConditionOnly`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `CFGGuider`
- `ManualSigmas`
- `LTXVImgToVideoConditionOnly`
- `SamplerCustomAdvanced` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAEDecode` ★核心
- `ImageFromBatch`
- `LTXVImgToVideoConditionOnly`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAELoader`
- `Seed Everywhere`
- `LTXVSeparateAVLatent`
- `LTXVPreprocess`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CreateVideo`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `TrimAudioDuration`
- `MathExpression|pysssss`
- `SetLatentNoiseMask`
- `LTXVLatentUpsampler` ★核心
- `GetLatentSizeAndCount`
- `SetLatentNoiseMask`
- `SolidMask`
- `LTXVLatentUpsampler` ★核心
- `GetLatentSizeAndCount`
- `SamplerCustomAdvanced` ★核心
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEEncode` ★核心
- `VAEDecodeTiled` ★核心
- `image_scale_pixel_v2`
- `EmptyLTXVLatentVideo`
- `SolidMask`
- `Image_Resize_longsize`
- `CM_IntToFloat`
- `Int`
- `SaveVideo`
- `LoadAudio`
- `JjkText`
- `JjkText`
- `LoadImage`
- `Note`
- `Note`
- `MathExpression|pysssss`
- `Note`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **93%**（67/72）

**有卡**：`easy cleanGpuUsed`、`VRAMReserver`、`PathchSageAttentionKJ`、`PromptRelayEncode`、`CLIPTextEncode`、`LTX2_NAG`、`LTXVConditioning`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`PrimitiveBoolean`、`LTXVConcatAVLatent`、`LTXAVTextEncoderLoader`、`SamplerCustomAdvanced`、`LTXVImgToVideoConditionOnly`、`CheckpointLoaderSimple`、`LTXVAudioVAEDecode`、`ImageFromBatch`、`LTXVSeparateAVLatent`、`LTXVAudioVAELoader`、`Seed Everywhere`、`LTXVPreprocess`、`LoraLoaderModelOnly`、`CreateVideo`、`LatentUpscaleModelLoader`、`TrimAudioDuration`、`MathExpression|pysssss`、`SetLatentNoiseMask`、`LTXVLatentUpsampler`、`GetLatentSizeAndCount`、`SolidMask`、`LTXVAudioVAEEncode`、`VAEDecodeTiled`、`image_scale_pixel_v2`、`EmptyLTXVLatentVideo`、`Image_Resize_longsize`、`CM_IntToFloat`、`Int`、`SaveVideo`、`LoadAudio`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
