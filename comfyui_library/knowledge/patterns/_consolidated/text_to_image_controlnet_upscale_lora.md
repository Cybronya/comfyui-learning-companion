---
name: text_to_image_controlnet_upscale_lora
type: Text To Image
frequency: 10
level: strong
coverage: 0.6306
common_nodes: [AIO_Preprocessor, BRIA_RMBG_ModelLoader_Zho, BRIA_RMBG_Zho, BrushNet, BrushNetLoader, CLIPSetLastLayer, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, GetNode, GrowMask, ImageRGBA2RGB, ImageResize+, ImageUpscaleWithModel, ImpactDilateMask, InvertMask, JjkText, KSampler, LoadImage, LoraLoader, PreviewImage, RepeatLatentBatch, SaveImage, SetNode, TextCombinerSix, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, WD14Tagger|pysssss, preview_mask]
problems: []
missing: []
members: [图片生成/图生图/室内设计一键装修毛坯房_2018218567396761601.json, 图片生成/图生图/室内设计线稿图上色_1988176105720954882.json, 图片生成/图生图/室内设计线稿图上色_2028633832232062978.json, 平台全量/【家装风格变换】基于参考图的室内装修设计_1821735880129163265.json, 平台全量/室内设计一键装修毛坯房_1880173363489566721.json, 平台全量/室内设计线稿图上色_1816447938980732930.json, 平台全量/室内设计线稿图上色_1818846394521399298.json, 平台全量/室内设计风格切换_1813806235933147138.json, 平台全量/服装彩稿转换_1812778298805510146.json, 平台全量/服装线稿上色_1812777408972906497.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_lora

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/室内设计一键装修毛坯房_2018218567396761601.json、图片生成/图生图/室内设计线稿图上色_1988176105720954882.json、图片生成/图生图/室内设计线稿图上色_2028633832232062978.json、平台全量/【家装风格变换】基于参考图的室内装修设计_1821735880129163265.json、平台全量/室内设计一键装修毛坯房_1880173363489566721.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 10 个 workflow 都包含：
- `AIO_Preprocessor`
- `BRIA_RMBG_ModelLoader_Zho`
- `BRIA_RMBG_Zho`
- `BrushNet`
- `BrushNetLoader`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `GetNode`
- `GrowMask`
- `ImageRGBA2RGB`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `ImpactDilateMask`
- `InvertMask`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `RepeatLatentBatch`
- `SaveImage`
- `SetNode`
- `TextCombinerSix`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `WD14Tagger|pysssss`
- `preview_mask`

**可变部分**（部分 workflow 才有）：
- `IPAdapter` —— 3/10 个有
- `IPAdapterUnifiedLoader` —— 3/10 个有
- `ImageBlend` —— 3/10 个有
- `ImageResizeKJ` —— 3/10 个有
- `easy positive` —— 2/10 个有
- `AV_VAELoader` —— 1/10 个有
- `Label (rgthree)` —— 1/10 个有
- `Mask Gaussian Region` —— 1/10 个有
- `Scribble_XDoG_Preprocessor` —— 1/10 个有
- `easy getNode` —— 1/10 个有
- `easy setNode` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.35 | 0.15 - 0.7 | 10 | 66% |
| LoRA 文本强度 | 1 | 1 - 1 | 10 | 100% |
| 采样步数 | 20 | 20 - 20 | 10 | 100% |
| Prompt 约束强度(CFG) | 7 | 7 - 7 | 10 | 100% |
| 采样算法 | dpmpp_2m | - | 10 | 100% |
| 调度器 | karras | - | 10 | 100% |
| 重绘幅度 | 0.5 | 0.38 - 0.7 | 10 | 82% |
| ControlNet 权重 | 0.7 | 0.4 - 1 | 10 | 78% |
| 宽度 | 512 | 512 - 512 | 10 | 100% |
| 高度 | 512 | 512 - 512 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.35，观测区间 0.15 - 0.7，10 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 20，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 7 - 7，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，10 个样本，一致性 100%
- 调度器 最常用 karras，10 个样本，一致性 100%
- 重绘幅度 中位数 0.5，观测区间 0.38 - 0.7，10 个样本，取值集中（一致性 82%）
- ControlNet 权重 中位数 0.7，观测区间 0.4 - 1，10 个样本
- 宽度 中位数 512，观测区间 512 - 512，10 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，10 个样本，取值集中（一致性 100%）
