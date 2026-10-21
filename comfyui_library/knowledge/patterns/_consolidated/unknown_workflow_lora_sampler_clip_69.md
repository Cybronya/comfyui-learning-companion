---
name: unknown_workflow_lora_sampler_clip_69
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7664
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: PurgeVRAM V2, LayerUtility: ImageReel, LayerUtility: ImageReelComposit]
members: [图片生成/文生图/1959972997622870017.json, 图片生成/文生图/1964982995616677890.json, 图片生成/文生图/1966026218137096193.json, 图片生成/文生图/1970348297275777025.json, 图片生成/文生图/Qwen-image 文生图lora版-极致美感_1991719726550298625.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_69

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1959972997622870017.json、图片生成/文生图/1964982995616677890.json、图片生成/文生图/1966026218137096193.json、图片生成/文生图/1970348297275777025.json、图片生成/文生图/Qwen-image 文生图lora版-极致美感_1991719726550298625.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageReel` —— 4/5 个有
- `LayerUtility: ImageReelComposit` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `JjkText` —— 2/5 个有
- `LayerUtility: PurgeVRAM V2` —— 2/5 个有
- `NunchakuQwenImageDiTLoader` —— 2/5 个有
- `EnhancedLoadDiffusionModel` —— 1/5 个有
- `ImageCombine` —— 1/5 个有
- `LoadImageMW` —— 1/5 个有
- `Lora Loader Stack (rgthree)` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 8 - 30 | 5 | 63% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 5 | 61% |
| 采样算法 | euler_ancestral | - | 5 | 60% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 8 - 30，5 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，5 个样本
- 采样算法 最常用 euler_ancestral，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM V2、LayerUtility: ImageReel、LayerUtility: ImageReelComposit
