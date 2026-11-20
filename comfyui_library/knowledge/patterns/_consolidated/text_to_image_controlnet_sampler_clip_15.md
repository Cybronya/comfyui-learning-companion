---
name: text_to_image_controlnet_sampler_clip_15
type: Text To Image
frequency: 5
level: moderate
coverage: 0.8226
common_nodes: [AIO_Preprocessor, BasicGuider, BasicScheduler, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApply, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, GetImageSize+, ImageInvert, ImageResizeKJ, KSampler, KSamplerSelect, LoadImage, PreviewImage, RH_Captioner, RH_Prompter, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, TextBox, TextCombinerSix, TextCombinerTwo, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/【自用，修复部分bug】服装设计3-线稿上色_2027728162251083777.json, 图片生成/图生图/线稿一键上色质感动漫_1890706658040094722.json, 平台全量/服装设计3-线稿上色_1909884431149268993.json, 平台全量/线稿上色_1871401133620228098.json, 平台全量/线稿转卡通3D工作流_1907738623158923265.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_15

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/【自用，修复部分bug】服装设计3-线稿上色_2027728162251083777.json、图片生成/图生图/线稿一键上色质感动漫_1890706658040094722.json、平台全量/服装设计3-线稿上色_1909884431149268993.json、平台全量/线稿上色_1871401133620228098.json、平台全量/线稿转卡通3D工作流_1907738623158923265.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `AIO_Preprocessor`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApply`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageInvert`
- `ImageResizeKJ`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `PreviewImage`
- `RH_Captioner`
- `RH_Prompter`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `TextBox`
- `TextCombinerSix`
- `TextCombinerTwo`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 4/5 个有
- `UpscaleModelLoader` —— 4/5 个有
- `ImageResize+` —— 3/5 个有
- `JjkText` —— 3/5 个有
- `LoraLoader` —— 3/5 个有
- `RH_Translator` —— 3/5 个有
- `RepeatLatentBatch` —— 3/5 个有
- `CR Prompt Text` —— 2/5 个有
- `CR Text Input Switch` —— 2/5 个有
- `FluxGuidance` —— 2/5 个有
- `ImageScaleToTotalPixels` —— 2/5 个有
- `Int` —— 2/5 个有
- `LayerUtility: GetMainColors` —— 2/5 个有
- `Note _O` —— 2/5 个有
- `TTP_Image_Assy` —— 2/5 个有
- `TTP_Image_Tile_Batch` —— 2/5 个有
- `TTP_Tile_image_size` —— 2/5 个有
- `VAEDecodeTiled` —— 2/5 个有
- `easy imageBatchToImageList` —— 2/5 个有
- `easy imageListToImageBatch` —— 2/5 个有
- `Label (rgthree)` —— 1/5 个有
- `SeedGenerator` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 5 | 100% |
| 高度 | 512 | 512 - 512 | 5 | 100% |
| ControlNet 权重 | 0.85 | 0.85 - 0.85 | 5 | 100% |
| LoRA 模型强度 | 0.7 | 0.4 - 0.7 | 3 | 76% |
| LoRA 文本强度 | 0.7 | 0.4 - 0.7 | 3 | 76% |
| 采样步数 | 20 | 12 - 20 | 5 | 77% |
| Prompt 约束强度(CFG) | 8 | 4.21 - 8 | 5 | 71% |
| 采样算法 | euler_ancestral | - | 5 | 100% |
| 调度器 | normal | - | 5 | 100% |
| 重绘幅度 | 1 | 0.38 - 1 | 5 | 60% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，5 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，5 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.85，观测区间 0.85 - 0.85，5 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.7，观测区间 0.4 - 0.7，3 个样本
- LoRA 文本强度 中位数 0.7，观测区间 0.4 - 0.7，3 个样本
- 采样步数 中位数 20，观测区间 12 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 4.21 - 8，5 个样本
- 采样算法 最常用 euler_ancestral，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.38 - 1，5 个样本
