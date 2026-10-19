---
name: text_to_image_upscale_lora_sampler_6
type: Text To Image
frequency: 5
level: weak
coverage: 0.8924
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize+, ImageResize+, ImageScaleBy, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图片放大图生图工作流｜低清小图秒变高清大图，细节无损放大_2107335691196788737.json, 图片生成/文生图/Z-Image 一键出图，细节拉满 8K_2104461803777519617.json, 图片生成/文生图/Z-Image文生图8K_2100484708844007425.json, 图片生成/文生图/文生图 Z-Image在线8K直出_2100499203217780738.json, 视频生成/文生视频/超级简单 一键生成-文生图 Z-Image在线8K直出_2094597344456171521.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_6

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/图片放大图生图工作流｜低清小图秒变高清大图，细节无损放大_2107335691196788737.json、图片生成/文生图/Z-Image 一键出图，细节拉满 8K_2104461803777519617.json、图片生成/文生图/Z-Image文生图8K_2100484708844007425.json、图片生成/文生图/文生图 Z-Image在线8K直出_2100499203217780738.json、视频生成/文生视频/超级简单 一键生成-文生图 Z-Image在线8K直出_2094597344456171521.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `PrimitiveFloat` —— 4/5 个有
- `Text Multiline` —— 4/5 个有
- `JjkText` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `SaveImageJPG_GH` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy clearCacheAll` —— 1/5 个有
- `solarL_SaveImagesToZip` —— 1/5 个有
- `孤海注释` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 80 - 1080 | 5 | 55% |
| 高度 | 1920 | 80 - 1920 | 5 | 53% |
| 采样步数 | 9 | 4 - 9 | 5 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 5 | 18% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | sgm_uniform | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 80 - 1080，5 个样本
- 高度 中位数 1920，观测区间 80 - 1920，5 个样本
- 采样步数 中位数 9，观测区间 4 - 9，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，5 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
