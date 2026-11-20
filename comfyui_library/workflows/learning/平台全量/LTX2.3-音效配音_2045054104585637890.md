---
key: 平台全量/LTX2.3-音效配音_2045054104585637890.json
name: LTX2.3-音效配音_2045054104585637890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.3-音效配音_2045054104585637890.json
hash: af2cc2a8de382d8c
coverage: 0.857143
learned_at: 2026-11-14 00:38:19
nodes: [MarkdownNote, PrimitiveInt, PrimitiveFloat, CLIPTextEncode, ModelPatchTorchSettings, PathchSageAttentionKJ, LTXVConcatAVLatent, SamplerCustomAdvanced, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, CLIPTextEncode, LTXVSeparateAVLatent, LTXVChunkFeedForward, LTXVConditioning, LTXVAudioVideoMask, LTXVEmptyLatentAudio, PrimitiveInt, MathExpression|pysssss, LTXVPreprocess, VAEEncode, LTXVAudioVAEDecode, VHS_VideoInfo, GetImageRangeFromBatch, CreateVideo, VAELoaderKJ, DualCLIPLoader, RH_LLMAPI_Pro_Node, VAELoaderKJ, easy showAnything, VHS_VideoCombine, LoraLoaderModelOnly, UNETLoader, VHS_LoadVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/LTX2.3-音效配音_2045054104585637890.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.3-音效配音_2045054104585637890.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（35 个）：
- `MarkdownNote`
- `PrimitiveInt`
- `PrimitiveFloat`
- `CLIPTextEncode` ★核心
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CLIPTextEncode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVChunkFeedForward`
- `LTXVConditioning`
- `LTXVAudioVideoMask`
- `LTXVEmptyLatentAudio` ★核心
- `PrimitiveInt`
- `MathExpression|pysssss`
- `LTXVPreprocess`
- `VAEEncode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoInfo`
- `GetImageRangeFromBatch`
- `CreateVideo`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `RH_LLMAPI_Pro_Node`
- `VAELoaderKJ`
- `easy showAnything`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VHS_LoadVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（30/35）

**有卡**：`CLIPTextEncode`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVSeparateAVLatent`、`LTXVChunkFeedForward`、`LTXVConditioning`、`LTXVAudioVideoMask`、`LTXVEmptyLatentAudio`、`MathExpression|pysssss`、`LTXVPreprocess`、`VAEEncode`、`LTXVAudioVAEDecode`、`VHS_VideoInfo`、`GetImageRangeFromBatch`、`CreateVideo`、`VAELoaderKJ`、`DualCLIPLoader`、`RH_LLMAPI_Pro_Node`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`UNETLoader`、`VHS_LoadVideo`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVAudioVAEDecode、LTXVConcatAVLatent
