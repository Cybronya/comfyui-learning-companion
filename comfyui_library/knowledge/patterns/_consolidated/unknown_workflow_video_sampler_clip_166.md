---
name: unknown_workflow_video_sampler_clip_166
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.67325
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, JWInteger, KSampler, LoadImage, ModelSamplingSD3, VAEDecode, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/07文生视频 T2V+全节点注释_2055495152193556482.json, 视频生成/文生视频/08图生视频 I2V -rapid-all in one+全节点注释_2055499440168947714.json, 视频生成/文生视频/Wan2.2 All-in-one V7文生视频（自用）_1955969425952395266.json, 视频生成/文生视频/Wan2.2万相4步加速视频生成-Rapid-AllInOne工作流_1972092157177884673.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_166

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/07文生视频 T2V+全节点注释_2055495152193556482.json、视频生成/文生视频/08图生视频 I2V -rapid-all in one+全节点注释_2055499440168947714.json、视频生成/文生视频/Wan2.2 All-in-one V7文生视频（自用）_1955969425952395266.json、视频生成/文生视频/Wan2.2万相4步加速视频生成-Rapid-AllInOne工作流_1972092157177884673.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `JWInteger`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `VAEDecode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `EmptyHunyuanLatentVideo` —— 3/4 个有
- `MathExpression|pysssss` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `WanImageToVideo` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `SaveLatent` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | sa_solver | - | 4 | 100% |
| 调度器 | normal | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
