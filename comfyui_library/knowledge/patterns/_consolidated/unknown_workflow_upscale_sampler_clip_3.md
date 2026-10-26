---
name: unknown_workflow_upscale_sampler_clip_3
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.90375
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/FLUX-高清修复-保留细节_1963975272259272705.json, 图片生成/图生图/FLUX超级高清放大修复_1911254476370706434.json, 图片生成/图生图/Flux-tile产品放大_1907653000217653250.json, 图片生成/图生图/Flux-图片降噪_1985551366481498113.json, 图片生成/图生图/flux高清放大-在线生图4K-标准版 (1)_1929345768141000706.json, 图片生成/图生图/flux高清放大-在线生图_1982986890833997825.json, 图片生成/图生图/flux高清放大-细节加强_2016726353726414850.json, 图片生成/图生图/小脸崩坏修复、细节修复，flux万能修复工作流_1927318504762925057.json, 图片生成/图生图/极致高清放大_2068619553789276162.json, 图片生成/图生图/超清放大 物-景-人 通用_1911244460179582977.json, 图片生成/图生图/超级高清放大，任意图像变无比高清图_1923649088472928257.json, 图片生成/图生图/高清放大(7)flux放大丨支持在线一键生成_1914340386142154754.json, 图片生成/图生图/高清放大-3D运营海报专用_2084528029019230210.json, 图片生成/图生图/高清放大-3D运营海报专用_2084918972494999553.json, 图片生成/图生图/高清放大-3D运营海报专用_2084920422033874946.json, 图片生成/文生图/FLUX-高清修复-不改变人物_商品主体细节-API便捷调用版_1989960138809372674.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_3

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/FLUX-高清修复-保留细节_1963975272259272705.json、图片生成/图生图/FLUX超级高清放大修复_1911254476370706434.json、图片生成/图生图/Flux-tile产品放大_1907653000217653250.json、图片生成/图生图/Flux-图片降噪_1985551366481498113.json、图片生成/图生图/flux高清放大-在线生图4K-标准版 (1)_1929345768141000706.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
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
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 15/16 个有
- `Joy_caption_two` —— 11/16 个有
- `Joy_caption_two_load` —— 11/16 个有
- `ImageResizeKJ` —— 10/16 个有
- `LoraLoader` —— 10/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/16 个有
- `PreviewImage` —— 6/16 个有
- `CR Text` —— 5/16 个有
- `LoraLoaderModelOnly` —— 5/16 个有
- `CR Text Concatenate` —— 3/16 个有
- `RH_Captioner` —— 3/16 个有
- `DifferentialDiffusion` —— 2/16 个有
- `FloatConstant` —— 2/16 个有
- `GetNode` —— 2/16 个有
- `SetNode` —— 2/16 个有
- `ShowText|pysssss` —— 2/16 个有
- `Text Concatenate (JPS)` —— 2/16 个有
- `VAEEncodeTiled` —— 2/16 个有
- `Anything Everywhere3` —— 1/16 个有
- `JjkShowText` —— 1/16 个有
- `LoadImagesFromURL` —— 1/16 个有
- `PMRF` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 10 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
