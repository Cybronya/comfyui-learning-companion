---
name: text_to_image_upscale_lora_sampler_13
type: Text To Image
frequency: 12
level: strong
coverage: 0.92525
common_nodes: [CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), ImageResize+, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, VAEDecode, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image-AIO超真实极致放大8K画质_2072147469131149314.json, 图片生成/文生图/Zimage文生图极致放大高清画质_2053323952407232513.json, 图片生成/文生图/Zimage文生图极致放大高清画质_2057126806733541378.json, 图片生成/文生图/krea2基础文生图高清_2102596196979269634.json, 图片生成/文生图/krea2文生图高清_2081557717600260097.json, 图片生成/文生图/krea2文生图高清_2081698530154082306.json, 图片生成/文生图/文生图Zimage极致放大8K画质_2045854309325213697.json, 图片生成/文生图/文生图Zimage极致放大_2046032429256810497.json, 图片生成/文生图/文生图Zimage极致放大_2071861851847221250.json, 图片生成/文生图/文生图Zimage极致放大_2071880803600125954.json, 图片生成/文生图/文生图极致放大8K画质_2046511468165730305.json, 视频生成/文生视频/Z-image-AIO超真实极致放大8K画质_1999037874991456257.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_13

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/Z-image-AIO超真实极致放大8K画质_2072147469131149314.json、图片生成/文生图/Zimage文生图极致放大高清画质_2053323952407232513.json、图片生成/文生图/Zimage文生图极致放大高清画质_2057126806733541378.json、图片生成/文生图/krea2基础文生图高清_2102596196979269634.json、图片生成/文生图/krea2文生图高清_2081557717600260097.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
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

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 9/12 个有
- `GetImageSize+` —— 9/12 个有
- `INTConstant` —— 9/12 个有
- `easy clearCacheAll` —— 9/12 个有
- `easy imageScaleDownBy` —— 9/12 个有
- `ImageScaleBy` —— 7/12 个有
- `PreviewImage` —— 6/12 个有
- `CLIPLoader` —— 3/12 个有
- `GetNode` —— 3/12 个有
- `UNETLoader` —— 3/12 个有
- `VAELoader` —— 3/12 个有
- `easy imageSize` —— 3/12 个有
- `CLIPLoaderGGUF` —— 2/12 个有
- `Float` —— 2/12 个有
- `SetNode` —— 2/12 个有
- `VAEEncode` —— 2/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 760 | 760 - 1024 | 12 | 86% |
| 高度 | 1024 | 1024 - 1024 | 12 | 100% |
| 采样步数 | 10 | 6 - 12 | 12 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 12 | 75% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 0.25 - 1 | 12 | 68% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 760，观测区间 760 - 1024，12 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，观测区间 1024 - 1024，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 6 - 12，12 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，12 个样本，一致性 75%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.25 - 1，12 个样本
