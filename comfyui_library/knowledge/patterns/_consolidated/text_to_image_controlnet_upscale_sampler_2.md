---
name: text_to_image_controlnet_upscale_sampler_2
type: Text To Image
frequency: 2
level: weak
coverage: 0.821
common_nodes: [AIO_Preprocessor, BasicGuider, BasicScheduler, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApply, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, GetImageSize+, ImageInvert, ImageResizeKJ, ImageUpscaleWithModel, KSampler, KSamplerSelect, LoadImage, PreviewImage, RH_Captioner, RH_Prompter, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, TextBox, TextCombinerSix, TextCombinerTwo, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/【自用，修复部分bug】服装设计3-线稿上色_2027728162251083777.json, 图片生成/图生图/线稿一键上色质感动漫_1890706658040094722.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_sampler_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【自用，修复部分bug】服装设计3-线稿上色_2027728162251083777.json、图片生成/图生图/线稿一键上色质感动漫_1890706658040094722.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
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
- `ImageUpscaleWithModel`
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
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `CR Text Input Switch` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `Int` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LayerUtility: GetMainColors` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `Note _O` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `RepeatLatentBatch` —— 1/2 个有
- `TTP_Image_Assy` —— 1/2 个有
- `TTP_Image_Tile_Batch` —— 1/2 个有
- `TTP_Tile_image_size` —— 1/2 个有
- `VAEDecodeTiled` —— 1/2 个有
- `easy imageBatchToImageList` —— 1/2 个有
- `easy imageListToImageBatch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| ControlNet 权重 | 0.85 | - | 2 | 100% |
| LoRA 模型强度 | 0.7 | - | 1 | 100% |
| LoRA 文本强度 | 0.7 | - | 1 | 100% |
| 采样步数 | 16 | - | 2 | 75% |
| Prompt 约束强度(CFG) | 6.105 | - | 2 | 69% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 0.69 | - | 2 | 55% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 16，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 6.105，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 0.69，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
