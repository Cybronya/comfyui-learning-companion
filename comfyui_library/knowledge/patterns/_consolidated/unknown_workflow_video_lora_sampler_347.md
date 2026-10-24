---
name: unknown_workflow_video_lora_sampler_347
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.704833
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, ImageResizeKJv2, KSamplerSelect, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, PathchSageAttentionKJ, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX 2.3+PromptRelay 三图参考_2040053495893598209.json, 视频生成/图生视频/LTX+2.3+PromptRelay+三图参考_2056919116946173954.json, 视频生成/图生视频/ltx无字幕多图参考promptrelay_2050899507684098050.json, 视频生成/文生视频/LTX 2.3+PromptRelay 三图参考_2054192199897755650.json, 视频生成/文生视频/LTX2.3+PromptRelay+四图参考_2056629366276321282.json, 视频生成/文生视频/LTX不出字幕单图参考_无压缩参考_2049840291389157378.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_347

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/LTX 2.3+PromptRelay 三图参考_2040053495893598209.json、视频生成/图生视频/LTX+2.3+PromptRelay+三图参考_2056919116946173954.json、视频生成/图生视频/ltx无字幕多图参考promptrelay_2050899507684098050.json、视频生成/文生视频/LTX 2.3+PromptRelay 三图参考_2054192199897755650.json、视频生成/文生视频/LTX2.3+PromptRelay+四图参考_2056629366276321282.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PromptRelayEncodeTimeline` —— 5/6 个有
- `GetImageRangeFromBatch` —— 4/6 个有
- `LTXVAddGuideMulti` —— 4/6 个有
- `BasicScheduler` —— 2/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `DF_Int_to_Float` —— 2/6 个有
- `Int` —— 2/6 个有
- `LTX2SamplingPreviewOverride` —— 2/6 个有
- `LTXVImgToVideoInplaceKJ` —— 2/6 个有
- `LTXVLatentUpsampler` —— 2/6 个有
- `LatentUpscaleModelLoader` —— 2/6 个有
- `ModelSamplingSD3` —— 2/6 个有
- `PreviewAny` —— 2/6 个有
- `SamplerCustom` —— 2/6 个有
- `SimpleMath+` —— 2/6 个有
- `VAELoader` —— 2/6 个有
- `VisualizeSigmasKJ` —— 2/6 个有
- `LTXVImgToVideoInplace` —— 1/6 个有
- `easy positive` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 361 | 305 - 465 | 6 | 85% |
| 高度 | 24 | 24 - 24 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 361，观测区间 305 - 465，6 个样本，取值集中（一致性 85%）
- 高度 中位数 24，观测区间 24 - 24，6 个样本，取值集中（一致性 100%）
