---
name: unknown_workflow_upscale_sampler_clip_6
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.877143
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, ImageListToImageBatch, ImageUpscaleWithModel, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/FLUX.  高清.修复.放大v5_1897313990823858178.json, 图片生成/图生图/flux图片高清放大_1915659288834932737.json, 图片生成/图生图/flux高清放大+Lora_1952609311073742849.json, 图片生成/图生图/flux高清放大-在线生图_1974848985930272769.json, 图片生成/图生图/「全网最强升级版」flux无损放大放大+修复_1882767903618486274.json, 图片生成/图生图/一键放大照片工作流_1920420645321248770.json, 图片生成/图生图/图像TTP分块放大 增加真实细节  高清修复放大-TTP放大 写实4K 万物通用版v1.0_2094731786977890306.json, 图片生成/图生图/图像超分-10.23-flux-tile放大_1981552116315635713.json, 图片生成/图生图/场景图8K高清修复放大_2071474028497428482.json, 图片生成/图生图/汽车图片8K放大+lora修复车身加速版_2056945533108973570.json, 图片生成/图生图/电商高清放大  精修处理_2015156106552676353.json, 图片生成/图生图/高清放大  精修处理_2004411744959295490.json, 图片生成/图生图/高清放大_1902741134769074178.json, 图片生成/图生图/🦖TTP 保细节放大_1894331074686922754.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_6

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/FLUX.  高清.修复.放大v5_1897313990823858178.json、图片生成/图生图/flux图片高清放大_1915659288834932737.json、图片生成/图生图/flux高清放大+Lora_1952609311073742849.json、图片生成/图生图/flux高清放大-在线生图_1974848985930272769.json、图片生成/图生图/「全网最强升级版」flux无损放大放大+修复_1882767903618486274.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `ImageListToImageBatch`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 13/14 个有
- `UNETLoader` —— 13/14 个有
- `FluxGuidance` —— 12/14 个有
- `Image Comparer (rgthree)` —— 12/14 个有
- `ImageScaleToTotalPixels` —— 12/14 个有
- `PreviewImage` —— 10/14 个有
- `ImageResize+` —— 6/14 个有
- `ImageResizeKJ` —— 5/14 个有
- `CLIPTextEncodeFlux` —— 3/14 个有
- `ConditioningCombine` —— 3/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/14 个有
- `LoraLoaderModelOnly` —— 3/14 个有
- `CR Simple Image Compare` —— 2/14 个有
- `ConditioningZeroOut` —— 2/14 个有
- `Joy_caption` —— 2/14 个有
- `Joy_caption_load` —— 2/14 个有
- `PlaySound|pysssss` —— 2/14 个有
- `StringFunction|pysssss` —— 2/14 个有
- `easy cleanGpuUsed` —— 2/14 个有
- `easy showAnything` —— 2/14 个有
- `RH_Captioner` —— 1/14 个有
- `workflow/model` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 0.8 - 1 | 13 | 94% |
| LoRA 文本强度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，13 个样本，取值集中（一致性 94%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
