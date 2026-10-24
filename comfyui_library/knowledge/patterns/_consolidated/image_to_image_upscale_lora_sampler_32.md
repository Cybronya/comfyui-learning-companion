---
name: image_to_image_upscale_lora_sampler_32
type: Image To Image
frequency: 5
level: strong
coverage: 0.8046
common_nodes: [CLIPLoader, ConstrainImage|pysssss, Fast Groups Bypasser (rgthree), Get Image Size, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-2511 调色风格迁移（摄影专用）_2071046601908510721.json, 图片生成/文生图/ZIT更好的身材曲线（胸围控制）_2059984057596989442.json, 图片生成/文生图/元气少女-Z-Image-Turbo（4K高清直出）_2049867512954798082.json, 图片生成/文生图/造相-Z-Image-Turbo-标准工作流（4K高清直出）_2044330203832393729.json, 图片生成/文生图/造相-Z-Image-Turbo-标准工作流（4K高清直出）_2046666708684902401.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_32

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen-2511 调色风格迁移（摄影专用）_2071046601908510721.json、图片生成/文生图/ZIT更好的身材曲线（胸围控制）_2059984057596989442.json、图片生成/文生图/元气少女-Z-Image-Turbo（4K高清直出）_2049867512954798082.json、图片生成/文生图/造相-Z-Image-Turbo-标准工作流（4K高清直出）_2044330203832393729.json、图片生成/文生图/造相-Z-Image-Turbo-标准工作流（4K高清直出）_2046666708684902401.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ConstrainImage|pysssss`
- `Fast Groups Bypasser (rgthree)`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 4/5 个有
- `CLIPTextEncode` —— 4/5 个有
- `CR Prompt Text` —— 4/5 个有
- `CR Text Concatenate` —— 4/5 个有
- `Color Correct (mtb)` —— 4/5 个有
- `EmptySD3LatentImage` —— 4/5 个有
- `ShowText|pysssss` —— 4/5 个有
- `CFGNorm` —— 1/5 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `SeedVR2` —— 1/5 个有
- `SeedVR2BlockSwap` —— 1/5 个有
- `TextEncodeQwenImageEditPlus` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 5 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，5 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
