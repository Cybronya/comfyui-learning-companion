---
name: unknown_workflow_video_sampler_clip_176
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.93325
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Wan2.1 T2V 原生文生视频_1947883118252408834.json, 视频生成/文生视频/Wan2.1 T2V 文生视频_1930553645908021250.json, 视频生成/文生视频/Wan2.1 t2V gguf 文生视频_1947317046674624514.json, 视频生成/文生视频/Wan2.2-t2v-rapid-AIO融合模型文生视频+4步快速生成_1951970286314926081.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_176

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/Wan2.1 T2V 原生文生视频_1947883118252408834.json、视频生成/文生视频/Wan2.1 T2V 文生视频_1930553645908021250.json、视频生成/文生视频/Wan2.1 t2V gguf 文生视频_1947317046674624514.json、视频生成/文生视频/Wan2.2-t2v-rapid-AIO融合模型文生视频+4步快速生成_1951970286314926081.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 3/4 个有
- `Note Plus (mtb)` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `LoadImageFromUrl` —— 2/4 个有
- `SaveAnimatedWEBP` —— 2/4 个有
- `PrimitiveInt` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `SaveWEBM` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 4 - 30 | 4 | 49% |
| Prompt 约束强度(CFG) | 6 | 1 - 6 | 4 | 54% |
| 采样算法 | uni_pc | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 4 - 30，4 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 6，4 个样本
- 采样算法 最常用 uni_pc，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
