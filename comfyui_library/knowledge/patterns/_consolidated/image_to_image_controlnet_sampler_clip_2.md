---
name: image_to_image_controlnet_sampler_clip_2
type: Image To Image
frequency: 10
level: moderate
coverage: 0.791
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CLIPTextEncodeFlux, CR Latent Batch Size, CR Text Concatenate, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoaderAdvanced, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), Joy_caption_two, Joy_caption_two_load, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RH_Translator, SaveImage, SetUnionControlNetType, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/FLUX 扩图细节优化加强版_2066053168391352321.json, 图片生成/图生图/Kontext+WAN2.1-FusionX +Flux图片修复+增强细节_1955414929416208386.json, 图片生成/图生图/Kontext+WAN2.1-FusionX +Flux图片修复+增强细节_1957737435725754369.json, 图片生成/图生图/KontextFusionXFlux高清修复洗图修复_2059045631867580418.json, 图片生成/图生图/扩图 + FLUX细节修复 - 扩图优化加强版_1945021612662116353.json, 图片生成/图生图/高清修复+洗图 Kontext+FusionX +Flux_1953400917112573953.json, 图片生成/图生图/高清修复+洗图 Kontext+FusionX +Flux究极修复-部分改变细节_1989899329307594753.json, 图片生成/图生图/高清修复+洗图 Kontext+FusionX +Flux究极修复_1950179546534469633.json, 图片生成/图生图/高清修复+洗图_Kontext+FusionX_+Flux究极修复_2076149697252782082.json, 图片生成/文生图/谷歌香蕉+保持原始画面比例扩图_1960893711712497665.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_2

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/FLUX 扩图细节优化加强版_2066053168391352321.json、图片生成/图生图/Kontext+WAN2.1-FusionX +Flux图片修复+增强细节_1955414929416208386.json、图片生成/图生图/Kontext+WAN2.1-FusionX +Flux图片修复+增强细节_1957737435725754369.json、图片生成/图生图/KontextFusionXFlux高清修复洗图修复_2059045631867580418.json、图片生成/图生图/扩图 + FLUX细节修复 - 扩图优化加强版_1945021612662116353.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 10 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `CR Latent Batch Size`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoaderAdvanced`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `RH_Translator`
- `SaveImage`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 7/10 个有
- `Float` —— 7/10 个有
- `ImageSharpen` —— 7/10 个有
- `ReferenceLatent` —— 7/10 个有
- `Text Multiline` —— 7/10 个有
- `DifferentialDiffusion` —— 3/10 个有
- `Fast Groups Bypasser (rgthree)` —— 3/10 个有
- `GrowMaskWithBlur` —— 3/10 个有
- `ImageCompositeMasked` —— 3/10 个有
- `ImagePadForOutpaint` —— 3/10 个有
- `InpaintModelConditioning` —— 3/10 个有
- `LoraLoader` —— 3/10 个有
- `MaskPreview+` —— 3/10 个有
- `NunchakuFluxDiTLoader` —— 3/10 个有
- `Primitive float [Crystools]` —— 3/10 个有
- `GetImageSize` —— 1/10 个有
- `GetNode` —— 1/10 个有
- `Int` —— 1/10 个有
- `LoadImagesFromURL` —— 1/10 个有
- `MathExpression_UTK` —— 1/10 个有
- `MaxNode` —— 1/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有
- `RH_Nano_Banana_Image2Image` —— 1/10 个有
- `SetNode` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | 0.5 - 0.7 | 10 | 86% |
| 采样步数 | 20 | 20 - 20 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 80% |
| 调度器 | simple | - | 10 | 50% |
| 重绘幅度 | 1 | 0.1 - 1 | 10 | 53% |
| LoRA 模型强度 | 0.2 | 0.2 - 0.6 | 3 | 43% |
| LoRA 文本强度 | 0.2 | 0.2 - 0.6 | 3 | 43% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.7，观测区间 0.5 - 0.7，10 个样本，取值集中（一致性 86%）
- 采样步数 中位数 20，观测区间 20 - 20，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 80%
- 调度器 最常用 simple，10 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.1 - 1，10 个样本
- LoRA 模型强度 中位数 0.2，观测区间 0.2 - 0.6，3 个样本，取值分散，一致性仅 43%
- LoRA 文本强度 中位数 0.2，观测区间 0.2 - 0.6，3 个样本，取值分散，一致性仅 43%
