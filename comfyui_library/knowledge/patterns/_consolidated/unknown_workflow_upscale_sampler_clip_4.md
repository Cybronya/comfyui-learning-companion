---
name: unknown_workflow_upscale_sampler_clip_4
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.893083
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/FLUX.  高清.修复.放大v5_1897313990823858178.json, 图片生成/图生图/FLUX超级高清放大修复_1911254476370706434.json, 图片生成/图生图/Flux-tile产品放大_1907653000217653250.json, 图片生成/图生图/Flux-图片降噪_1985551366481498113.json, 图片生成/图生图/flux图片高清放大_1915659288834932737.json, 图片生成/图生图/flux高清放大+Lora_1952609311073742849.json, 图片生成/图生图/flux高清放大-在线生图4K-标准版 (1)_1929345768141000706.json, 图片生成/图生图/flux高清放大-在线生图_1974848985930272769.json, 图片生成/图生图/flux高清放大-在线生图_1982986890833997825.json, 图片生成/图生图/flux高清放大-细节加强_2016726353726414850.json, 图片生成/图生图/「全网最强升级版」flux无损放大放大+修复_1882767903618486274.json, 图片生成/图生图/【人物一致多角度】FLUX完美三视图不同视角IP角色创建_1916057498137333761.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_4

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/FLUX.  高清.修复.放大v5_1897313990823858178.json、图片生成/图生图/FLUX超级高清放大修复_1911254476370706434.json、图片生成/图生图/Flux-tile产品放大_1907653000217653250.json、图片生成/图生图/Flux-图片降噪_1985551366481498113.json、图片生成/图生图/flux图片高清放大_1915659288834932737.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
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
- `LoraLoader` —— 11/12 个有
- `UNETLoader` —— 11/12 个有
- `ImageResizeKJ` —— 9/12 个有
- `Joy_caption_two` —— 5/12 个有
- `Joy_caption_two_load` —— 5/12 个有
- `PreviewImage` —— 4/12 个有
- `StringFunction|pysssss` —— 3/12 个有
- `CLIPTextEncodeFlux` —— 2/12 个有
- `ConditioningCombine` —— 2/12 个有
- `ImageResize+` —— 2/12 个有
- `Joy_caption` —— 2/12 个有
- `Joy_caption_load` —— 2/12 个有
- `easy showAnything` —— 2/12 个有
- `Anything Everywhere3` —— 1/12 个有
- `ControlNetApplySD3` —— 1/12 个有
- `ControlNetLoader` —— 1/12 个有
- `DWPreprocessor` —— 1/12 个有
- `EmptySD3LatentImage` —— 1/12 个有
- `Fast Groups Muter (rgthree)` —— 1/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `LoraLoaderModelOnly` —— 1/12 个有
- `ModelSamplingFlux` —— 1/12 个有
- `Simple String` —— 1/12 个有
- `UltimateSDUpscale` —— 1/12 个有
- `VAEDecode` —— 1/12 个有
- `workflow/model` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 0.8 - 1 | 11 | 94% |
| LoRA 文本强度 | 1 | 1 - 1 | 11 | 100% |
| ControlNet 权重 | 0.75 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，11 个样本，取值集中（一致性 94%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
