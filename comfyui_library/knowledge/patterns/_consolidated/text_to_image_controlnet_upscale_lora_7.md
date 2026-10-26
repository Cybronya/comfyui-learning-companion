---
name: text_to_image_controlnet_upscale_lora_7
type: Text To Image
frequency: 3
level: strong
coverage: 0.59
common_nodes: [AIO_Preprocessor, BRIA_RMBG_ModelLoader_Zho, BRIA_RMBG_Zho, BrushNet, BrushNetLoader, CLIPSetLastLayer, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, GetNode, GrowMask, ImageRGBA2RGB, ImageResize+, ImageUpscaleWithModel, ImpactDilateMask, InvertMask, JjkText, KSampler, LoadImage, LoraLoader, PreviewImage, RepeatLatentBatch, SaveImage, SetNode, TextCombinerSix, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, WD14Tagger|pysssss, preview_mask]
problems: []
missing: []
members: [图片生成/图生图/室内设计一键装修毛坯房_2018218567396761601.json, 图片生成/图生图/室内设计线稿图上色_1988176105720954882.json, 图片生成/图生图/室内设计线稿图上色_2028633832232062978.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_lora_7

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/室内设计一键装修毛坯房_2018218567396761601.json、图片生成/图生图/室内设计线稿图上色_1988176105720954882.json、图片生成/图生图/室内设计线稿图上色_2028633832232062978.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 3 个 workflow 都包含：
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
- `IPAdapter` —— 1/3 个有
- `IPAdapterUnifiedLoader` —— 1/3 个有
- `ImageBlend` —— 1/3 个有
- `ImageResizeKJ` —— 1/3 个有
- `easy positive` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.35 | 0.35 - 0.35 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 7 | 7 - 7 | 3 | 100% |
| 采样算法 | dpmpp_2m | - | 3 | 100% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 0.5 | 0.4 - 0.5 | 3 | 90% |
| ControlNet 权重 | 0.7 | 0.7 - 1 | 3 | 82% |
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.35，观测区间 0.35 - 0.35，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 7 - 7，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 100%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 0.5，观测区间 0.4 - 0.5，3 个样本，取值集中（一致性 90%）
- ControlNet 权重 中位数 0.7，观测区间 0.7 - 1，3 个样本，取值集中（一致性 82%）
- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
