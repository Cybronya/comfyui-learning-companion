---
name: unknown_workflow_lora_sampler_clip_92
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.606333
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, CreateVideo, ImageBatch, ImageFromBatch, KSampler, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, PrimitiveInt, SaveVideo, UNETLoader, VAEDecode, VAELoader, WanInfiniteTalkToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/InfiniteTalk_图生视频_双人对话-对口型_2019310713029791745.json, 视频生成/图生视频/InfiniteTalk_数字人（单人）_2019342958109134850.json, 视频生成/图生视频/infinitetalk官方版双人Loop循环流(手动遮罩版）_2073309678620209153.json, 视频生成/图生视频/infinitetalk官方版双人Loop循环流(自动遮罩版）_2073309877631541249.json, 视频生成/图生视频/目前最强双人数字人infinitetalk官方版 循环流(自动遮罩版） 林耀2.6_2019770784713023490.json, 视频生成/图生视频/音频驱动 最强双人数字人视频生成 infinitetalk官方  循环流(自动遮罩版）_2021071474643177473.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_92

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/InfiniteTalk_图生视频_双人对话-对口型_2019310713029791745.json、视频生成/图生视频/InfiniteTalk_数字人（单人）_2019342958109134850.json、视频生成/图生视频/infinitetalk官方版双人Loop循环流(手动遮罩版）_2073309678620209153.json、视频生成/图生视频/infinitetalk官方版双人Loop循环流(自动遮罩版）_2073309877631541249.json、视频生成/图生视频/目前最强双人数字人infinitetalk官方版 循环流(自动遮罩版） 林耀2.6_2019770784713023490.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 6 个 workflow 都包含：
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
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanInfiniteTalkToVideo`

**可变部分**（部分 workflow 才有）：
- `AudioConcat` —— 5/6 个有
- `Audio Duration (mtb)` —— 4/6 个有
- `SimpleCalculatorKJ` —— 4/6 个有
- `VHS_VideoCombine` —— 4/6 个有
- `easy forLoopEnd` —— 4/6 个有
- `easy forLoopStart` —— 4/6 个有
- `MaskPreview` —— 3/6 个有
- `SegmentV2` —— 3/6 个有
- `ShowAnything|Mie` —— 3/6 个有
- `ZML_MaskSeparateDistance` —— 3/6 个有
- `GetNode` —— 2/6 个有
- `JWInteger` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `PreviewAudio` —— 2/6 个有
- `SetNode` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | normal | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 normal，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（17/6 个样本）：Steps较低可能导致细节不足
