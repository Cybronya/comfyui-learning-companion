---
name: text_to_image_lora_sampler_clip_515
type: Text To Image
frequency: 3
level: strong
coverage: 0.829
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize, GrowMaskWithBlur, Image Comparer (rgthree), ImageResizeKJv2, ImageScale, ImageToMask, Int, JjkText, KSampler, KSamplerSelect, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerUtility: ColorImage V2, LayerUtility: CropByMask V2, LayerUtility: ImageBlendAdvance, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, ManualSigmas, Mask Fill Holes, MathExpression|pysssss, MaxNode, PreviewBridge, PreviewImage, QwenImage21Cache, SamplerCustom, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1 Turbo万物迁移｜一键风格迁移高效出图加速版_2113443918649057281.json, 图片生成/图生图/Qwen image 2.1 turbo万物迁移 风格迁移图像处理工具_2113690855524618241.json, 图片生成/图生图/细节恢复qwen image 2.1 图片清晰度增强方案_2109713939251687425.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_515

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 Turbo万物迁移｜一键风格迁移高效出图加速版_2113443918649057281.json、图片生成/图生图/Qwen image 2.1 turbo万物迁移 风格迁移图像处理工具_2113690855524618241.json、图片生成/图生图/细节恢复qwen image 2.1 图片清晰度增强方案_2109713939251687425.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageResizeKJv2`
- `ImageScale`
- `ImageToMask`
- `Int`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `LayerUtility: ColorImage V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `Mask Fill Holes`
- `MathExpression|pysssss`
- `MaxNode`
- `PreviewBridge`
- `PreviewImage`
- `QwenImage21Cache`
- `SamplerCustom`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageRemoveAlpha` —— 2/3 个有
- `Image Overlay` —— 1/3 个有
- `KuwaharaBlur` —— 1/3 个有
- `LayerFilter: GaussianBlur` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
