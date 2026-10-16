---
key: 视频生成/图生视频/ltx2.3_Q4_gguf_首尾帧生视频（字幕压制版）_2038979711182839810.json
name: ltx2.3_Q4_gguf_首尾帧生视频（字幕压制版）_2038979711182839810.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2038979711182839810.json
hash: 1572c8e346065b35
coverage: 0.964286
learned_at: 2026-10-15 22:36:06
nodes: [PathchSageAttentionKJ, ManualSigmas, LTXVEmptyLatentAudio, SamplerCustomAdvanced, EmptyLTXVLatentVideo, SimpleMath+, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVPreprocess, LTXVPreprocess, LTXVLatentUpsampler, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CM_IntToFloat, SaveVideo, CreateVideo, StringToAnyNode, easy showAnything, LTXVConcatAVLatent, LayerUtility: ImageScaleByAspectRatio V2, SamplerCustomAdvanced, LayerUtility: PurgeVRAM V2, RandomNoise, RandomNoise, Int, Int, LayerUtility: ImageScaleByAspectRatio V2, UnetLoaderGGUF, VAELoaderKJ, KSamplerSelect, LTXVChunkFeedForward, CLIPTextEncode, LTXVConditioning, LTX2SamplingPreviewOverride, CFGGuider, KSamplerSelect, ManualSigmas, LTX2SamplingPreviewOverride, CFGGuider, LoadImage, LTXVImgToVideoInplaceKJ, ComfySwitchNode, RH_LLMAPI_Pro_Node, LoadImage, LTXVImgToVideoInplaceKJ, VAELoaderKJ, LTX2_NAG, CR Text, CLIPTextEncode, ModelPatchTorchSettings, DualCLIPLoader, LatentUpscaleModelLoader, DualCLIPLoaderGGUF, Int, easy boolean]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 241}
---

# 视频生成/图生视频/ltx2.3_Q4_gguf_首尾帧生视频（字幕压制版）_2038979711182839810.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2038979711182839810.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `PathchSageAttentionKJ`
- `ManualSigmas`
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `EmptyLTXVLatentVideo`
- `SimpleMath+`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CM_IntToFloat`
- `SaveVideo`
- `CreateVideo`
- `StringToAnyNode`
- `easy showAnything`
- `LTXVConcatAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SamplerCustomAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `RandomNoise`
- `RandomNoise`
- `Int`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UnetLoaderGGUF` ★核心
- `VAELoaderKJ`
- `KSamplerSelect` ★核心
- `LTXVChunkFeedForward`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTX2SamplingPreviewOverride`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTX2SamplingPreviewOverride`
- `CFGGuider`
- `LoadImage`
- `LTXVImgToVideoInplaceKJ`
- `ComfySwitchNode`
- `RH_LLMAPI_Pro_Node`
- `LoadImage`
- `LTXVImgToVideoInplaceKJ`
- `VAELoaderKJ`
- `LTX2_NAG`
- `CR Text`
- `CLIPTextEncode` ★核心
- `ModelPatchTorchSettings`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `DualCLIPLoaderGGUF`
- `Int`
- `easy boolean`

## 关键参数

- `width` = `241`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **96%**（54/56）

**有卡**：`PathchSageAttentionKJ`、`ManualSigmas`、`LTXVEmptyLatentAudio`、`SamplerCustomAdvanced`、`EmptyLTXVLatentVideo`、`SimpleMath+`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTXVPreprocess`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CM_IntToFloat`、`SaveVideo`、`CreateVideo`、`StringToAnyNode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM V2`、`RandomNoise`、`Int`、`UnetLoaderGGUF`、`VAELoaderKJ`、`KSamplerSelect`、`LTXVChunkFeedForward`、`CLIPTextEncode`、`LTXVConditioning`、`LTX2SamplingPreviewOverride`、`CFGGuider`、`LoadImage`、`LTXVImgToVideoInplaceKJ`、`RH_LLMAPI_Pro_Node`、`LTX2_NAG`、`CR Text`、`ModelPatchTorchSettings`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`DualCLIPLoaderGGUF`、`easy boolean`

**用到的条目**：CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent、LTXVSeparateAVLatent
