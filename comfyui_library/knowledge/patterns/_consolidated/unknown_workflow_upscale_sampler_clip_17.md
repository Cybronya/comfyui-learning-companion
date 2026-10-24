---
name: unknown_workflow_upscale_sampler_clip_17
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.756
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionLoader, DualCLIPLoader, FluxGuidance, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, StyleModelLoader, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/FLUX网红复制流_1906249305932353538.json, 图片生成/图生图/Fast upscale Flux_1937350990159101953.json, 图片生成/图生图/Flux人像图片4K超清放大V2.3_1955463868035186690.json, 图片生成/图生图/「无需抽卡」图片+Lora网红脸一键融合_2040308225584664577.json, 图片生成/图生图/「无需抽卡」图片+Lora网红脸一键融合_2041807805040037890.json, 图片生成/图生图/「无需抽卡」图片+Lora网红脸融合_1885348084627697665.json, 图片生成/图生图/一键生成网红脸，上传一张模特图片融合_2017607231864311810.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_17

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/FLUX网红复制流_1906249305932353538.json、图片生成/图生图/Fast upscale Flux_1937350990159101953.json、图片生成/图生图/Flux人像图片4K超清放大V2.3_1955463868035186690.json、图片生成/图生图/「无需抽卡」图片+Lora网红脸一键融合_2040308225584664577.json、图片生成/图生图/「无需抽卡」图片+Lora网红脸一键融合_2041807805040037890.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelLoader`
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
- `CLIPVisionEncode` —— 6/7 个有
- `Florence2Run` —— 6/7 个有
- `Image Comparer (rgthree)` —— 6/7 个有
- `ImageResizeKJ` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `StyleModelApply` —— 6/7 个有
- `EmptySD3LatentImage` —— 5/7 个有
- `GetNode` —— 5/7 个有
- `SetNode` —— 5/7 个有
- `VAEDecode` —— 5/7 个有
- `easy cleanGpuUsed` —— 5/7 个有
- `DepthAnythingPreprocessor` —— 4/7 个有
- `DisableNoise` —— 4/7 个有
- `DownloadAndLoadFlorence2Model` —— 4/7 个有
- `LayerFilter: FilmV2` —— 4/7 个有
- `ModelSamplingFlux` —— 4/7 个有
- `PlaySound|pysssss` —— 4/7 个有
- `ShowText|pysssss` —— 4/7 个有
- `SplitSigmasDenoise` —— 4/7 个有
- `Florence2ModelLoader` —— 2/7 个有
- `easy imageListToImageBatch` —— 2/7 个有
- `Anything Everywhere3` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `ImageListToImageBatch` —— 1/7 个有
- `LoraLoader` —— 1/7 个有
- `ReduxAdvanced` —— 1/7 个有
- `String Literal` —— 1/7 个有
- `Text Concatenate (JPS)` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
