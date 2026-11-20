---
name: image_to_image_controlnet_inpaint_sampler_8
type: Image To Image
frequency: 4
level: strong
coverage: 0.80925
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CLIPVisionLoader, CR Prompt Text, CR Text Concatenate, ControlNetApplyAdvanced, ControlNetLoader, DifferentialDiffusion, DualCLIPLoader, Florence2ModelLoader, Florence2Run, FluxGuidance, GetImageSize, GetImageSize+, GrowMask, Image Blank, ImageCompositeMasked, ImageScale, InpaintModelConditioning, InvertMask (segment anything), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RMBG, ReduxAdvanced, SaveImage, SetLatentNoiseMask, SetNode, ShowText|pysssss, StyleModelLoader, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux_换背景+参考图打光工作流_1982485690057400322.json, 图片生成/图生图/WH-AI-Studio-FLUX电商产品（人物模特）换背景（文字LOGO不变形）_2022611144027938818.json, 平台全量/FLux_换背景_1921587918136344577.json, 平台全量/换背景+打光最新版本2.1_1923310574204014593.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_sampler_8

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux_换背景+参考图打光工作流_1982485690057400322.json、图片生成/图生图/WH-AI-Studio-FLUX电商产品（人物模特）换背景（文字LOGO不变形）_2022611144027938818.json、平台全量/FLux_换背景_1921587918136344577.json、平台全量/换背景+打光最新版本2.1_1923310574204014593.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `CR Text Concatenate`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `GetImageSize`
- `GetImageSize+`
- `GrowMask`
- `Image Blank`
- `ImageCompositeMasked`
- `ImageScale`
- `InpaintModelConditioning`
- `InvertMask (segment anything)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RMBG`
- `ReduxAdvanced`
- `SaveImage`
- `SetLatentNoiseMask`
- `SetNode`
- `ShowText|pysssss`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 2/4 个有
- `Anything Everywhere3` —— 2/4 个有
- `BaiduTranslateNode` —— 2/4 个有
- `CheckpointLoaderSimple` —— 2/4 个有
- `Color (hexadecimal)` —— 2/4 个有
- `DetailTransfer` —— 2/4 个有
- `Float` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `ICLightConditioning` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `Int` —— 2/4 个有
- `LayerColor: ColorAdapter` —— 2/4 个有
- `LayerUtility: ExtendCanvas` —— 2/4 个有
- `LoadAndApplyICLightUnet` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `StringConstantMultiline` —— 2/4 个有
- `TeaCache` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `easy promptConcat` —— 2/4 个有
- `easy imageConcat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.5 | 0.5 - 0.5 | 4 | 100% |
| 采样步数 | 16.5 | 8 - 25 | 4 | 48% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.5，观测区间 0.5 - 0.5，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 16.5，观测区间 8 - 25，4 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
