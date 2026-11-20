---
name: text_to_image_controlnet_upscale_lora_3
type: Text To Image
frequency: 6
level: strong
coverage: 0.8365
common_nodes: [AIO_Preprocessor, Anything Everywhere, Anything Everywhere3, BasicGuider, BasicScheduler, CLIPTextEncode, CR Float To Integer, CR Text, CR Text Concatenate, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, FloatSlider, FluxGuidance, GrowMask, GrowMaskWithBlur, Image Comparer (rgthree), ImageAndMaskPreview, ImageCompositeMasked, ImageResizeKJ, ImageToMask, ImageUpscaleWithModel, InvertMask, KSampler, KSamplerSelect, LayerMask: MaskPreview, LayerMask: SegmentAnythingUltra V2, LayerUtility: CropByMask V2, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LayerUtility: RestoreCropBox, LineArtPreprocessor, LoadImage, LoraLoader, MaskBlur+, MaskComposite, MaskPreview+, MaskToImage, Miaoshouai_Tagger, PortraitMaster_中文版, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetLatentNoiseMask, SetUnionControlNetType, ShowText|pysssss, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy anythingIndexSwitch, easy cleanGpuUsed, easy imageRemBg, easy imageSize, easy promptReplace]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AI_助力跨境电商变现！_模特替换肤色_2115430793211367425.json, 图片生成/图生图/AI_助力跨境电商变现！_模特替换肤色_2115656248908673025.json, 图片生成/图生图/更换人物+更换肤色---跨境电商专用！_1978068538311192578.json, 图片生成/图生图/项链_1942390570528485377.json, 平台全量/AI 助力跨境电商变现！ 模特替换肤色_1922224585247490049.json, 平台全量/换肤色  跨境电商换模特调节肤色 Kontext万能人像调节肤色调节一键换脸质感提升_1998232363761065986.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_lora_3

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/AI_助力跨境电商变现！_模特替换肤色_2115430793211367425.json、图片生成/图生图/AI_助力跨境电商变现！_模特替换肤色_2115656248908673025.json、图片生成/图生图/更换人物+更换肤色---跨境电商专用！_1978068538311192578.json、图片生成/图生图/项链_1942390570528485377.json、平台全量/AI 助力跨境电商变现！ 模特替换肤色_1922224585247490049.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
- `AIO_Preprocessor`
- `Anything Everywhere`
- `Anything Everywhere3`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Float To Integer`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FloatSlider`
- `FluxGuidance`
- `GrowMask`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImageCompositeMasked`
- `ImageResizeKJ`
- `ImageToMask`
- `ImageUpscaleWithModel`
- `InvertMask`
- `KSampler`
- `KSamplerSelect`
- `LayerMask: MaskPreview`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageScaleByAspectRatio`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: RestoreCropBox`
- `LineArtPreprocessor`
- `LoadImage`
- `LoraLoader`
- `MaskBlur+`
- `MaskComposite`
- `MaskPreview+`
- `MaskToImage`
- `Miaoshouai_Tagger`
- `PortraitMaster_中文版`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetLatentNoiseMask`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy cleanGpuUsed`
- `easy imageRemBg`
- `easy imageSize`
- `easy promptReplace`

**可变部分**（部分 workflow 才有）：
- `DetailDaemonSamplerNode` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有
- `LayerMask: PersonMaskUltra V2` —— 5/6 个有
- `LayerMask: SegformerB2ClothesUltra` —— 5/6 个有
- `ModelSamplingFlux` —— 3/6 个有
- `NunchakuFluxDiTLoader` —— 3/6 个有
- `NunchakuFluxLoraLoader` —— 3/6 个有
- `CR Value` —— 1/6 个有
- `DeepTranslatorTextNode` —— 1/6 个有
- `RHHiddenNodes` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 768 | 6 | 100% |
| 高度 | 1024 | 1024 - 1024 | 6 | 100% |
| ControlNet 权重 | 0.5 | 0.5 - 0.5 | 6 | 100% |
| 采样步数 | 8 | 8 - 8 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 768，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.5，观测区间 0.5 - 0.5，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
