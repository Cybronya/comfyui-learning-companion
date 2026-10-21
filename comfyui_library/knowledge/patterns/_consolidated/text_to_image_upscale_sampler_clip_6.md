---
name: text_to_image_upscale_sampler_clip_6
type: Text To Image
frequency: 13
level: strong
coverage: 0.868077
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2基础生图+ SeedVR 4K 超清放大_2082094625946431490.json, 图片生成/文生图/Krea2文生图+SeedVR2高清放大_2079590934051901442.json, 图片生成/文生图/Z-Image + 4K超清放大_1995496468943396865.json, 图片生成/文生图/Z-Image-Turbo瑶光-超真实增强版_2067510090214760449.json, 图片生成/文生图/Z-Image-文生图-超真实细节增强_2064964807132008450.json, 图片生成/文生图/Z-Image-文生图-超真实细节增强_2065333042721411074.json, 图片生成/文生图/Z-Image-瑶光版-超真实细节_2082340410323726337.json, 图片生成/文生图/Z-Image-瑶光版-超真实细节增强+4K放大_2056677168402489346.json, 图片生成/文生图/Z-Image-瑶光版-超真实细节增强-人物四视图_2094975538946461697.json, 图片生成/文生图/Z-Image-空姐模特_2066181843638349824.json, 图片生成/文生图/ZImage+Kook大佬瑶光lora+Kook如梦似幻lora_2059586906224156674.json, 图片生成/文生图/云信短剧主角-瑶光lora_2086014484270903297.json, 视频生成/文生视频/极致电影4K美学-Krea2基础生图++SeedVR+4K+超清放大-极氪白白酱_2082122814294937602.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_6

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Krea2基础生图+ SeedVR 4K 超清放大_2082094625946431490.json、图片生成/文生图/Krea2文生图+SeedVR2高清放大_2079590934051901442.json、图片生成/文生图/Z-Image + 4K超清放大_1995496468943396865.json、图片生成/文生图/Z-Image-Turbo瑶光-超真实增强版_2067510090214760449.json、图片生成/文生图/Z-Image-文生图-超真实细节增强_2064964807132008450.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 13 个 workflow 都包含：
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
- `CLIPLoader` —— 12/13 个有
- `Image Comparer (rgthree)` —— 12/13 个有
- `ImageScaleToTotalPixels` —— 11/13 个有
- `Fast Groups Bypasser (rgthree)` —— 9/13 个有
- `INTConstant` —— 9/13 个有
- `LoraLoaderModelOnly` —— 9/13 个有
- `PreviewImage` —— 9/13 个有
- `CR Text` —— 8/13 个有
- `FastFilmGrain` —— 8/13 个有
- `LayerColor: BrightnessContrastV2` —— 8/13 个有
- `ConditioningZeroOut` —— 4/13 个有
- `MuyeTextEditOutput` —— 3/13 个有
- `CR Prompt Text` —— 2/13 个有
- `Lora Loader Stack (rgthree)` —— 2/13 个有
- `CLIPLoaderGGUF` —— 1/13 个有
- `ImageScaleBy` —— 1/13 个有
- `LayerUtility: TextJoin` —— 1/13 个有
- `LoadImage` —— 1/13 个有
- `忽略多组孤海` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 9 | 13 | 97% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | res_2s | - | 13 | 62% |
| 调度器 | bong_tangent | - | 13 | 62% |
| 重绘幅度 | 1 | 0.97 - 1 | 13 | 99% |
| 宽度 | 1080 | 1024 - 2048 | 13 | 71% |
| 高度 | 1920 | 856 - 1920 | 13 | 77% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 9，13 个样本，取值集中（一致性 97%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，13 个样本，一致性 62%
- 调度器 最常用 bong_tangent，13 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 0.97 - 1，13 个样本，取值集中（一致性 99%）
- 宽度 中位数 1080，观测区间 1024 - 2048，13 个样本
- 高度 中位数 1920，观测区间 856 - 1920，13 个样本
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
