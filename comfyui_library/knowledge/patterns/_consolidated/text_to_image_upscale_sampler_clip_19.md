---
name: text_to_image_upscale_sampler_clip_19
type: Text To Image
frequency: 7
level: moderate
coverage: 0.963429
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize+, ImageCASharpening+, ImageResize+, ImageScaleBy, KSampler, RunningHub Deepcleaner, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/很棒的动漫模型ANIMA文生图-自动提示词_2056029257322778625.json, 图片生成/文生图/艺术人像摄影超写实高清4K_-Zimage_梦幻出片1_2084906889938296834.json, 图片生成/文生图/艺术人像摄影超写实高清4K_-Zimage_梦幻出片1_2084913862234697730.json, 图片生成/文生图/顶级艺术人像摄影-Zimage_如梦似幻-Kook版_2078129341376057346.json, 视频生成/图生视频/艺术人像摄影-Zimage_4K_2085548054337380353.json, 视频生成/图生视频/艺术人像摄影-Zimage_Kook版 (2)_2085250585183477762.json, 视频生成/图生视频/艺术人像摄影-Zimage__2084823694760833026.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_19

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/很棒的动漫模型ANIMA文生图-自动提示词_2056029257322778625.json、图片生成/文生图/艺术人像摄影超写实高清4K_-Zimage_梦幻出片1_2084906889938296834.json、图片生成/文生图/艺术人像摄影超写实高清4K_-Zimage_梦幻出片1_2084913862234697730.json、图片生成/文生图/顶级艺术人像摄影-Zimage_如梦似幻-Kook版_2078129341376057346.json、视频生成/图生视频/艺术人像摄影-Zimage_4K_2085548054337380353.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `RunningHub Deepcleaner`
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
- `CR Text` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `PhotoShakeNode` —— 6/7 个有
- `PreviewImage` —— 2/7 个有
- `DuckHideNode` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `JoinStringMulti` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `RH_LLMAPI_Pro_Node` —— 1/7 个有
- `孤海注释` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 7 | 21% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 7 | 31% |
| 采样算法 | res_2s_ode | - | 7 | 86% |
| 调度器 | bong_tangent | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1080 | 1080 - 1920 | 7 | 76% |
| 高度 | 1384 | 1128 - 1384 | 7 | 93% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，7 个样本，取值分散，一致性仅 21%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，7 个样本，取值分散，一致性仅 31%
- 采样算法 最常用 res_2s_ode，7 个样本，一致性 86%
- 调度器 最常用 bong_tangent，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1920，7 个样本
- 高度 中位数 1384，观测区间 1128 - 1384，7 个样本，取值集中（一致性 93%）
- 高发问题（6/7 个样本）：Steps较低可能导致细节不足
