---
name: image_to_image_lora_sampler_checkpoint_10
type: Image To Image
frequency: 3
level: strong
coverage: 0.845333
common_nodes: [BasicScheduler, CFGNorm, CLIPLoader, CheckpointLoaderSimple, DetailDaemonSamplerNode, Image Comparer (rgthree), ImageColorMatch+, ImageScaleToTotalPixelsX, KSampler, KSamplerSelect, LayerMask: MaskGrow, LayerUtility: ColorImage V2, LayerUtility: ImageBlend, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PainterFluxImageEdit, PreviewImage, SamplerCustom, SaveImage, Seed (rgthree), TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy ifElse, easy int, easy positive]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2klein产品融合人物场景融合_2057455216148176897.json, 图片生成/图生图/Flux2klein产品融合人物场景融合_2062023682289135617.json, 平台全量/firered-image-edit-1.1-flux2-klein-模特与产品互动_2050753855205453826.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_checkpoint_10

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux2klein产品融合人物场景融合_2057455216148176897.json、图片生成/图生图/Flux2klein产品融合人物场景融合_2062023682289135617.json、平台全量/firered-image-edit-1.1-flux2-klein-模特与产品互动_2050753855205453826.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CFGNorm`
- `CLIPLoader`
- `CheckpointLoaderSimple`
- `DetailDaemonSamplerNode`
- `Image Comparer (rgthree)`
- `ImageColorMatch+`
- `ImageScaleToTotalPixelsX`
- `KSampler`
- `KSamplerSelect`
- `LayerMask: MaskGrow`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PainterFluxImageEdit`
- `PreviewImage`
- `SamplerCustom`
- `SaveImage`
- `Seed (rgthree)`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy ifElse`
- `easy int`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `Int` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
