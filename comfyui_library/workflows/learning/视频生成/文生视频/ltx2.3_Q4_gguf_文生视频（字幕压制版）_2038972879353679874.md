---
key: 视频生成/文生视频/ltx2.3_Q4_gguf_文生视频（字幕压制版）_2038972879353679874.json
name: ltx2.3_Q4_gguf_文生视频（字幕压制版）_2038972879353679874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx2.3_Q4_gguf_文生视频（字幕压制版）_2038972879353679874.json
hash: 75bf470be72a5654
coverage: 0.921569
learned_at: 2026-10-15 22:47:22
nodes: [LTXVLatentUpsampler, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, SimpleMath+, Int, Note, LTXVSeparateAVLatent, Note, PathchSageAttentionKJ, ModelPatchTorchSettings, CLIPTextEncode, RH_LLMAPI_Pro_Node, StringToAnyNode, easy showAnything, Int, Int, Int, easy boolean, ComfySwitchNode, VAEDecodeTiled, LTXVAudioVAEDecode, CM_IntToFloat, RandomNoise, RandomNoise, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, SaveVideo, CreateVideo, LTXVChunkFeedForward, LTXVConditioning, UnetLoaderGGUF, LatentUpscaleModelLoader, VAELoaderKJ, LTXVSeparateAVLatent, VAELoaderKJ, LTXVConcatAVLatent, LTX2_NAG, CR Text, LTX2SamplingPreviewOverride, CLIPTextEncode, SamplerCustomAdvanced, LayerUtility: PurgeVRAM V2, DualCLIPLoader, DualCLIPLoaderGGUF, SamplerCustomAdvanced, CFGGuider, LTX2SamplingPreviewOverride, CFGGuider]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 241}
---

# 视频生成/文生视频/ltx2.3_Q4_gguf_文生视频（字幕压制版）_2038972879353679874.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ltx2.3_Q4_gguf_文生视频（字幕压制版）_2038972879353679874.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（51 个）：
- `LTXVLatentUpsampler` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `SimpleMath+`
- `Int`
- `Note`
- `LTXVSeparateAVLatent`
- `Note`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `CLIPTextEncode` ★核心
- `RH_LLMAPI_Pro_Node`
- `StringToAnyNode`
- `easy showAnything`
- `Int`
- `Int`
- `Int`
- `easy boolean`
- `ComfySwitchNode`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CM_IntToFloat`
- `RandomNoise`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SaveVideo`
- `CreateVideo`
- `LTXVChunkFeedForward`
- `LTXVConditioning`
- `UnetLoaderGGUF` ★核心
- `LatentUpscaleModelLoader`
- `VAELoaderKJ`
- `LTXVSeparateAVLatent`
- `VAELoaderKJ`
- `LTXVConcatAVLatent`
- `LTX2_NAG`
- `CR Text`
- `LTX2SamplingPreviewOverride`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `DualCLIPLoader`
- `DualCLIPLoaderGGUF`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `LTX2SamplingPreviewOverride`
- `CFGGuider`

## 关键参数

- `width` = `241`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（47/51）

**有卡**：`LTXVLatentUpsampler`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`SimpleMath+`、`Int`、`LTXVSeparateAVLatent`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPTextEncode`、`RH_LLMAPI_Pro_Node`、`StringToAnyNode`、`easy boolean`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CM_IntToFloat`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`SaveVideo`、`CreateVideo`、`LTXVChunkFeedForward`、`LTXVConditioning`、`UnetLoaderGGUF`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`LTX2_NAG`、`CR Text`、`LTX2SamplingPreviewOverride`、`SamplerCustomAdvanced`、`LayerUtility: PurgeVRAM V2`、`DualCLIPLoader`、`DualCLIPLoaderGGUF`、`CFGGuider`

**用到的条目**：CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent、LTXVSeparateAVLatent、VAEDecodeTiled
