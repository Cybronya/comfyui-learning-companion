---
name: unknown_workflow_video_sampler_clip_91
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.654333
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, JWInteger, KSampler, LoadImage, MathExpression|pysssss, ModelSamplingSD3, VAEDecode, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss]
members: [视频生成/图生视频/1972092157177884673.json, 视频生成/图生视频/2039317134282592258.json, 视频生成/文生视频/05基础版本+图生视频+全节点注释_2055549946513903617.json, 视频生成/文生视频/07文生视频 T2V+全节点注释_2055495152193556482.json, 视频生成/文生视频/08图生视频 I2V -rapid-all in one+全节点注释_2055499440168947714.json, 视频生成/文生视频/1972092157177884673.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_91

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1972092157177884673.json、视频生成/图生视频/2039317134282592258.json、视频生成/文生视频/05基础版本+图生视频+全节点注释_2055549946513903617.json、视频生成/文生视频/07文生视频 T2V+全节点注释_2055495152193556482.json、视频生成/文生视频/08图生视频 I2V -rapid-all in one+全节点注释_2055499440168947714.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `JWInteger`
- `KSampler`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `VAEDecode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `WanImageToVideo` —— 5/6 个有
- `EmptyHunyuanLatentVideo` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `wanBlockSwap` —— 2/6 个有
- `Text Multiline` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | sa_solver | - | 6 | 100% |
| 调度器 | normal | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，6 个样本，一致性 100%
- 调度器 最常用 normal，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、MathExpression|pysssss
