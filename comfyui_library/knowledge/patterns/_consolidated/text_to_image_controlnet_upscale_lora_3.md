---
name: text_to_image_controlnet_upscale_lora_3
type: Text To Image
frequency: 5
level: strong
coverage: 0.9224
common_nodes: [Anything Everywhere, Anything Everywhere3, BasicGuider, BasicScheduler, CLIPTextEncode, CR Color Panel, CR Text Concatenate, CR Upscale Image, ControlNetApplySD3, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, Florence2ModelLoader, Florence2Run, FluxGuidance, GetImageSize, Image Batch, Image Overlay, ImageCrop, ImageListToImageBatch, ImageScaleToTotalPixels, ImpactImageBatchToImageList, InspyrenetRembg, InvertMask, KSampler, KSamplerSelect, LoadImage, LoraLoader, LyingSigmaSampler, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, StringFunction|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed, easy clearCacheAll, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/【人物四视图】多角度人物一致性 TPP放大4K超清+自动裁剪v1.0_1919277430182182913.json, 图片生成/图生图/【人物四视图】多角度人物一致性_1919389223948845058.json, 图片生成/图生图/【人物四视图】多角度人物一致性创建不同视角IP+4K超清+自动裁剪_1917823447202992130.json, 图片生成/图生图/图生四视图_1920656787886768130.json, 图片生成/图生图/图生四视图_1925144697353007106.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_lora_3

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/【人物四视图】多角度人物一致性 TPP放大4K超清+自动裁剪v1.0_1919277430182182913.json、图片生成/图生图/【人物四视图】多角度人物一致性_1919389223948845058.json、图片生成/图生图/【人物四视图】多角度人物一致性创建不同视角IP+4K超清+自动裁剪_1917823447202992130.json、图片生成/图生图/图生四视图_1920656787886768130.json、图片生成/图生图/图生四视图_1925144697353007106.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `Anything Everywhere`
- `Anything Everywhere3`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Color Panel`
- `CR Text Concatenate`
- `CR Upscale Image`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `GetImageSize`
- `Image Batch`
- `Image Overlay`
- `ImageCrop`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImpactImageBatchToImageList`
- `InspyrenetRembg`
- `InvertMask`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `LyingSigmaSampler`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `ETN_Translate` —— 3/5 个有
- `ArgosTranslateTextNode` —— 1/5 个有
- `SDVN Translate` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | 0.7 - 0.7 | 5 | 100% |
| 宽度 | 512 | 512 - 512 | 5 | 100% |
| 高度 | 512 | 512 - 512 | 5 | 100% |
| 采样步数 | 25 | 25 - 25 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | deis | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 模型强度 | 0.8 | 0.8 - 0.8 | 5 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.7，观测区间 0.7 - 0.7，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，5 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 deis，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 0.8，5 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
