---
name: unknown_workflow_video_sampler_clip_153
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSampler, ModelSamplingSD3, VAEDecode, VHS_VideoCombine, WanVaceToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/AIO-MegaV2-图生视频_1970032698750365698.json, 视频生成/图生视频/AIO-MegaV2-文生视频_1970029254320812033.json, 视频生成/图生视频/AIO-mega-v9-Wan2.2_fast_图生视频_1981747829813190657.json, 视频生成/图生视频/ALL-IN-ONE720P_25fps图生视频_1990981841551302658.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_153

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/AIO-MegaV2-图生视频_1970032698750365698.json、视频生成/图生视频/AIO-MegaV2-文生视频_1970029254320812033.json、视频生成/图生视频/AIO-mega-v9-Wan2.2_fast_图生视频_1981747829813190657.json、视频生成/图生视频/ALL-IN-ONE720P_25fps图生视频_1990981841551302658.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSampler`
- `ModelSamplingSD3`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `MathExpression|pysssss` —— 3/4 个有
- `PrimitiveInt` —— 3/4 个有
- `WanVideoVACEStartToEndFrame` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `DF_Integer` —— 1/4 个有
- `JWFloat` —— 1/4 个有
- `JWInteger` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | ipndm | - | 4 | 75% |
| 调度器 | sgm_uniform | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ipndm，4 个样本，一致性 75%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
