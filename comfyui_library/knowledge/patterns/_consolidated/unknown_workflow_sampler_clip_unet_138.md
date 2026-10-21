---
name: unknown_workflow_sampler_clip_unet_138
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9396
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSampler, LoadImage, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1950857599925288961.json, 视频生成/文生视频/1954455270426603522.json, 视频生成/文生视频/1950005929661087745.json, 视频生成/文生视频/1950178934676701186.json, 视频生成/文生视频/1950766450359324674.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_138

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1950857599925288961.json、视频生成/文生视频/1954455270426603522.json、视频生成/文生视频/1950005929661087745.json、视频生成/文生视频/1950178934676701186.json、视频生成/文生视频/1950766450359324674.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Wan22ImageToVideoLatent` —— 4/5 个有
- `CFGZeroStar` —— 1/5 个有
- `PatchModelPatcherOrder` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有
- `TrimVideoLatent` —— 1/5 个有
- `VHS_VideoCombine` —— 1/5 个有
- `WanVaceToVideo` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 20 | 5 | 78% |
| Prompt 约束强度(CFG) | 5 | 1 - 5 | 5 | 62% |
| 采样算法 | uni_pc | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 5，观测区间 1 - 5，5 个样本
- 采样算法 最常用 uni_pc，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
