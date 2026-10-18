---
key: 音频生成/音频生成/LTX2.3-无声视频音效设计优化版V2_2030312017944383489.json
name: LTX2.3-无声视频音效设计优化版V2_2030312017944383489
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/LTX2.3-无声视频音效设计优化版V2_2030312017944383489.json
hash: cefbfcec668f6377
coverage: 0.857143
learned_at: 2026-10-18 02:28:41
nodes: [MarkdownNote, PrimitiveInt, PrimitiveFloat, CLIPTextEncode, ModelPatchTorchSettings, PathchSageAttentionKJ, LTXVConcatAVLatent, SamplerCustomAdvanced, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, CLIPTextEncode, LTXVSeparateAVLatent, LTXVChunkFeedForward, LTXVConditioning, LTXVAudioVideoMask, LTXVEmptyLatentAudio, PrimitiveInt, MathExpression|pysssss, LTXVPreprocess, VAEEncode, LTXVAudioVAEDecode, VHS_VideoInfo, GetImageRangeFromBatch, CreateVideo, VAELoaderKJ, DualCLIPLoader, RH_LLMAPI_Pro_Node, VHS_LoadVideo, VAELoaderKJ, easy showAnything, VHS_VideoCombine, LoraLoaderModelOnly, UNETLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 音频生成/音频生成/LTX2.3-无声视频音效设计优化版V2_2030312017944383489.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/LTX2.3-无声视频音效设计优化版V2_2030312017944383489.json`

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
- `VHS_LoadVideo`
- `VAELoaderKJ`
- `easy showAnything`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（30/35）

**有卡**：`CLIPTextEncode`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVSeparateAVLatent`、`LTXVChunkFeedForward`、`LTXVConditioning`、`LTXVAudioVideoMask`、`LTXVEmptyLatentAudio`、`MathExpression|pysssss`、`LTXVPreprocess`、`VAEEncode`、`LTXVAudioVAEDecode`、`VHS_VideoInfo`、`GetImageRangeFromBatch`、`CreateVideo`、`VAELoaderKJ`、`DualCLIPLoader`、`RH_LLMAPI_Pro_Node`、`VHS_LoadVideo`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`UNETLoader`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent
