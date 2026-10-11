---
key: 视频生成/文生视频/ltx2.3_Q4_gguf_文生视频（字幕压制版）_2038972879353679874.json
name: ltx2.3_Q4_gguf_文生视频（字幕压制版）_2038972879353679874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx2.3_Q4_gguf_文生视频（字幕压制版）_2038972879353679874.json
hash: 75bf470be72a5654
coverage: 0.843137
learned_at: 2026-10-11 19:49:44
nodes: [LTXVLatentUpsampler, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, SimpleMath+, Int, Note, LTXVSeparateAVLatent, Note, PathchSageAttentionKJ, ModelPatchTorchSettings, CLIPTextEncode, RH_LLMAPI_Pro_Node, StringToAnyNode, easy showAnything, Int, Int, Int, easy boolean, ComfySwitchNode, VAEDecodeTiled, LTXVAudioVAEDecode, CM_IntToFloat, RandomNoise, RandomNoise, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, SaveVideo, CreateVideo, LTXVChunkFeedForward, LTXVConditioning, UnetLoaderGGUF, LatentUpscaleModelLoader, VAELoaderKJ, LTXVSeparateAVLatent, VAELoaderKJ, LTXVConcatAVLatent, LTX2_NAG, CR Text, LTX2SamplingPreviewOverride, CLIPTextEncode, SamplerCustomAdvanced, LayerUtility: PurgeVRAM V2, DualCLIPLoader, DualCLIPLoaderGGUF, SamplerCustomAdvanced, CFGGuider, LTX2SamplingPreviewOverride, CFGGuider]
patterns: []
missing: [CR Text, LayerUtility: PurgeVRAM V2, SimpleMath+, easy boolean]
parameters: {"batch_size": 1, "height": 24, "width": 241}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识]
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

覆盖率 **84%**（43/51）

**有卡**：`LTXVLatentUpsampler`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`Int`、`LTXVSeparateAVLatent`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPTextEncode`、`RH_LLMAPI_Pro_Node`、`StringToAnyNode`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CM_IntToFloat`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`SaveVideo`、`CreateVideo`、`LTXVChunkFeedForward`、`LTXVConditioning`、`UnetLoaderGGUF`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`SamplerCustomAdvanced`、`DualCLIPLoader`、`DualCLIPLoaderGGUF`、`CFGGuider`

**缺卡**（4）：`CR Text`、`LayerUtility: PurgeVRAM V2`、`SimpleMath+`、`easy boolean`

**用到的条目**：CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent、LTXVSeparateAVLatent、VAEDecodeTiled

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
