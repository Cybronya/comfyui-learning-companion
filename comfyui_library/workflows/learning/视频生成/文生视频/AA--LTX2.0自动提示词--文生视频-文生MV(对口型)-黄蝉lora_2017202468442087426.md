---
key: 视频生成/文生视频/AA--LTX2.0自动提示词--文生视频-文生MV(对口型)-黄蝉lora_2017202468442087426.json
name: AA--LTX2.0自动提示词--文生视频-文生MV(对口型)-黄蝉lora_2017202468442087426
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/AA--LTX2.0自动提示词--文生视频-文生MV(对口型)-黄蝉lora_2017202468442087426.json
hash: 141af2c9fb6e582c
coverage: 0.714286
learned_at: 2026-10-11 03:07:08
nodes: [LTXVCropGuides, LTXVSeparateAVLatent, KSamplerSelect, LTXAVTextEncoderLoader, LTXVConcatAVLatent, ManualSigmas, KSamplerSelect, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, RandomNoise, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, VAEDecodeTiled, GetImageSize, ImageScaleBy, LTXVConditioning, LatentUpscaleModelLoader, LTXVLatentUpsampler, LTXVScheduler, CreateVideo, SaveVideo, VAEDecode, MarkdownNote, MarkdownNote, Note, LTXVEmptyLatentAudio, CFGGuider, Note, PrimitiveNode, CheckpointLoaderSimple, CFGGuider, SamplerCustomAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, EmptyImage, RandomNoise, LTXVAudioVAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Qwen3_VQA, easy showAnything, JoinStrings, TextInput_, easy showAnything, CLIPTextEncode, JoinStrings, CLIPTextEncode, LoraLoaderModelOnly, PrimitiveInt, PrimitiveFloat, PrimitiveInt, Note, Note, Note, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, MelBandRoFormerModelLoader, SolidMask, LTXVAudioVAEEncode, SetLatentNoiseMask, MelBandRoFormerSampler, LatentUpscaleModelLoader, SetNode, SetNode, SetNode, LTXVSeparateAVLatent, TrimAudioDuration, VAELoaderKJ, LTXVSeparateAVLatent, LTXVLatentUpsampler, ManualSigmas, KSamplerSelect, LTXVConcatAVLatent, SamplerCustomAdvanced, EmptyImage, ImageScaleBy, GetImageSize, EmptyLTXVLatentVideo, LTXVConcatAVLatent, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVConditioning, SetNode, CLIPTextEncode, RandomNoise, KSamplerSelect, LTXVScheduler, CFGGuider, CFGGuider, GetNode, INTConstant, PrimitiveFloat, CM_FloatBinaryOperation, easy showAnything, CM_FloatToInt, CM_FloatBinaryOperation, INTConstant, PathchSageAttentionKJ, Note, DualCLIPLoaderGGUF, VAELoader, SetNode, SetNode, GetNode, VHS_VideoCombine, UnetLoaderGGUF, UNETLoader, LoraLoaderModelOnly, GetNode, LoraLoaderModelOnly, LTXVChunkFeedForward, INTConstant, CM_FloatBinaryOperation, LoadAudio, easy float, easy float, Qwen3_VQA, easy showAnything, JoinStrings, TextInput_, JoinStrings, TextInput_, TextInput_, TextInput_, easy showAnything, CLIPTextEncode, LoraLoaderModelOnly, SetNode, Note, Note, Note, Fast Groups Bypasser (rgthree), TextInput_]
patterns: []
missing: [easy float, easy float]
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/AA--LTX2.0自动提示词--文生视频-文生MV(对口型)-黄蝉lora_2017202468442087426.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/AA--LTX2.0自动提示词--文生视频-文生MV(对口型)-黄蝉lora_2017202468442087426.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（140 个）：
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `GetImageSize`
- `ImageScaleBy`
- `LTXVConditioning`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `LTXVScheduler`
- `CreateVideo`
- `SaveVideo`
- `VAEDecode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `Note`
- `LTXVEmptyLatentAudio` ★核心
- `CFGGuider`
- `Note`
- `PrimitiveNode`
- `CheckpointLoaderSimple` ★核心
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyImage`
- `RandomNoise`
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Qwen3_VQA`
- `easy showAnything`
- `JoinStrings`
- `TextInput_`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `JoinStrings`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveInt`
- `Note`
- `Note`
- `Note`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `MelBandRoFormerModelLoader`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `MelBandRoFormerSampler` ★核心
- `LatentUpscaleModelLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
- `TrimAudioDuration`
- `VAELoaderKJ`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `EmptyImage`
- `ImageScaleBy`
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `SetNode`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `CFGGuider`
- `CFGGuider`
- `GetNode`
- `INTConstant`
- `PrimitiveFloat`
- `CM_FloatBinaryOperation`
- `easy showAnything`
- `CM_FloatToInt`
- `CM_FloatBinaryOperation`
- `INTConstant`
- `PathchSageAttentionKJ`
- `Note`
- `DualCLIPLoaderGGUF`
- `VAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `UnetLoaderGGUF` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LTXVChunkFeedForward`
- `INTConstant`
- `CM_FloatBinaryOperation`
- `LoadAudio`
- `easy float`
- `easy float`
- `Qwen3_VQA`
- `easy showAnything`
- `JoinStrings`
- `TextInput_`
- `JoinStrings`
- `TextInput_`
- `TextInput_`
- `TextInput_`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `Note`
- `Note`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `TextInput_`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **71%**（100/140）

**有卡**：`LTXVCropGuides`、`LTXVSeparateAVLatent`、`KSamplerSelect`、`LTXAVTextEncoderLoader`、`LTXVConcatAVLatent`、`ManualSigmas`、`SamplerCustomAdvanced`、`RandomNoise`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`GetImageSize`、`ImageScaleBy`、`LTXVConditioning`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`LTXVScheduler`、`CreateVideo`、`SaveVideo`、`VAEDecode`、`LTXVEmptyLatentAudio`、`CFGGuider`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`EmptyImage`、`LTXVAudioVAELoader`、`Qwen3_VQA`、`JoinStrings`、`TextInput_`、`CLIPTextEncode`、`MelBandRoFormerModelLoader`、`SolidMask`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`MelBandRoFormerSampler`、`TrimAudioDuration`、`VAELoaderKJ`、`INTConstant`、`CM_FloatBinaryOperation`、`CM_FloatToInt`、`PathchSageAttentionKJ`、`DualCLIPLoaderGGUF`、`VAELoader`、`VHS_VideoCombine`、`UnetLoaderGGUF`、`UNETLoader`、`LTXVChunkFeedForward`、`LoadAudio`

**缺卡**（2）：`easy float`、`easy float`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CFGGuider、KSamplerSelect

## 学习发现

- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
