---
name: unknown_workflow_upscale_sampler_clip_37
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.860667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DownloadAndLoadFlorence2Model, Florence2Run, Image Comparer (rgthree), ImageUpscaleWithModel, KSamplerSelect, LoadImage, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UpscaleModelLoader, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: []
missing: []
members: [图片生成/图生图/Flux-Nunchaku极速洗图-优化细节_1911034449600151554.json, 图片生成/图生图/Flux商业洗图+放大_1904367585897652225.json, 图片生成/图生图/Qwen-Image的分块放大_1955543349093548034.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_37

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux-Nunchaku极速洗图-优化细节_1911034449600151554.json、图片生成/图生图/Flux商业洗图+放大_1904367585897652225.json、图片生成/图生图/Qwen-Image的分块放大_1955543349093548034.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `Image Comparer (rgthree)`
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
- `UpscaleModelLoader`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `ImageScale` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `VAEDecode` —— 2/3 个有
- `CFGGuider` —— 1/3 个有
- `CLIPLoader` —— 1/3 个有
- `Display Any (rgthree)` —— 1/3 个有
- `DualCLIPLoader` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `NunchakuFluxDiTLoader` —— 1/3 个有
- `NunchakuFluxLoraLoader` —— 1/3 个有
- `NunchakuTextEncoderLoader` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `VAEDecodeTiled` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
