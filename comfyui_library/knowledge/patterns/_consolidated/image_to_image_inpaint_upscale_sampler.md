---
name: image_to_image_inpaint_upscale_sampler
type: Image To Image
frequency: 2
level: weak
coverage: 0.729
common_nodes: [Anything Everywhere, Anything Everywhere3, CLIPTextEncode, CR Aspect Ratio, CheckpointLoaderSimple, ConditioningCombine, ConditioningConcat, DetailerForEachDebug, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), INPAINT_ExpandMask, Image Comparer (rgthree), ImageUpscaleWithModel, ImpactConditionalBranch, KSampler, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio, LoadImage, MaskToSEGS, PreviewImage, Prompts Everywhere, SAMLoader, SaveImage, Seed_, UpscaleModelLoader, VAEDecode, VAEEncode, easy setNode]
problems: []
missing: [CR Aspect Ratio, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), LayerUtility: ImageScaleByAspectRatio, easy setNode, LayerMask: MaskPreview, Prompts Everywhere]
members: [图片生成/文生图/1958386608041050113.json, "图片生成/文生图/wai文生图+4K高清修复,手部修复_2025961446353408001.json"]
source: knowledge_consolidation
---

# image_to_image_inpaint_upscale_sampler

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1958386608041050113.json、图片生成/文生图/wai文生图+4K高清修复,手部修复_2025961446353408001.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `Anything Everywhere3`
- `CLIPTextEncode`
- `CR Aspect Ratio`
- `CheckpointLoaderSimple`
- `ConditioningCombine`
- `ConditioningConcat`
- `DetailerForEachDebug`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `INPAINT_ExpandMask`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `ImpactConditionalBranch`
- `KSampler`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio`
- `LoadImage`
- `MaskToSEGS`
- `PreviewImage`
- `Prompts Everywhere`
- `SAMLoader`
- `SaveImage`
- `Seed_`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `CompressImages` —— 1/2 个有
- `LatentUpscaleBy` —— 1/2 个有
- `Lora Loader Stack (rgthree)` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `easy batchAnything` —— 1/2 个有
- `easy forLoopEnd` —— 1/2 个有
- `easy forLoopStart` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 21 | - | 2 | 81% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | karras | - | 2 | 50% |
| 重绘幅度 | 0.4 | - | 2 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 21，样本不足，未给区间，2 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 50%
- 重绘幅度 中位数 0.4，样本不足，未给区间，2 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：CR Aspect Ratio、GroundingDinoModelLoader (segment anything)、GroundingDinoSAMSegment (segment anything)、LayerUtility: ImageScaleByAspectRatio、easy setNode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
