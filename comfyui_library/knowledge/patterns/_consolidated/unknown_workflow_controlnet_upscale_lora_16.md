---
name: unknown_workflow_controlnet_upscale_lora_16
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.597
common_nodes: [Anything Everywhere, BasicGuider, BasicScheduler, CLIPTextEncode, CR Simple Image Compare, ControlNetApplySD3, ControlNetLoader, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, DownloadAndLoadFlorence2Model, DualCLIPLoader, Fast Groups Bypasser (rgthree), Florence2Run, FluxGuidance, GetNode, Image Comparer (rgthree), ImageResizeKJ, ImageScaleToTotalPixels, ImageUpscaleWithModel, Int, KSamplerSelect, LoadImage, LoraLoaderModelOnly, Multi Text Merge, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextInput_, UnetLoaderGGUF, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList]
problems: []
missing: []
members: [平台全量/FLUX 雕刻大师_1850964005623058434.json, 平台全量/FLUX字母海报_1849440094343286786.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_lora_16

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/FLUX 雕刻大师_1850964005623058434.json、平台全量/FLUX字母海报_1849440094343286786.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：60%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Simple Image Compare`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `DownloadAndLoadFlorence2Model`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `Florence2Run`
- `FluxGuidance`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageResizeKJ`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `Int`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Multi Text Merge`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextInput_`
- `UnetLoaderGGUF`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `ApplyPulidFlux` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `Crop Face` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `Load RetinaFace` —— 1/2 个有
- `PulidFluxEvaClipLoader` —— 1/2 个有
- `PulidFluxInsightFaceLoader` —— 1/2 个有
- `PulidFluxModelLoader` —— 1/2 个有
- `RepeatLatentBatch` —— 1/2 个有
- `SDXLPromptStylerAdvanced` —— 1/2 个有
- `UNETLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.45 | - | 2 | 89% |
| 宽度 | 512 | - | 1 | 100% |
| 高度 | 512 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.45，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
