---
name: unknown_workflow_video_lora_sampler_658
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.846333
common_nodes: [Audio Duration (mtb), CLIPTextEncode, EmptyImage, EmptyLTXVLatentVideo, Fast Groups Bypasser (rgthree), GetImageSize, ImageResizeKJv2, KSampler, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVPreprocess, LoadAudio, LoadImage, LoraLoaderModelOnly, PreviewAudio, SetLatentNoiseMask, SimpleMath+, SolidMask, VAEDecode, VHS_VideoCombine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/ltx2.3数字人_2029843228320600065.json, 视频生成/图生视频/个性化自定义数字人_2072235683716100097.json, 视频生成/文生视频/定制数字人_2072181596492492801.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_658

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/ltx2.3数字人_2029843228320600065.json、视频生成/图生视频/个性化自定义数字人_2072235683716100097.json、视频生成/文生视频/定制数字人_2072181596492492801.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `Audio Duration (mtb)`
- `CLIPTextEncode`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `ImageResizeKJv2`
- `KSampler`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewAudio`
- `SetLatentNoiseMask`
- `SimpleMath+`
- `SolidMask`
- `VAEDecode`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `DualCLIPLoader` —— 2/3 个有
- `LTX2_NAG` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `VAELoaderKJ` —— 2/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `ImagePadForOutpaint` —— 1/3 个有
- `LTXAVTextEncoderLoader` —— 1/3 个有
- `LTXVAudioVAELoader` —— 1/3 个有
- `MelBandRoFormerModelLoader` —— 1/3 个有
- `MelBandRoFormerSampler` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `TrimAudioDuration` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
