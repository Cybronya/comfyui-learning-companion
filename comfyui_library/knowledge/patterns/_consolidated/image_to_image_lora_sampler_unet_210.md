---
name: image_to_image_lora_sampler_unet_210
type: Image To Image
frequency: 3
level: strong
coverage: 0.890333
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, RMBG, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2511-人物姿态迁移工作流_2029439907747336194.json, 平台全量/2511多图工作流（电商产品设计）_2028821522370011137.json, 平台全量/Qwen2511-角色替换极简工作流_2080644410693472258.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_210

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen2511-人物姿态迁移工作流_2029439907747336194.json、平台全量/2511多图工作流（电商产品设计）_2028821522370011137.json、平台全量/Qwen2511-角色替换极简工作流_2080644410693472258.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `RMBG`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 2/3 个有
- `FastCanvas` —— 2/3 个有
- `FastCanvasTool` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `ReferenceLatent` —— 2/3 个有
- `SDPoseOODLoader` —— 2/3 个有
- `SDPoseOODProcessor` —— 2/3 个有
- `Switch any [Crystools]` —— 2/3 个有
- `TTResolutionSelector` —— 2/3 个有
- `YOLOModelLoader` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `DrawMaskOnImage` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `ImageBatchMultiple+` —— 1/3 个有
- `LayerMask: MaskGrow` —— 1/3 个有
- `LayerUtility: ImageBlend` —— 1/3 个有
- `MaskPreview+` —— 1/3 个有
- `easy sam3ImageSegmentation` —— 1/3 个有
- `easy sam3ModelLoader` —— 1/3 个有
- `忽略多组孤海` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
