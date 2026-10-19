---
name: unknown_workflow_sampler_clip_checkpoint_7
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.796
common_nodes: [ApplySageAttention, CLIPTextEncode, CheckpointLoaderSimple, JWInteger, KSampler, ModelSamplingSD3, VAEDecode, WanVaceToVideo]
problems: [Steps较低可能导致细节不足]
missing: [ImageFromBatch+, CR Prompt Text]
members: [视频生成/文生视频/1973020564535250945.json, 视频生成/文生视频/1974823534423879681.json, 视频生成/文生视频/1975808111913119746.json, 视频生成/文生视频/1975830963999649793.json, 视频生成/文生视频/1977017622829125634.json, 视频生成/文生视频/1977742174395793409.json, 视频生成/文生视频/1967877695067533314.json, 视频生成/文生视频/wan2.2-aio-v7-文生视频_1982741566634762241.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_7

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/1973020564535250945.json、视频生成/文生视频/1974823534423879681.json、视频生成/文生视频/1975808111913119746.json、视频生成/文生视频/1975830963999649793.json、视频生成/文生视频/1977017622829125634.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 8 个 workflow 都包含：
- `ApplySageAttention`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `JWInteger`
- `KSampler`
- `ModelSamplingSD3`
- `VAEDecode`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 6/8 个有
- `ImageFromBatch+` —— 3/8 个有
- `SaveImage` —— 3/8 个有
- `LoadImage` —— 2/8 个有
- `TT_img_enc` —— 2/8 个有
- `TT_img_enc_v2` —— 2/8 个有
- `CR Prompt Text` —— 1/8 个有
- `DeepTranslatorTextNode` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `MathExpression|pysssss` —— 1/8 个有
- `SetNode` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | ipndm | - | 8 | 50% |
| 调度器 | sgm_uniform | - | 8 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ipndm，8 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，8 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：ImageFromBatch+、CR Prompt Text
