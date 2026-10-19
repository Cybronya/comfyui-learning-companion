---
name: unknown_workflow_video_sampler_clip_72
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.867125
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyHunyuanLatentVideo, KSampler, ModelSamplingSD3, VAEDecode, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: PurgeVRAM]
members: [视频生成/文生视频/1970121357323366402.json, 视频生成/文生视频/1962791550226968577.json, 视频生成/文生视频/1956027106604011521.json, 视频生成/文生视频/1958143458798161921.json, 视频生成/文生视频/1958906003150548993.json, 视频生成/文生视频/1955156862251536386.json, 视频生成/文生视频/文生视频Wan2.2 - T2V-rapid-aio AI 文生视频_2009171871626960898.json, 视频生成/文生视频/1958907032336281602.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_72

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/1970121357323366402.json、视频生成/文生视频/1962791550226968577.json、视频生成/文生视频/1956027106604011521.json、视频生成/文生视频/1958143458798161921.json、视频生成/文生视频/1958906003150548993.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `ModelSamplingSD3`
- `VAEDecode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageFromBatch+` —— 5/8 个有
- `JWInteger` —— 5/8 个有
- `PathchSageAttentionKJ` —— 3/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 8 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler_ancestral | - | 8 | 50% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，8 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，8 个样本，一致性 50%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM
