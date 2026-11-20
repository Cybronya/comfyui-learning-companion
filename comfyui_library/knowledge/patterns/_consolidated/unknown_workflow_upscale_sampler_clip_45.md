---
name: unknown_workflow_upscale_sampler_clip_45
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8455
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, ImageUpscaleWithModel, KSamplerSelect, LoadImage, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/文生图/文生图或图放大（4k）_1901839602184036353.json, 平台全量/FLUX图像无损放大_1851980086793986050.json, 平台全量/植物细化_2053729038467911682.json, 平台全量/植物细化_2084921137074622466.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_45

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/文生图或图放大（4k）_1901839602184036353.json、平台全量/FLUX图像无损放大_1851980086793986050.json、平台全量/植物细化_2053729038467911682.json、平台全量/植物细化_2084921137074622466.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `Florence2ModelLoader` —— 3/4 个有
- `Florence2Run` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `easy imageListToImageBatch` —— 3/4 个有
- `CR Prompt Text` —— 2/4 个有
- `Constant Number` —— 2/4 个有
- `ImageResize+` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `LoraLoader` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `easy imageInsetCrop` —— 2/4 个有
- `CLIPTextEncodeFlux` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `EmptyLatentImage` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `ImageListToBatch+` —— 1/4 个有
- `MuyeTextEditOutput` —— 1/4 个有
- `Text Find and Replace` —— 1/4 个有
- `VAEDecode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |
| LoRA 模型强度 | 0.925 | - | 2 | 92% |
| LoRA 文本强度 | 0.925 | - | 2 | 92% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.925，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- LoRA 文本强度 中位数 0.925，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
