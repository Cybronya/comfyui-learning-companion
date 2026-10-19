---
name: unknown_workflow_video_sampler_clip_103
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7526
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSampler, ModelSamplingSD3, PrimitiveInt, VAEDecode, VHS_VideoCombine, WanVaceToVideo]
problems: [Steps较低可能导致细节不足]
missing: [Label (rgthree)]
members: [图片生成/文生图/1987118145712361473.json, 视频生成/图生视频/1970121529851867137.json, 视频生成/图生视频/1970032698750365698.json, 视频生成/图生视频/1970029254320812033.json, 视频生成/图生视频/1981747829813190657.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_103

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1987118145712361473.json、视频生成/图生视频/1970121529851867137.json、视频生成/图生视频/1970032698750365698.json、视频生成/图生视频/1970029254320812033.json、视频生成/图生视频/1981747829813190657.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSampler`
- `ModelSamplingSD3`
- `PrimitiveInt`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/5 个有
- `WanVideoVACEStartToEndFrame` —— 4/5 个有
- `MathExpression|pysssss` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `DF_Integer` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `LoadAudio` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | ipndm | - | 5 | 80% |
| 调度器 | beta | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ipndm，5 个样本，一致性 80%
- 调度器 最常用 beta，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Label (rgthree)
