---
name: text_to_image_inpaint_lora_sampler_5
type: Text To Image
frequency: 3
level: strong
coverage: 0.848667
common_nodes: [CLIPTextEncode, CLIPTextEncodeFlux, CLIPVisionLoader, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, Fast Groups Muter (rgthree), GetImageSize+, GrowMaskWithBlur, ImageConcanate, ImageCrop+, ImageToMask, ImpactConditionalBranch, InpaintCrop, InpaintModelConditioning, InpaintStitch, InspyrenetRembg, Joy_caption_two, Joy_caption_two_load, KSampler, LayerMask: SegmentAnythingUltra V2, LayerUtility: ColorImage, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskPreview+, MaskToImage, PreviewImage, ReduxAdvanced, Replace Text _O, SaveImage, ShowText|pysssss, StyleModelLoader, TextInput_, UNETLoader, VAEDecode, VAELoader, easy imageColorMatch]
problems: []
missing: []
members: [平台全量/项链上身_1931966537824186369.json, 平台全量/项链首饰模特展示，搭配主页IC-LoRA_1893739639084089346.json, 平台全量/项链首饰模特生成，电商场景_1896732148869341185.json]
source: knowledge_consolidation
---

# text_to_image_inpaint_lora_sampler_5

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/项链上身_1931966537824186369.json、平台全量/项链首饰模特展示，搭配主页IC-LoRA_1893739639084089346.json、平台全量/项链首饰模特生成，电商场景_1896732148869341185.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Muter (rgthree)`
- `GetImageSize+`
- `GrowMaskWithBlur`
- `ImageConcanate`
- `ImageCrop+`
- `ImageToMask`
- `ImpactConditionalBranch`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `InspyrenetRembg`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ColorImage`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `MaskToImage`
- `PreviewImage`
- `ReduxAdvanced`
- `Replace Text _O`
- `SaveImage`
- `ShowText|pysssss`
- `StyleModelLoader`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageColorMatch`

**可变部分**（部分 workflow 才有）：
- `DifferentialDiffusion` —— 1/3 个有
- `FluxGuidance` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `Note _O` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
