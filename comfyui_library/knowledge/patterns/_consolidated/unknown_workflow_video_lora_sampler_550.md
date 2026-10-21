---
name: unknown_workflow_video_lora_sampler_550
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.96025
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CR Text, CheckpointLoaderSimple, DapaoImageAspectRatioResizeNode, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveBoolean, PrimitiveFloat, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, Seed (rgthree), SimpleMath+, VAEDecodeTiled, VHS_VideoCombine, easy cleanGpuUsed, easy int]
problems: []
missing: []
members: [视频生成/图生视频/2030910422534066178.json, 视频生成/文生视频/LTX2.3 图生视频 提示词自动优化版  数字人说话唱歌_2051094708809678850.json, 视频生成/文生视频/LTX2.3+图生视频 提示词自动优化版 数字人说话唱歌_2063795562855624705.json, 视频生成/文生视频/图生视频LTX2.3 +提示词自动优化版+数字人说话唱歌_2066319019455639554.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_550

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2030910422534066178.json、视频生成/文生视频/LTX2.3 图生视频 提示词自动优化版  数字人说话唱歌_2051094708809678850.json、视频生成/文生视频/LTX2.3+图生视频 提示词自动优化版 数字人说话唱歌_2063795562855624705.json、视频生成/文生视频/图生视频LTX2.3 +提示词自动优化版+数字人说话唱歌_2066319019455639554.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CR Text`
- `CheckpointLoaderSimple`
- `DapaoImageAspectRatioResizeNode`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `Seed (rgthree)`
- `SimpleMath+`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `LTXVAudioVAEEncode` —— 1/4 个有
- `LoadAudio` —— 1/4 个有
- `MelBandRoFormerModelLoader` —— 1/4 个有
- `MelBandRoFormerSampler` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `SetLatentNoiseMask` —— 1/4 个有
- `SolidMask` —— 1/4 个有
- `SoundFlow_GetLength` —— 1/4 个有
- `TrimAudioDuration` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
