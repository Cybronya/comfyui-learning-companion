---
name: unknown_workflow_video_sampler_clip_106
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.9705
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, GetImageRangeFromBatch, GetImageSizeAndCount, INTConstant, ImageBatchMulti, ImageResizeKJ, KSampler, LoadImage, MaskBatchMulti, ModelSamplingSD3, String Literal, VAEDecode, VHS_VideoCombine, WanVaceToVideo, WanVideoVACEStartToEndFrame]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/最强丝滑过渡mega首尾帧（任意调节）_1971209701084057601.json, 视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-3图首尾帧_1982052292696391681.json, 视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-4图首尾帧_1982052313701457921.json, 视频生成/文生视频/Mega-v3-AllInOne-3图首尾帧_1971152097230102529.json, 视频生成/文生视频/Mega-v3-AllInOne-4图首尾帧_1971242674084859905.json, 视频生成/文生视频/Mega-v3-AllInOne-6图首尾帧_1971236337447845889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_106

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/最强丝滑过渡mega首尾帧（任意调节）_1971209701084057601.json、视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-3图首尾帧_1982052292696391681.json、视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-4图首尾帧_1982052313701457921.json、视频生成/文生视频/Mega-v3-AllInOne-3图首尾帧_1971152097230102529.json、视频生成/文生视频/Mega-v3-AllInOne-4图首尾帧_1971242674084859905.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageBatchMulti`
- `ImageResizeKJ`
- `KSampler`
- `LoadImage`
- `MaskBatchMulti`
- `ModelSamplingSD3`
- `String Literal`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 4/6 个有
- `AV_VAELoader` —— 1/6 个有
- `CLIPLoader` —— 1/6 个有
- `LayerMask: MaskPreview` —— 1/6 个有
- `PreviewImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | ipndm | - | 6 | 83% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ipndm，6 个样本，一致性 83%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
