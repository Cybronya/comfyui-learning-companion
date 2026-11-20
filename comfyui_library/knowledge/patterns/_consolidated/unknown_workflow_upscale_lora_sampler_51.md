---
name: unknown_workflow_upscale_lora_sampler_51
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.91075
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageListToImageBatch, ImageResizeKJ, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerSelect, LoadImage, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/【人物一致多角度】FLUX完美三视图不同视角IP角色创建_1916057498137333761.json, 图片生成/图生图/室内外洗图洗稿2.0丨超强质感3k高清_1925214634473627650.json, 图片生成/图生图/室内建筑场景洗图+高清修复_1937868192171606018.json, 图片生成/图生图/室内建筑场景洗图+高清修复_1976190617967558657.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_51

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/【人物一致多角度】FLUX完美三视图不同视角IP角色创建_1916057498137333761.json、图片生成/图生图/室内外洗图洗稿2.0丨超强质感3k高清_1925214634473627650.json、图片生成/图生图/室内建筑场景洗图+高清修复_1937868192171606018.json、图片生成/图生图/室内建筑场景洗图+高清修复_1976190617967558657.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageResizeKJ`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `ConstrainImage|pysssss` —— 3/4 个有
- `Float` —— 3/4 个有
- `Joy_caption_two` —— 2/4 个有
- `Joy_caption_two_load` —— 2/4 个有
- `LayerMask: LoadFlorence2Model` —— 2/4 个有
- `LayerUtility: Florence2Image2Prompt` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `ControlNetApplySD3` —— 1/4 个有
- `ControlNetLoader` —— 1/4 个有
- `DWPreprocessor` —— 1/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `Florence2ModelLoader` —— 1/4 个有
- `Florence2Run` —— 1/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有
- `LoadImagesFromURL` —— 1/4 个有
- `ModelSamplingFlux` —— 1/4 个有
- `Simple String` —— 1/4 个有
- `StringFunction|pysssss` —— 1/4 个有
- `UltimateSDUpscale` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.75 | - | 1 | 100% |
| LoRA 模型强度 | 0.5 | 0.5 - 0.9 | 4 | 71% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.5，观测区间 0.5 - 0.9，4 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
