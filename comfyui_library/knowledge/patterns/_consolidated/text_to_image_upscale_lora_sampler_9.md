---
name: text_to_image_upscale_lora_sampler_9
type: Text To Image
frequency: 8
level: weak
coverage: 0.775375
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetNode, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, LoraLoaderModelOnly, ResolutionSelector, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen2.1文生图与图像编辑合集，开源新王t2i i2i多场景覆盖_2103238483472113665.json, 图片生成/文生图/Qwen2.1文生图加图生视频高清合集｜图片视频双修工作流包｜一次收齐_2102244573996212225.json, 图片生成/文生图/Qwen2.1文生图图生视频高清工作流合集V2，多场景覆盖方案_2103548965714223106.json, 图片生成/文生图/Text-to-Image_ Ultra-High Definition文生图高清极致真实感_2101483367073148930.json, 图片生成/文生图/千问Qwen2.1文生图图像编辑合集，开源图像新王多场景覆盖方案_2106101872363921410.json, 图片生成/文生图/壮男熊熊lora版-Krea2 Turbo+Realism Engineer V2文生图_2074491759014535169.json, 图片生成/文生图/高清极致真实感-Krea2 Turbo+Realism Engineer V2文生图_2072233474878169090.json, 图片生成/文生图/高清极致真实感-Krea2 Turbo+Realism Engineer V2文生图_2074410090194628609.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_9

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Qwen2.1文生图与图像编辑合集，开源新王t2i i2i多场景覆盖_2103238483472113665.json、图片生成/文生图/Qwen2.1文生图加图生视频高清合集｜图片视频双修工作流包｜一次收齐_2102244573996212225.json、图片生成/文生图/Qwen2.1文生图图生视频高清工作流合集V2，多场景覆盖方案_2103548965714223106.json、图片生成/文生图/Text-to-Image_ Ultra-High Definition文生图高清极致真实感_2101483367073148930.json、图片生成/文生图/千问Qwen2.1文生图图像编辑合集，开源图像新王多场景覆盖方案_2106101872363921410.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 7/8 个有
- `PrimitiveStringMultiline` —— 6/8 个有
- `Fast Groups Bypasser (rgthree)` —— 5/8 个有
- `LoadImage` —— 5/8 个有
- `Any Switch (rgthree)` —— 4/8 个有
- `ComfySwitchNode` —— 4/8 个有
- `ConditioningZeroOut` —— 4/8 个有
- `JjkText` —— 4/8 个有
- `PreviewAny` —— 4/8 个有
- `QwenImage21Cache` —— 4/8 个有
- `StringConcatenate` —— 4/8 个有
- `TextEncodeQwenImage21` —— 4/8 个有
- `TextGenerate` —— 4/8 个有
- `easy cleanGpuUsed` —— 4/8 个有
- `solarL_SaveImagesToZip` —— 4/8 个有
- `ImageConcatMulti` —— 2/8 个有
- `Int` —— 2/8 个有
- `RH_Captioner` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 552 | 80 - 1024 | 8 | 14% |
| 高度 | 552 | 80 - 1024 | 8 | 14% |
| 采样步数 | 6 | 4 - 8 | 8 | 67% |
| Prompt 约束强度(CFG) | 2.75 | 1 - 4.5 | 8 | 36% |
| 采样算法 | er_sde | - | 8 | 50% |
| 调度器 | beta | - | 8 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 552，观测区间 80 - 1024，8 个样本，取值分散，一致性仅 14%
- 高度 中位数 552，观测区间 80 - 1024，8 个样本，取值分散，一致性仅 14%
- 采样步数 中位数 6，观测区间 4 - 8，8 个样本
- Prompt 约束强度(CFG) 中位数 2.75，观测区间 1 - 4.5，8 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 er_sde，8 个样本，一致性 50%
- 调度器 最常用 beta，8 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（10/8 个样本）：Steps较低可能导致细节不足
