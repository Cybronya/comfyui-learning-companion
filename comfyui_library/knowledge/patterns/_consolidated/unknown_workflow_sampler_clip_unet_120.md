---
name: unknown_workflow_sampler_clip_unet_120
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.8865
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/超强文生图Z-image-base_2016185060738732034.json, 图片生成/文生图/阿清的AI模特文生图_2000461829648379906.json, 图片生成/文生图/陶器工作流_2071425077450727425.json, 图片生成/文生图/静帧画面工作流_2025778505488801793.json, 图片生成/文生图/黑兽ZImage+LoRA文生图（推荐）_2026928720652541954.json, 图片生成/文生图/（贞贞版）Z-Image-Base 2w2步_2016755186840113154.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_120

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/超强文生图Z-image-base_2016185060738732034.json、图片生成/文生图/阿清的AI模特文生图_2000461829648379906.json、图片生成/文生图/陶器工作流_2071425077450727425.json、图片生成/文生图/静帧画面工作流_2025778505488801793.json、图片生成/文生图/黑兽ZImage+LoRA文生图（推荐）_2026928720652541954.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `CR Text` —— 1/6 个有
- `DuckHideNode` —— 1/6 个有
- `FluxResolutionNode` —— 1/6 个有
- `Image Filter Adjustments` —— 1/6 个有
- `LayerUtility: PurgeVRAM` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 50 | 6 | 35% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 6 | 54% |
| 采样算法 | euler | - | 6 | 67% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 50，6 个样本，取值分散，一致性仅 35%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
