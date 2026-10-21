---
name: image_to_image_lora_sampler_unet_7
type: Image To Image
frequency: 7
level: moderate
coverage: 0.833429
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/图生图/2003636475113684993.json, 图片生成/图生图/2004105975781072898.json, 图片生成/图生图/2008133174475366401.json, 图片生成/图生图/2034603108478754818.json, 图片生成/文生图/Qwen Edit 2511 图片去水印 全节点注释_2077810588885020674.json, 图片生成/文生图/Qwen Image Edit 2511-三图编辑-圣诞节快乐_2003966404120461313.json, 视频生成/文生视频/QwenEdit 2511（FH修复油腻感模型）_2004948756900573185.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_7

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/2003636475113684993.json、图片生成/图生图/2004105975781072898.json、图片生成/图生图/2008133174475366401.json、图片生成/图生图/2034603108478754818.json、图片生成/文生图/Qwen Edit 2511 图片去水印 全节点注释_2077810588885020674.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 6/7 个有
- `ImageScaleToTotalPixels` —— 6/7 个有
- `CR Text` —— 5/7 个有
- `ImageConcanate` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `EmptyImage` —— 1/7 个有
- `Int` —— 1/7 个有
- `LayerUtility: ImageReel` —— 1/7 个有
- `LayerUtility: ImageReelComposit` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `ReferenceLatent` —— 1/7 个有
- `TwoWaySwitch` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 7 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 7 | 69% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、LayerUtility: ImageScaleByAspectRatio V2
