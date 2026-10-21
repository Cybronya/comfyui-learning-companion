---
name: unknown_workflow_clip_unet_vae_8
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8986
common_nodes: [CLIPLoader, CLIPTextEncode, ModelSamplingSD3, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: PurgeVRAM, CR Image Size]
members: [图片生成/文生图/1950509671901810689.json, 图片生成/文生图/1953829480836026370.json, 图片生成/文生图/1956245195178344449.json, 图片生成/文生图/1960368358069776385.json, 图片生成/文生图/文生图热巴_2076853328952250370.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_8

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1950509671901810689.json、图片生成/文生图/1953829480836026370.json、图片生成/文生图/1956245195178344449.json、图片生成/文生图/1960368358069776385.json、图片生成/文生图/文生图热巴_2076853328952250370.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ModelSamplingSD3`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/5 个有
- `EmptyHunyuanLatentVideo` —— 3/5 个有
- `KSamplerAdvanced` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `EmptyLatentImage` —— 2/5 个有
- `KSampler` —— 2/5 个有
- `CR Image Size` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `PreviewAny` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 40% |
| Prompt 约束强度(CFG) | 20 | 1 - 20 | 5 | 25% |
| 采样算法 | 3.5 | 3.5 - 8 | 3 | 58% |
| 调度器 | euler | - | 5 | 40% |
| 重绘幅度 | simple | - | 5 | 40% |
| 宽度 | 1064 | - | 2 | 80% |
| 高度 | 600 | - | 2 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 40%
- Prompt 约束强度(CFG) 中位数 20，观测区间 1 - 20，5 个样本，取值分散，一致性仅 25%
- 采样算法 中位数 3.5，观测区间 3.5 - 8，3 个样本
- 调度器 最常用 euler，5 个样本，一致性 40%
- 重绘幅度 最常用 simple，5 个样本，一致性 40%
- 宽度 中位数 1064，样本不足，未给区间，2 个样本
- 高度 中位数 600，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM、CR Image Size
