---
name: text_to_image_upscale_lora_sampler_18
type: Text To Image
frequency: 10
level: strong
coverage: 0.8159
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Text-to-Image_ Ultra-High Definition文生图高清极致真实感_2101483367073148930.json, 图片生成/文生图/Z-Image文生图+TTP高清放大_2059978387187388417.json, 图片生成/文生图/ZImage文生图（TTP高清4K）_2096553840748355585.json, 图片生成/文生图/krea2基础文生图高清_2102596196979269634.json, 图片生成/文生图/krea2文生图高清_2081557717600260097.json, 图片生成/文生图/krea2文生图高清_2081698530154082306.json, 图片生成/文生图/人像写真 美图生成洗图 虚拟美女模特 Z-Image文生图_提示词反推+SeedVR2TTP高清放大_2060190994372579329.json, 图片生成/文生图/壮男熊熊lora版-Krea2 Turbo+Realism Engineer V2文生图_2074491759014535169.json, 图片生成/文生图/高清极致真实感-Krea2 Turbo+Realism Engineer V2文生图_2072233474878169090.json, 图片生成/文生图/高清极致真实感-Krea2 Turbo+Realism Engineer V2文生图_2074410090194628609.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_18

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Text-to-Image_ Ultra-High Definition文生图高清极致真实感_2101483367073148930.json、图片生成/文生图/Z-Image文生图+TTP高清放大_2059978387187388417.json、图片生成/文生图/ZImage文生图（TTP高清4K）_2096553840748355585.json、图片生成/文生图/krea2基础文生图高清_2102596196979269634.json、图片生成/文生图/krea2文生图高清_2081557717600260097.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
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
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 7/10 个有
- `easy cleanGpuUsed` —— 7/10 个有
- `SetNode` —— 6/10 个有
- `PreviewAny` —— 5/10 个有
- `Fast Groups Bypasser (rgthree)` —— 4/10 个有
- `PrimitiveStringMultiline` —— 4/10 个有
- `ResolutionSelector` —— 4/10 个有
- `StringConcatenate` —— 4/10 个有
- `TextGenerate` —— 4/10 个有
- `ConstrainImage|pysssss` —— 3/10 个有
- `Get Image Size` —— 3/10 个有
- `孤海注释` —— 3/10 个有
- `CLIPLoaderGGUF` —— 2/10 个有
- `LoadImage` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `RH_Captioner` —— 2/10 个有
- `VAEEncode` —— 2/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 10 | 10 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 70% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 0.25 - 1 | 10 | 65% |
| 宽度 | 1024 | 1024 - 1024 | 10 | 100% |
| 高度 | 1024 | 1024 - 1536 | 10 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 10，10 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 70%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.25 - 1，10 个样本
- 宽度 中位数 1024，观测区间 1024 - 1024，10 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1536，10 个样本，取值集中（一致性 80%）
- 高发问题（9/10 个样本）：Steps较低可能导致细节不足
