---
name: unknown_workflow_inpaint_lora_sampler_2
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.853
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, CropWithPadInfo, FluxKontextMultiReferenceLatentMethod, GetNode, Image Comparer (rgthree), ImageAndMaskPreview, InpaintStitchImproved, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, PrimitiveStringMultiline, QwenEditOutputExtractor, RHHiddenNodes, SaveImage, SetNode, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, UnetLoaderGGUF, VAEDecode, VAELoader, easy imageConcat, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/万物迁移局部重绘+4K高清+_2094586188085682177.json, 图片生成/图生图/万物迁移局部重绘+4K高清+_2097131655344508929.json, 图片生成/图生图/万物迁移局部重绘+4K高清+_2097230454498881537.json, 图片生成/图生图/万物迁移局部重绘+4K高清_2019308573083312129.json, 图片生成/图生图/万物迁移局部重绘+4K高清_2056986344089542658.json, 图片生成/图生图/万物迁移局部重绘+4K高清_2084074874313728002.json, 图片生成/图生图/万物迁移局部重绘+4K高清_2084537756524564482.json, 图片生成/图生图/万物迁移局部重绘+4K高清_2084903756356997122.json, 图片生成/图生图/万物迁移局部重绘+4K高清_2084995717353000962.json, 图片生成/图生图/万物迁移局部重绘+4K高清_2085203465571229698.json, 图片生成/图生图/万物迁移局部重绘+4K高清_2085207817744642050.json, 图片生成/图生图/万物迁移局部重绘+4K高清_2085888011966959617.json, 图片生成/图生图/万物迁移局部重绘+4K高清_2086649145699422210.json, 图片生成/图生图/万物迁移局部重绘+4K高清_2088505371513151490.json, 图片生成/图生图/万物迁移局部重绘+4K高清_2094318355120476161.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_2

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/万物迁移局部重绘+4K高清+_2094586188085682177.json、图片生成/图生图/万物迁移局部重绘+4K高清+_2097131655344508929.json、图片生成/图生图/万物迁移局部重绘+4K高清+_2097230454498881537.json、图片生成/图生图/万物迁移局部重绘+4K高清_2019308573083312129.json、图片生成/图生图/万物迁移局部重绘+4K高清_2056986344089542658.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 15 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `CropWithPadInfo`
- `FluxKontextMultiReferenceLatentMethod`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `InpaintStitchImproved`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `QwenEditOutputExtractor`
- `RHHiddenNodes`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `easy imageConcat`
- `easy int`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | simple | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 simple，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
