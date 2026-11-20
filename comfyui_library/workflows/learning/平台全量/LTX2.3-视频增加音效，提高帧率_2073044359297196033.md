---
key: 平台全量/LTX2.3-视频增加音效，提高帧率_2073044359297196033.json
name: LTX2.3-视频增加音效，提高帧率_2073044359297196033
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.3-视频增加音效，提高帧率_2073044359297196033.json
hash: aca2c3b81be22402
coverage: 0.864865
learned_at: 2026-11-14 00:38:15
nodes: [MarkdownNote, ModelPatchTorchSettings, PathchSageAttentionKJ, LTXVChunkFeedForward, VHS_VideoInfo, DualCLIPLoader, LoraLoaderModelOnly, UNETLoader, SamplerCustomAdvanced, ManualSigmas, KSamplerSelect, RandomNoise, easy showAnything, CreateVideo, VAEDecode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, CLIPTextEncode, RH_LLMAPI_Pro_Node, PrimitiveInt, PrimitiveInt, PrimitiveFloat, VAELoaderKJ, LTXVConditioning, CFGGuider, VAELoaderKJ, GetImageRangeFromBatch, VAEEncode, MathExpression|pysssss, LTXVAudioVideoMask, LTXVEmptyLatentAudio, LTXVConcatAVLatent, LTXVPreprocess, VHS_VideoCombine, VHS_LoadVideo, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/LTX2.3-视频增加音效，提高帧率_2073044359297196033.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.3-视频增加音效，提高帧率_2073044359297196033.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（37 个）：
- `MarkdownNote`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `VHS_VideoInfo`
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `easy showAnything`
- `CreateVideo`
- `VAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `CLIPTextEncode` ★核心
- `RH_LLMAPI_Pro_Node`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveFloat`
- `VAELoaderKJ`
- `LTXVConditioning`
- `CFGGuider`
- `VAELoaderKJ`
- `GetImageRangeFromBatch`
- `VAEEncode` ★核心
- `MathExpression|pysssss`
- `LTXVAudioVideoMask`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `LTXVPreprocess`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `CLIPTextEncode` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（32/37）

**有卡**：`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`VHS_VideoInfo`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`SamplerCustomAdvanced`、`ManualSigmas`、`KSamplerSelect`、`RandomNoise`、`CreateVideo`、`VAEDecode`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`CLIPTextEncode`、`RH_LLMAPI_Pro_Node`、`VAELoaderKJ`、`LTXVConditioning`、`CFGGuider`、`GetImageRangeFromBatch`、`VAEEncode`、`MathExpression|pysssss`、`LTXVAudioVideoMask`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`LTXVPreprocess`、`VHS_VideoCombine`、`VHS_LoadVideo`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVAudioVAEDecode
