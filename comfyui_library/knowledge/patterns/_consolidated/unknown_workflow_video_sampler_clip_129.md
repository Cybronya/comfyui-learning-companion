---
name: unknown_workflow_video_sampler_clip_129
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.8894
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/1947883118252408834.json, 视频生成/文生视频/1930553645908021250.json, 视频生成/文生视频/1947317046674624514.json, 视频生成/文生视频/1951970286314926081.json, 视频生成/文生视频/1950680019137941506.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_129

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/1947883118252408834.json、视频生成/文生视频/1930553645908021250.json、视频生成/文生视频/1947317046674624514.json、视频生成/文生视频/1951970286314926081.json、视频生成/文生视频/1950680019137941506.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `Note Plus (mtb)` —— 3/5 个有
- `LoadImageFromUrl` —— 2/5 个有
- `PrimitiveInt` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `SaveAnimatedWEBP` —— 2/5 个有
- `SaveWEBM` —— 1/5 个有
- `UnetLoaderGGUF` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 30 | 5 | 34% |
| Prompt 约束强度(CFG) | 6 | 1 - 6 | 5 | 39% |
| 采样算法 | uni_pc | - | 5 | 60% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 30，5 个样本，取值分散，一致性仅 34%
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 6，5 个样本，取值分散，一致性仅 39%
- 采样算法 最常用 uni_pc，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
