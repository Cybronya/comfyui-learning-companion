---
name: unknown_workflow_upscale_latent_upscale_sampler_9
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.9545
common_nodes: [CFGGuider, CLIPTextEncode, CM_IntToFloat, CR Text, ComfySwitchNode, CreateVideo, EmptyLTXVLatentVideo, Int, KSamplerSelect, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: PurgeVRAM V2, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, SaveVideo, SimpleMath+, StringToAnyNode, VAEDecodeTiled, easy boolean, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/ltx2.3 首帧生视频+lora_2045560076383035394.json, 视频生成/图生视频/ltx2.3_Q4_gguf_首尾帧生视频（字幕压制版）_2038979711182839810.json, 视频生成/图生视频/ltx2.3_Q4_gguf_首帧生视频（字幕压制版）_2038953188350500865.json, 视频生成/图生视频/ltx2.3图生视频_2034896033376899073.json, 视频生成/图生视频/ltx2.3首尾帧生视频_2034985387369697281.json, 视频生成/图生视频/ltx2.3首帧生视频优化版_2045761939795611649.json, 视频生成/图生视频/ltx2.3首帧生视频优化版_2071735603636563970.json, 视频生成/图生视频/ltx_2045411758013161473.json, 视频生成/文生视频/ltx2.3_Q4_gguf_文生视频（字幕压制版）_2038972879353679874.json, 视频生成/文生视频/ltx2.3文生视频_2033751992933294081.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_9

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/ltx2.3 首帧生视频+lora_2045560076383035394.json、视频生成/图生视频/ltx2.3_Q4_gguf_首尾帧生视频（字幕压制版）_2038979711182839810.json、视频生成/图生视频/ltx2.3_Q4_gguf_首帧生视频（字幕压制版）_2038953188350500865.json、视频生成/图生视频/ltx2.3图生视频_2034896033376899073.json、视频生成/图生视频/ltx2.3首尾帧生视频_2034985387369697281.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_IntToFloat`
- `CR Text`
- `ComfySwitchNode`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `Int`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: PurgeVRAM V2`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SimpleMath+`
- `StringToAnyNode`
- `VAEDecodeTiled`
- `easy boolean`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LTXVPreprocess` —— 8/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/10 个有
- `LoadImage` —— 8/10 个有
- `LoraLoaderModelOnly` —— 8/10 个有
- `DualCLIPLoader` —— 7/10 个有
- `LTX2SamplingPreviewOverride` —— 7/10 个有
- `LTX2_NAG` —— 7/10 个有
- `UnetLoaderGGUF` —— 7/10 个有
- `VAELoaderKJ` —— 7/10 个有
- `DualCLIPLoaderGGUF` —— 5/10 个有
- `LTXVCropGuides` —— 5/10 个有
- `LTXVImgToVideoConditionOnly` —— 5/10 个有
- `CheckpointLoaderSimple` —— 3/10 个有
- `LTXAVTextEncoderLoader` —— 3/10 个有
- `LTXVAudioVAELoader` —— 3/10 个有
- `LTXVImgToVideoInplaceKJ` —— 3/10 个有
- `LTXVScheduler` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 241 | 241 - 241 | 10 | 100% |
| 高度 | 24 | 24 - 24 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 241，观测区间 241 - 241，10 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，10 个样本，取值集中（一致性 100%）
