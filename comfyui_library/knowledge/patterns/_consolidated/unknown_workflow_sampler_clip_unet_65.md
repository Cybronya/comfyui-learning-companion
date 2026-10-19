---
name: unknown_workflow_sampler_clip_unet_65
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.85725
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, ModelSamplingSD3, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [String Literal, easy seed, LayerUtility: PurgeVRAM, CR Image Size]
members: [图片生成/文生图/1950849465034940417.json, 图片生成/文生图/1952444989798330370.json, 图片生成/文生图/1956245195178344449.json, 图片生成/文生图/1960368358069776385.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_65

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1950849465034940417.json、图片生成/文生图/1952444989798330370.json、图片生成/文生图/1956245195178344449.json、图片生成/文生图/1960368358069776385.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `ModelSamplingSD3`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `CR Image Size` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有
- `String Literal` —— 1/4 个有
- `WanVideoNAG` —— 1/4 个有
- `easy seed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5.5 | 4 - 20 | 4 | 25% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 4 | 33% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 0.75 | 0.3 - 1 | 4 | 56% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5.5，观测区间 4 - 20，4 个样本，取值分散，一致性仅 25%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，4 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 0.75，观测区间 0.3 - 1，4 个样本
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：String Literal、easy seed、LayerUtility: PurgeVRAM、CR Image Size
