---
name: unknown_workflow_video_sampler_clip_134
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8096
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyHunyuanLatentVideo, ImageFromBatch+, JWInteger, KSampler, ModelSamplingSD3, VAEDecode, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Wan2.2 All-in-one V10文生视频加速版V2_1962791550226968577.json, 视频生成/文生视频/Wan2.2 All-in-one V6文生视频加速版_1956027106604011521.json, 视频生成/文生视频/Wan2.2 All-in-one V8.1文生视频加速版_1958143458798161921.json, 视频生成/文生视频/Wan2.2 All-in-one V9文生视频加速版V2_1958906003150548993.json, 视频生成/文生视频/（贞贞版）Wan2.2 All-in-one V9文生视频高动态极速版V1_1958907032336281602.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_134

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/Wan2.2 All-in-one V10文生视频加速版V2_1962791550226968577.json、视频生成/文生视频/Wan2.2 All-in-one V6文生视频加速版_1956027106604011521.json、视频生成/文生视频/Wan2.2 All-in-one V8.1文生视频加速版_1958143458798161921.json、视频生成/文生视频/Wan2.2 All-in-one V9文生视频加速版V2_1958906003150548993.json、视频生成/文生视频/（贞贞版）Wan2.2 All-in-one V9文生视频高动态极速版V1_1958907032336281602.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyHunyuanLatentVideo`
- `ImageFromBatch+`
- `JWInteger`
- `KSampler`
- `ModelSamplingSD3`
- `VAEDecode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 3/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | sa_solver | - | 5 | 60% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，5 个样本，一致性 60%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
