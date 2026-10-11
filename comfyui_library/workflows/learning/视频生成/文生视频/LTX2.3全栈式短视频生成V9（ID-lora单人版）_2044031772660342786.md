---
key: 视频生成/文生视频/LTX2.3全栈式短视频生成V9（ID-lora单人版）_2044031772660342786.json
name: LTX2.3全栈式短视频生成V9（ID-lora单人版）_2044031772660342786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3全栈式短视频生成V9（ID-lora单人版）_2044031772660342786.json
hash: 620c5fa8b4c4956d
coverage: 0.636364
learned_at: 2026-10-11 19:49:38
nodes: [PrimitiveStringMultiline, SetNode, SetNode, easy promptLine, easy convertAnything, RegexExtract, ManualSigmas, ComfyMathExpression, LTXVSeparateAVLatent, ManualSigmas, LTXVConcatAVLatent, LTXVSeparateAVLatent, CFGGuider, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, GetNode, SamplerCustomAdvanced, SamplerCustomAdvanced, CFGGuider, ComfyMathExpression, ComfyMathExpression, LTXVCropGuides, LTXVCropGuides, easy indexAnything, GetNode, LTXVAudioVAEDecode, GetNode, VAEDecodeTiled, TrimVideoLatent, KSamplerSelect, KSamplerSelect, KSamplerSelect, LTXVConcatAVLatent, PrimitiveInt, GetNode, ComfyMathExpression, LTXVLatentUpsampler, LTXVLatentUpsampler, PrimitiveInt, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, CFGGuider, easy forLoopStart, easy forLoopEnd, easy batchAnything, LTXVConditioning, GetNode, LTXVReferenceAudio, INTConstant, INTConstant, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, easy positive, SetNode, easy positive, LongTextToList, GetNode, GetNode, ShowText|pysssss, SetNode, VAELoaderKJ, DualCLIPLoader, VAELoaderKJ, SetNode, LatentUpscaleModelLoader, SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, SetNode, LoraLoaderModelOnly, LoadAudio, RandomNoise, RandomNoise, UNETLoader, RandomNoise, VHS_VideoCombine, INTConstant]
patterns: []
missing: [easy batchAnything, easy convertAnything, easy forLoopEnd, easy forLoopStart, easy indexAnything, easy positive, easy positive, easy promptLine]
parameters: {"batch_size": 1, "height": 25, "width": 97}
discoveries: [次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy indexAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/LTX2.3全栈式短视频生成V9（ID-lora单人版）_2044031772660342786.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3全栈式短视频生成V9（ID-lora单人版）_2044031772660342786.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（88 个）：
- `PrimitiveStringMultiline`
- `SetNode`
- `SetNode`
- `easy promptLine`
- `easy convertAnything`
- `RegexExtract`
- `ManualSigmas`
- `ComfyMathExpression`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVCropGuides`
- `LTXVCropGuides`
- `easy indexAnything`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `VAEDecodeTiled` ★核心
- `TrimVideoLatent`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `PrimitiveInt`
- `GetNode`
- `ComfyMathExpression`
- `LTXVLatentUpsampler` ★核心
- `LTXVLatentUpsampler` ★核心
- `PrimitiveInt`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `CFGGuider`
- `easy forLoopStart`
- `easy forLoopEnd`
- `easy batchAnything`
- `LTXVConditioning`
- `GetNode`
- `LTXVReferenceAudio`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy positive`
- `SetNode`
- `easy positive`
- `LongTextToList`
- `GetNode`
- `GetNode`
- `ShowText|pysssss`
- `SetNode`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `SetNode`
- `LatentUpscaleModelLoader`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoadAudio`
- `RandomNoise`
- `RandomNoise`
- `UNETLoader` ★核心
- `RandomNoise`
- `VHS_VideoCombine`
- `INTConstant`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **64%**（56/88）

**有卡**：`RegexExtract`、`ManualSigmas`、`ComfyMathExpression`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`TrimVideoLatent`、`KSamplerSelect`、`LTXVLatentUpsampler`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`LTXVReferenceAudio`、`INTConstant`、`CLIPTextEncode`、`LongTextToList`、`VAELoaderKJ`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`LoadAudio`、`RandomNoise`、`UNETLoader`、`VHS_VideoCombine`

**缺卡**（8）：`easy batchAnything`、`easy convertAnything`、`easy forLoopEnd`、`easy forLoopStart`、`easy indexAnything`、`easy positive`、`easy positive`、`easy promptLine`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent

## 学习发现

- 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `easy indexAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
