---
name: unknown_workflow_sampler_clip_unet_410
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/高质量双采样_RH版_v1_2019943536841461761.json, 图片生成/文生图/黑兽ZImage+LoRA文生图（推荐）_2026928720652541954.json, 图片生成/文生图/（贞贞版4图版）Qwen 2512 Kook千问美人+真实幻想+极致真实文生图V1_2008746844083462145.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_410

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/高质量双采样_RH版_v1_2019943536841461761.json、图片生成/文生图/黑兽ZImage+LoRA文生图（推荐）_2026928720652541954.json、图片生成/文生图/（贞贞版4图版）Qwen 2512 Kook千问美人+真实幻想+极致真实文生图V1_2008746844083462145.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `DuckHideNode` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `VAEEncode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 采样步数 | 8 | 4 - 8 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_2m | - | 3 | 33% |
| 调度器 | normal | - | 3 | 33% |
| 重绘幅度 | 1 | 0.4 - 1 | 3 | 65% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2m，3 个样本，一致性 33%
- 调度器 最常用 normal，3 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，3 个样本
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
