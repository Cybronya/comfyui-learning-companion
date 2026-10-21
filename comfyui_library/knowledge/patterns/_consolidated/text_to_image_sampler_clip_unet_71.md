---
name: text_to_image_sampler_clip_unet_71
type: Text To Image
frequency: 7
level: weak
coverage: 0.966714
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Ovis-Image 海报设计工作流_1997462628240932866.json, 图片生成/文生图/Ovis-image文生图工作流_1996530154350452738.json, 图片生成/文生图/Red-Z image Base-10步出图极速版_2018674863816318977.json, 图片生成/文生图/Text to Image _ Z-IMAGE_1993955627510726657.json, 图片生成/文生图/Z-Image 超强文生图_1993850615438704641.json, 图片生成/文生图/Z-image+SeedVR2-文生图-图片放大-高清直出_2021747203928236033.json, 图片生成/文生图/Z-image+SeedVR2-文生图-高清出图_2081632081444167681.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_71

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Ovis-Image 海报设计工作流_1997462628240932866.json、图片生成/文生图/Ovis-image文生图工作流_1996530154350452738.json、图片生成/文生图/Red-Z image Base-10步出图极速版_2018674863816318977.json、图片生成/文生图/Text to Image _ Z-IMAGE_1993955627510726657.json、图片生成/文生图/Z-Image 超强文生图_1993850615438704641.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/7 个有
- `Int` —— 3/7 个有
- `CR SDXL Aspect Ratio` —— 2/7 个有
- `Label (rgthree)` —— 2/7 个有
- `LayerUtility: PurgeVRAM V2` —— 2/7 个有
- `SeedVR2` —— 2/7 个有
- `Textbox` —— 2/7 个有
- `CustomAddLabel` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `ModelSamplingFlux` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 50 | 7 | 16% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 7 | 16% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1024 | 720 - 1080 | 7 | 88% |
| 高度 | 1280 | 576 - 1920 | 7 | 65% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 50，7 个样本，取值分散，一致性仅 16%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，7 个样本，取值分散，一致性仅 16%
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 720 - 1080，7 个样本，取值集中（一致性 88%）
- 高度 中位数 1280，观测区间 576 - 1920，7 个样本
