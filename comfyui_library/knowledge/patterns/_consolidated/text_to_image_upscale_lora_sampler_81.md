---
name: text_to_image_upscale_lora_sampler_81
type: Text To Image
frequency: 3
level: strong
coverage: 0.71
common_nodes: [ApplyFBCacheOnModel, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPTextEncodeFlux, CR SDXL Aspect Ratio, DualCLIPLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), ImageListToImageBatch, ImageScaleBy, ImageUpscaleWithModel, ImpactImageBatchToImageList, KSampler, KSamplerSelect, LoadImage, LoraLoader, LyingSigmaSampler, PreviewImage, RH_Captioner, RandomNoise, RepeatLatentBatch, SamplerCustomAdvanced, SaveImage, SetNode, ShowText|pysssss, StringFunction|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, Text Concatenate (JPS), UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageScaleDownBy, easy stylesSelector]
problems: []
missing: []
members: [图片生成/图生图/4K高清网红写实洗图流_2032442851988082689.json, 图片生成/文生图/4K高清网红写实洗图流_1890630074368958465.json, 图片生成/文生图/高清网红写实洗图流_2052935015373262850.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_81

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/4K高清网红写实洗图流_2032442851988082689.json、图片生成/文生图/4K高清网红写实洗图流_1890630074368958465.json、图片生成/文生图/高清网红写实洗图流_2052935015373262850.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyFBCacheOnModel`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `CR SDXL Aspect Ratio`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `ImpactImageBatchToImageList`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `LyingSigmaSampler`
- `PreviewImage`
- `RH_Captioner`
- `RandomNoise`
- `RepeatLatentBatch`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `Text Concatenate (JPS)`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageScaleDownBy`
- `easy stylesSelector`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | exponential | - | 3 | 100% |
| 重绘幅度 | 0.9 | 0.9 - 0.9 | 3 | 100% |
| 宽度 | 800 | 800 - 800 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| LoRA 模型强度 | 0.8 | 0.7 - 0.8 | 3 | 94% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 exponential，3 个样本，一致性 100%
- 重绘幅度 中位数 0.9，观测区间 0.9 - 0.9，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 800，观测区间 800 - 800，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，观测区间 0.7 - 0.8，3 个样本，取值集中（一致性 94%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
