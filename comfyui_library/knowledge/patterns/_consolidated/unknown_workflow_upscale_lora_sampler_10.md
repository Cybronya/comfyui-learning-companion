---
name: unknown_workflow_upscale_lora_sampler_10
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.807333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerSelect, LoraLoader, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: [ImageListToBatch+, Text Find and Replace, easy imageBatchToImageList, CR Prompt Text, LayerUtility: JoyCaption2, easy imageListToImageBatch]
members: [图片生成/文生图/1901839602184036353.json, 图片生成/文生图/1907615339520397314.json, 图片生成/文生图/3D蛇年定制头像_1882053493610700801.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_10

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1901839602184036353.json、图片生成/文生图/1907615339520397314.json、图片生成/文生图/3D蛇年定制头像_1882053493610700801.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoraLoader`
- `PreviewImage`
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
- `CLIPTextEncodeFlux` —— 2/3 个有
- `CR Prompt Text` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `easy imageListToImageBatch` —— 2/3 个有
- `AegisFlow/aflogo` —— 1/3 个有
- `ApplyTeaCachePatchAdvanced` —— 1/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Florence2ModelLoader` —— 1/3 个有
- `Florence2Run` —— 1/3 个有
- `FluxResolutionNode` —— 1/3 个有
- `ImageListToBatch+` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `LayerUtility: JoyCaption2` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `LyingSigmaSampler` —— 1/3 个有
- `RH_Prompter` —— 1/3 个有
- `SeargePromptCombiner` —— 1/3 个有
- `Text Find and Replace` —— 1/3 个有
- `TextCombinerTwo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 1024 | 3 | 84% |
| 高度 | 1280 | 1024 - 1280 | 3 | 90% |
| LoRA 模型强度 | 0.8 | 0.5 - 1 | 3 | 73% |
| LoRA 文本强度 | 1 | 0.5 - 1 | 3 | 72% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 1024，3 个样本，取值集中（一致性 84%）
- 高度 中位数 1280，观测区间 1024 - 1280，3 个样本，取值集中（一致性 90%）
- LoRA 模型强度 中位数 0.8，观测区间 0.5 - 1，3 个样本
- LoRA 文本强度 中位数 1，观测区间 0.5 - 1，3 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：ImageListToBatch+、Text Find and Replace、easy imageBatchToImageList、CR Prompt Text、LayerUtility: JoyCaption2
