---
name: unknown_workflow_video_lora_sampler_430
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7082
common_nodes: [Audio Duration (mtb), AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, CreateVideo, ImageBatch, ImageFromBatch, KSampler, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, PrimitiveInt, SaveVideo, SimpleCalculatorKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanInfiniteTalkToVideo, easy forLoopEnd, easy forLoopStart]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/infinitetalk官方版单人Loop循环流_2073310072448577538.json, 视频生成/图生视频/infinitetalk官方版双人Loop循环流(手动遮罩版）_2073309678620209153.json, 视频生成/图生视频/infinitetalk官方版双人Loop循环流(自动遮罩版）_2073309877631541249.json, 视频生成/图生视频/目前最强双人数字人infinitetalk官方版 循环流(自动遮罩版） 林耀2.6_2019770784713023490.json, 视频生成/图生视频/音频驱动 最强双人数字人视频生成 infinitetalk官方  循环流(自动遮罩版）_2021071474643177473.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_430

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/infinitetalk官方版单人Loop循环流_2073310072448577538.json、视频生成/图生视频/infinitetalk官方版双人Loop循环流(手动遮罩版）_2073309678620209153.json、视频生成/图生视频/infinitetalk官方版双人Loop循环流(自动遮罩版）_2073309877631541249.json、视频生成/图生视频/目前最强双人数字人infinitetalk官方版 循环流(自动遮罩版） 林耀2.6_2019770784713023490.json、视频生成/图生视频/音频驱动 最强双人数字人视频生成 infinitetalk官方  循环流(自动遮罩版）_2021071474643177473.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 5 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `CreateVideo`
- `ImageBatch`
- `ImageFromBatch`
- `KSampler`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `PrimitiveInt`
- `SaveVideo`
- `SimpleCalculatorKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanInfiniteTalkToVideo`
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `AudioConcat` —— 4/5 个有
- `MaskPreview` —— 3/5 个有
- `SegmentV2` —— 3/5 个有
- `ShowAnything|Mie` —— 3/5 个有
- `ZML_MaskSeparateDistance` —— 3/5 个有
- `JWInteger` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `PreviewAudio` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（10/5 个样本）：Steps较低可能导致细节不足
