---
name: image_to_image_lora_sampler_clip_115
type: Image To Image
frequency: 3
level: moderate
coverage: 0.921333
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, ImageConcanate, ImpactInt, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewAny, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/洗图_2035019832340516866.json, 图片生成/图生图/美女批量洗图反推提示词(z-image最新模型）(1)_2007282608924790785.json, 图片生成/图生图/美女洗图美女生成(zimage最新模型）带lora版_2007278029894062082.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_115

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/洗图_2035019832340516866.json、图片生成/图生图/美女批量洗图反推提示词(z-image最新模型）(1)_2007282608924790785.json、图片生成/图生图/美女洗图美女生成(zimage最新模型）带lora版_2007278029894062082.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `ImageConcanate`
- `ImpactInt`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DuckHideNode` —— 1/3 个有
- `ImageBatchToList` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RHBatchImages:` —— 1/3 个有
- `RHUploadZip` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 3 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
