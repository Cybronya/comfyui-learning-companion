---
name: unknown_workflow_video_lora_sampler_359
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.652
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, ImageResizeKJv2, KSamplerSelect, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2040053495893598209.json, 视频生成/图生视频/2056919116946173954.json, 视频生成/图生视频/2080550056238862337.json, 视频生成/图生视频/video_ltx2_3_best_faceid_ganloss_2083097564500549633.json, 视频生成/文生视频/LTX 2.3+PromptRelay 三图参考_2054192199897755650.json, 视频生成/文生视频/LTX2.3+PromptRelay+四图参考_2056629366276321282.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_359

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2040053495893598209.json、视频生成/图生视频/2056919116946173954.json、视频生成/图生视频/2080550056238862337.json、视频生成/图生视频/video_ltx2_3_best_faceid_ganloss_2083097564500549633.json、视频生成/文生视频/LTX 2.3+PromptRelay 三图参考_2054192199897755650.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 4/6 个有
- `LTX2_NAG` —— 4/6 个有
- `LTXVAddGuideMulti` —— 4/6 个有
- `LTXVAudioVAEDecode` —— 4/6 个有
- `MathExpression|pysssss` —— 4/6 个有
- `PathchSageAttentionKJ` —— 4/6 个有
- `PromptRelayEncodeTimeline` —— 4/6 个有
- `ComfyMathExpression` —— 2/6 个有
- `LTXIdentityOverlapConditioning` —— 2/6 个有
- `LatentUpscaleModelLoader` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `RMBG` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 361 | 97 - 465 | 6 | 51% |
| 高度 | 24 | 24 - 25 | 6 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 361，观测区间 97 - 465，6 个样本
- 高度 中位数 24，观测区间 24 - 25，6 个样本，取值集中（一致性 98%）
