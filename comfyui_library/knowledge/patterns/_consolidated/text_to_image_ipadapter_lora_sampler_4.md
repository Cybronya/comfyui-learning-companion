---
name: text_to_image_ipadapter_lora_sampler_4
type: Text To Image
frequency: 3
level: strong
coverage: 0.584
common_nodes: [AV_IPAdapter, Anything Everywhere, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, GetImageSize+, GetNode, ImageBatch, ImageDesaturate+, ImageScaleToMegapixels, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModel, LayerUtility: ImageRemoveAlpha, LoadImage, LoraLoader, MaskToImage, PreviewImage, Prompts Everywhere, SaveImage, Seed Generator, SetNode, ShowText|pysssss, String Literal, VAEDecode, WD14Tagger|pysssss, easy promptConcat, easy promptReplace]
problems: []
missing: []
members: [平台全量/Turn your photo to line drawing style!_1867148737771700225.json, 平台全量/将你的照片一键变成线条画风！_1891521480553877505.json, 平台全量/线绘风格 Turn your photo to line drawing style!_1840703002272288770.json]
source: knowledge_consolidation
---

# text_to_image_ipadapter_lora_sampler_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Turn your photo to line drawing style!_1867148737771700225.json、平台全量/将你的照片一键变成线条画风！_1891521480553877505.json、平台全量/线绘风格 Turn your photo to line drawing style!_1840703002272288770.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 3 个 workflow 都包含：
- `AV_IPAdapter`
- `Anything Everywhere`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `GetImageSize+`
- `GetNode`
- `ImageBatch`
- `ImageDesaturate+`
- `ImageScaleToMegapixels`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModel`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `LoraLoader`
- `MaskToImage`
- `PreviewImage`
- `Prompts Everywhere`
- `SaveImage`
- `Seed Generator`
- `SetNode`
- `ShowText|pysssss`
- `String Literal`
- `VAEDecode`
- `WD14Tagger|pysssss`
- `easy promptConcat`
- `easy promptReplace`

**可变部分**（部分 workflow 才有）：
- `AV_ControlNetPreprocessor` —— 2/3 个有
- `ControlNetApplyAdvanced` —— 2/3 个有
- `ACN_ControlNet++LoaderSingle` —— 1/3 个有
- `ControlNetLoader` —— 1/3 个有
- `workflow/cn` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 5.4 | 5.4 - 5.4 | 3 | 100% |
| 采样算法 | dpmpp_sde | - | 3 | 100% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |
| ControlNet 权重 | 0.65 | - | 2 | 100% |
| LoRA 模型强度 | 0.8 | 0.8 - 0.8 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5.4，观测区间 5.4 - 5.4，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，3 个样本，一致性 100%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.65，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 0.8，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
