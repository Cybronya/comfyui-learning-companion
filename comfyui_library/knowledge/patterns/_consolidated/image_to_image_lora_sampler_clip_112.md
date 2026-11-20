---
name: image_to_image_lora_sampler_clip_112
type: Image To Image
frequency: 4
level: strong
coverage: 0.864
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, ImageConcanate, ImageScaleToTotalPixels, KSampler, LayerMask: TransparentBackgroundUltra, LayerUtility: TextBox, LoadImage, LoraLoaderModelOnly, NunchakuFluxDiTLoader, PreviewImage, RH_Captioner, ReferenceLatent, SaveImage, ShowText|pysssss, Text Concatenate, VAEDecode, VAEEncode, VAELoader, easy promptReplace]
problems: []
missing: []
members: [图片生成/图生图/多图融合kontext_可编辑版_1969422698864668673.json, 图片生成/图生图/多图融合终极版 kontext dev 全面优化加速持续更新_1939927487025422337.json, 图片生成/图生图/最强Flux-Kontext 融合，背景替换，虚拟合影+放大_1948190652130557954.json, 平台全量/单图编辑终极版 kontext dev 全面优化加速持续更新_1939743239899680769.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_112

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/多图融合kontext_可编辑版_1969422698864668673.json、图片生成/图生图/多图融合终极版 kontext dev 全面优化加速持续更新_1939927487025422337.json、图片生成/图生图/最强Flux-Kontext 融合，背景替换，虚拟合影+放大_1948190652130557954.json、平台全量/单图编辑终极版 kontext dev 全面优化加速持续更新_1939743239899680769.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageConcanate`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerMask: TransparentBackgroundUltra`
- `LayerUtility: TextBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `NunchakuFluxDiTLoader`
- `PreviewImage`
- `RH_Captioner`
- `ReferenceLatent`
- `SaveImage`
- `ShowText|pysssss`
- `Text Concatenate`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptReplace`

**可变部分**（部分 workflow 才有）：
- `Compositor3` —— 3/4 个有
- `CompositorConfig3` —— 3/4 个有
- `GetImageSize` —— 3/4 个有
- `ImageConcatMulti` —— 3/4 个有
- `LayerUtility: SaveImagePlus` —— 3/4 个有
- `AddLabel` —— 1/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `FastCanvas` —— 1/4 个有
- `FastCanvasTool` —— 1/4 个有
- `Images to RGB` —— 1/4 个有
- `LayerUtility: ColorImage V2` —— 1/4 个有
- `LayerUtility: ImageCombineAlpha` —— 1/4 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/4 个有
- `RH_Translator` —— 1/4 个有
- `easy ifElse` —— 1/4 个有
- `easy isMaskEmpty` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
