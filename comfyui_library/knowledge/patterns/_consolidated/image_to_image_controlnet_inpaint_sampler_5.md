---
name: image_to_image_controlnet_inpaint_sampler_5
type: Image To Image
frequency: 2
level: weak
coverage: 0.828
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CLIPVisionLoader, CR Prompt Text, CR Text Concatenate, ControlNetApplyAdvanced, ControlNetLoader, DifferentialDiffusion, DualCLIPLoader, Florence2ModelLoader, Florence2Run, FluxGuidance, GetImageSize, GetImageSize+, GrowMask, Image Blank, ImageCompositeMasked, ImageScale, InpaintModelConditioning, InvertMask (segment anything), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RMBG, ReduxAdvanced, SaveImage, SetLatentNoiseMask, SetNode, ShowText|pysssss, StyleModelLoader, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux_换背景+参考图打光工作流_1982485690057400322.json, 图片生成/图生图/WH-AI-Studio-FLUX电商产品（人物模特）换背景（文字LOGO不变形）_2022611144027938818.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_sampler_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux_换背景+参考图打光工作流_1982485690057400322.json、图片生成/图生图/WH-AI-Studio-FLUX电商产品（人物模特）换背景（文字LOGO不变形）_2022611144027938818.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
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
- `Anything Everywhere` —— 1/2 个有
- `Anything Everywhere3` —— 1/2 个有
- `BaiduTranslateNode` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `Color (hexadecimal)` —— 1/2 个有
- `DetailTransfer` —— 1/2 个有
- `Float` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ICLightConditioning` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `Int` —— 1/2 个有
- `LayerColor: ColorAdapter` —— 1/2 个有
- `LayerUtility: ExtendCanvas` —— 1/2 个有
- `LoadAndApplyICLightUnet` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `StringConstantMultiline` —— 1/2 个有
- `TeaCache` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy imageConcat` —— 1/2 个有
- `easy promptConcat` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.5 | - | 2 | 100% |
| 采样步数 | 16.5 | - | 2 | 48% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 16.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
