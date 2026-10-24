---
name: unknown_workflow_upscale_lora_sampler_67
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.843667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerSelect, LoraLoader, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/文生图/AI写真之胶片摄影_1907615339520397314.json, 图片生成/文生图/AI动画文生图_2026095152678309890.json, 图片生成/文生图/超强文生图+超清放大_1985899421487509506.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_67

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/AI写真之胶片摄影_1907615339520397314.json、图片生成/文生图/AI动画文生图_2026095152678309890.json、图片生成/文生图/超强文生图+超清放大_1985899421487509506.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

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
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `ImageListToImageBatch` —— 2/3 个有
- `ImageResizeKJ` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `ApplyTeaCachePatchAdvanced` —— 1/3 个有
- `CLIPTextEncodeFlux` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `LayerUtility: JoyCaption2` —— 1/3 个有
- `LyingSigmaSampler` —— 1/3 个有
- `SeargePromptCombiner` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `easy imageListToImageBatch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1360 | 720 - 1360 | 3 | 74% |
| 高度 | 768 | 768 - 1280 | 3 | 74% |
| LoRA 模型强度 | 0.8 | 0.5 - 0.8 | 3 | 80% |
| LoRA 文本强度 | 0.8 | 0.5 - 0.8 | 3 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1360，观测区间 720 - 1360，3 个样本
- 高度 中位数 768，观测区间 768 - 1280，3 个样本
- LoRA 模型强度 中位数 0.8，观测区间 0.5 - 0.8，3 个样本
- LoRA 文本强度 中位数 0.8，观测区间 0.5 - 0.8，3 个样本
