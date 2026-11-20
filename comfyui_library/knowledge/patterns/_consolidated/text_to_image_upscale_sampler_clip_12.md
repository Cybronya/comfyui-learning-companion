---
name: text_to_image_upscale_sampler_clip_12
type: Text To Image
frequency: 9
level: weak
coverage: 0.883222
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/千问最新文生图模型 2512_2006387159393112065.json, 图片生成/文生图/强力模型Z-image，活人感图片生成_1993860368776757249.json, 图片生成/文生图/熊猫哥AIGC_Zimage_文生图+高清放大_2054039924533407745.json, 图片生成/文生图/瑶光 zimage出图_2056391963225706497.json, 图片生成/文生图/短剧主角生成工作流ZImage+Kook瑶光lora_2053108617959755777.json, 图片生成/文生图/短剧剧情设计工作流-ZImage+Kook大佬瑶光lora+Kook如梦似幻lora_2053083458406236162.json, 图片生成/文生图/短剧最佳拍档AI创客训练营｜画布功能支持场景角色创作_2106237793725931522.json, 图片生成/文生图/短剧最佳拍档画布功能，支持场景角色文生视频_2111550122223038466.json, 图片生成/文生图/高清放大｜Krea2 lora动漫角色文生图基础工作流_2089832493032763394.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_12

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/千问最新文生图模型 2512_2006387159393112065.json、图片生成/文生图/强力模型Z-image，活人感图片生成_1993860368776757249.json、图片生成/文生图/熊猫哥AIGC_Zimage_文生图+高清放大_2054039924533407745.json、图片生成/文生图/瑶光 zimage出图_2056391963225706497.json、图片生成/文生图/短剧主角生成工作流ZImage+Kook瑶光lora_2053108617959755777.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 8/9 个有
- `Image Comparer (rgthree)` —— 7/9 个有
- `ImageScaleToTotalPixels` —— 7/9 个有
- `Fast Groups Bypasser (rgthree)` —— 6/9 个有
- `CR Text` —— 5/9 个有
- `FastFilmGrain` —— 3/9 个有
- `INTConstant` —— 3/9 个有
- `JjkText` —— 3/9 个有
- `LayerColor: BrightnessContrastV2` —— 3/9 个有
- `PreviewImage` —— 3/9 个有
- `solarL_SaveImagesToZip` —— 3/9 个有
- `孤海注释` —— 3/9 个有
- `ConditioningZeroOut` —— 2/9 个有
- `MuyeTextEditOutput` —— 2/9 个有
- `FluxResolutionNode` —— 1/9 个有
- `TTResolutionSelector` —— 1/9 个有
- `easy ifElse` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 80 - 1920 | 9 | 20% |
| 高度 | 1080 | 80 - 1920 | 9 | 20% |
| 采样步数 | 8 | 4 - 10 | 9 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 9 | 24% |
| 采样算法 | er_sde | - | 9 | 33% |
| 调度器 | beta | - | 9 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 80 - 1920，9 个样本，取值分散，一致性仅 20%
- 高度 中位数 1080，观测区间 80 - 1920，9 个样本，取值分散，一致性仅 20%
- 采样步数 中位数 8，观测区间 4 - 10，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，9 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 er_sde，9 个样本，一致性 33%
- 调度器 最常用 beta，9 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（12/9 个样本）：Steps较低可能导致细节不足
