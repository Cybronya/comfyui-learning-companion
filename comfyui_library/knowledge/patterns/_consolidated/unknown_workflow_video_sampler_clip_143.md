---
name: unknown_workflow_video_sampler_clip_143
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8342
common_nodes: [ApplySageAttention, CLIPTextEncode, CheckpointLoaderSimple, JWInteger, KSampler, ModelSamplingSD3, VAEDecode, VHS_VideoCombine, WanVaceToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Wan2.2 Rapid-AIO-Mega V4文生视频极速版_1973020564535250945.json, 视频生成/文生视频/Wan2.2 Rapid-AIO-Mega V5文生视频极速版_1974823534423879681.json, 视频生成/文生视频/Wan2.2 Rapid-AIO-Mega V5文生视频极速版_1975808111913119746.json, 视频生成/文生视频/Wan2.2 Rapid-AIO-Mega V6文生视频极速版_1975830963999649793.json, 视频生成/文生视频/Wan2.2 Rapid-AIO-Mega文生视频极速版_1967877695067533314.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_143

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/Wan2.2 Rapid-AIO-Mega V4文生视频极速版_1973020564535250945.json、视频生成/文生视频/Wan2.2 Rapid-AIO-Mega V5文生视频极速版_1974823534423879681.json、视频生成/文生视频/Wan2.2 Rapid-AIO-Mega V5文生视频极速版_1975808111913119746.json、视频生成/文生视频/Wan2.2 Rapid-AIO-Mega V6文生视频极速版_1975830963999649793.json、视频生成/文生视频/Wan2.2 Rapid-AIO-Mega文生视频极速版_1967877695067533314.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `ApplySageAttention`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `JWInteger`
- `KSampler`
- `ModelSamplingSD3`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanVaceToVideo`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | ipndm | - | 5 | 80% |
| 调度器 | sgm_uniform | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ipndm，5 个样本，一致性 80%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
