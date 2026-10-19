---
name: unknown_workflow_video_lora_clip_10
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.96825
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.2文生视频加速版（4步加速lora+MOE版）_2062184071983357953.json, 视频生成/文生视频/Wan2.2文生视频加速版（4步加速lora+官方版）_2019642699384627202.json, 视频生成/文生视频/1955652862984556545.json, 视频生成/文生视频/1950151381917327361.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_10

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/Wan2.2文生视频加速版（4步加速lora+MOE版）_2062184071983357953.json、视频生成/文生视频/Wan2.2文生视频加速版（4步加速lora+官方版）_2019642699384627202.json、视频生成/文生视频/1955652862984556545.json、视频生成/文生视频/1950151381917327361.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 3/4 个有
- `ModelSamplingSD3` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `KSamplerAdvanced` —— 2/4 个有
- `MathExpression|pysssss` —— 2/4 个有
- `ModelPatchTorchSettings` —— 2/4 个有
- `WanMoeKSampler` —— 2/4 个有
- `CFGZeroStarAndInit` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 75% |
| Prompt 约束强度(CFG) | 6 | 4 - 10 | 4 | 60% |
| 采样算法 | 1 | 1 - 3 | 4 | 42% |
| 调度器 | 1 | - | 2 | 100% |
| 重绘幅度 | euler | - | 4 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 10，4 个样本
- 采样算法 中位数 1，观测区间 1 - 3，4 个样本，取值分散，一致性仅 42%
- 调度器 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler，4 个样本，一致性 50%
