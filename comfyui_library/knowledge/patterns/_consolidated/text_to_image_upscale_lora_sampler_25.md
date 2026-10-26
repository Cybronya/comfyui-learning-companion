---
name: text_to_image_upscale_lora_sampler_25
type: Text To Image
frequency: 9
level: strong
coverage: 0.935889
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, GetImageSize+, INTConstant, Image Comparer (rgthree), ImageResize+, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, VAEDecode, easy cleanGpuUsed, easy clearCacheAll, easy imageScaleDownBy]
problems: []
missing: []
members: [图片生成/文生图/Z-image-AIO超真实极致放大8K画质_2072147469131149314.json, 图片生成/文生图/Zimage文生图极致放大高清画质_2053323952407232513.json, 图片生成/文生图/Zimage文生图极致放大高清画质_2057126806733541378.json, 图片生成/文生图/文生图Zimage极致放大8K画质_2045854309325213697.json, 图片生成/文生图/文生图Zimage极致放大_2046032429256810497.json, 图片生成/文生图/文生图Zimage极致放大_2071861851847221250.json, 图片生成/文生图/文生图Zimage极致放大_2071880803600125954.json, 图片生成/文生图/文生图极致放大8K画质_2046511468165730305.json, 视频生成/文生视频/Z-image-AIO超真实极致放大8K画质_1999037874991456257.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_25

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Z-image-AIO超真实极致放大8K画质_2072147469131149314.json、图片生成/文生图/Zimage文生图极致放大高清画质_2053323952407232513.json、图片生成/文生图/Zimage文生图极致放大高清画质_2057126806733541378.json、图片生成/文生图/文生图Zimage极致放大8K画质_2045854309325213697.json、图片生成/文生图/文生图Zimage极致放大_2046032429256810497.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSize+`
- `INTConstant`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `VAEDecode`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy imageScaleDownBy`

**可变部分**（部分 workflow 才有）：
- `ImageScaleBy` —— 4/9 个有
- `PreviewImage` —— 4/9 个有
- `Float` —— 2/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 760 | 760 - 760 | 9 | 100% |
| 高度 | 1024 | 1024 - 1024 | 9 | 100% |
| 采样步数 | 10 | 10 - 12 | 9 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 760，观测区间 760 - 760，9 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 10 - 12，9 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
