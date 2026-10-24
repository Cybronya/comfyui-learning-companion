---
name: unknown_workflow_upscale_sampler_clip_12
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.832
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, ImageUpscaleWithModel, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/分块高清放大工作流_1934782777130688514.json, 图片生成/图生图/图片-TTP高清修复放大_1978037084130791426.json, 图片生成/图生图/图片超级高清放大_1915403255067639810.json, 图片生成/图生图/场景图8K高清修复放大_2071474028497428482.json, 图片生成/图生图/放大-F.1_1942192673929498626.json, 图片生成/图生图/高清放大_1902741134769074178.json, 图片生成/图生图/高清放大工作流（TRANCE）_1925847949354422273.json, 图片生成/文生图/文生图或图放大（4k）_1901839602184036353.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_12

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/分块高清放大工作流_1934782777130688514.json、图片生成/图生图/图片-TTP高清修复放大_1978037084130791426.json、图片生成/图生图/图片超级高清放大_1915403255067639810.json、图片生成/图生图/场景图8K高清修复放大_2071474028497428482.json、图片生成/图生图/放大-F.1_1942192673929498626.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoadImage`
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
- `FluxGuidance` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `Image Comparer (rgthree)` —— 5/8 个有
- `ImageResize+` —— 5/8 个有
- `ImageScaleToTotalPixels` —— 5/8 个有
- `LoraLoader` —— 5/8 个有
- `Florence2ModelLoader` —— 4/8 个有
- `Florence2Run` —— 4/8 个有
- `ImageListToImageBatch` —— 3/8 个有
- `easy imageListToImageBatch` —— 3/8 个有
- `Constant Number` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `ImageListToBatch+` —— 2/8 个有
- `ShowText|pysssss` —— 2/8 个有
- `Text Find and Replace` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `easy imageInsetCrop` —— 2/8 个有
- `CLIPTextEncodeFlux` —— 1/8 个有
- `CR Prompt Text` —— 1/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `EmptyLatentImage` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有
- `NunchakuFluxDiTLoader` —— 1/8 个有
- `VAEDecode` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 0.8 - 1 | 5 | 92% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，5 个样本，取值集中（一致性 92%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
