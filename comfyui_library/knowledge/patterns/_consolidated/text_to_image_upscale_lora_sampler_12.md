---
name: text_to_image_upscale_lora_sampler_12
type: Text To Image
frequency: 7
level: moderate
coverage: 0.920857
common_nodes: [CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), ImageResize+, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, VAEDecode, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image-AIO超真实极致放大8K画质_2072147469131149314.json, 图片生成/文生图/krea2基础文生图高清_2102596196979269634.json, 图片生成/文生图/krea2文生图高清_2081557717600260097.json, 图片生成/文生图/krea2文生图高清_2081698530154082306.json, 图片生成/文生图/文生图Zimage极致放大_2071861851847221250.json, 图片生成/文生图/文生图Zimage极致放大_2071880803600125954.json, 视频生成/文生视频/Z-image-AIO超真实极致放大8K画质_1999037874991456257.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_12

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Z-image-AIO超真实极致放大8K画质_2072147469131149314.json、图片生成/文生图/krea2基础文生图高清_2102596196979269634.json、图片生成/文生图/krea2文生图高清_2081557717600260097.json、图片生成/文生图/krea2文生图高清_2081698530154082306.json、图片生成/文生图/文生图Zimage极致放大_2071861851847221250.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
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
- `ImageScaleBy` —— 5/7 个有
- `CheckpointLoaderSimple` —— 4/7 个有
- `GetImageSize+` —— 4/7 个有
- `INTConstant` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `easy clearCacheAll` —— 4/7 个有
- `easy imageScaleDownBy` —— 4/7 个有
- `CLIPLoader` —— 3/7 个有
- `GetNode` —— 3/7 个有
- `UNETLoader` —— 3/7 个有
- `VAELoader` —— 3/7 个有
- `easy imageSize` —— 3/7 个有
- `CLIPLoaderGGUF` —— 2/7 个有
- `SetNode` —— 2/7 个有
- `VAEEncode` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 760 | 760 - 1024 | 7 | 85% |
| 高度 | 1024 | 1024 - 1024 | 7 | 100% |
| 采样步数 | 10 | 6 - 10 | 7 | 79% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 7 | 57% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 0.25 - 1 | 7 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 760，观测区间 760 - 1024，7 个样本，取值集中（一致性 85%）
- 高度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 6 - 10，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，7 个样本，一致性 57%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.25 - 1，7 个样本
- 高发问题（5/7 个样本）：Steps较低可能导致细节不足
