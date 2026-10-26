---
name: unknown_workflow_lora_sampler_clip_101
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9036
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Klein 抠图 白底 透明材质_2076477973649256450.json, 图片生成/图生图/Klein用方框进行图像增改删_2042840062538289154.json, 图片生成/图生图/动漫转写实真人快速版_2042420411459182593.json, 图片生成/图生图/打光_溶图_改透视_提升画质_100%不偏移_细节迁移_klein_9b_2091710740364349442.json, 图片生成/图生图/打光_溶图_改透视_提升画质_100%不偏移_细节迁移_klein_9b_2091842911334912001.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_101

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Klein 抠图 白底 透明材质_2076477973649256450.json、图片生成/图生图/Klein用方框进行图像增改删_2042840062538289154.json、图片生成/图生图/动漫转写实真人快速版_2042420411459182593.json、图片生成/图生图/打光_溶图_改透视_提升画质_100%不偏移_细节迁移_klein_9b_2091710740364349442.json、图片生成/图生图/打光_溶图_改透视_提升画质_100%不偏移_细节迁移_klein_9b_2091842911334912001.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `ImageScaleToTotalPixels` —— 3/5 个有
- `LayerMask: BiRefNetUltraV2` —— 3/5 个有
- `LayerMask: LoadBiRefNetModelV2` —— 3/5 个有
- `easy seed` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `ImageBatchConcatNode` —— 2/5 个有
- `Int` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `XinbaoPintu` —— 2/5 个有
- `easy imageConcat` —— 2/5 个有
- `easy imageDetailTransfer` —— 2/5 个有
- `GrowMaskWithBlur` —— 1/5 个有
- `JoinImageWithAlpha` —— 1/5 个有
- `LayerUtility: ImageCombineAlpha` —— 1/5 个有
- `Mask Invert` —— 1/5 个有
- `SDMatteApply` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
