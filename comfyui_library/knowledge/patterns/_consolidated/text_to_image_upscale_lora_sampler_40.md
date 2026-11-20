---
name: text_to_image_upscale_lora_sampler_40
type: Text To Image
frequency: 7
level: strong
coverage: 0.839
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), ImageResize+, ImageScaleBy, JjkText, KSampler, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy imageSize, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1文生图图生视频高清工作流合集处理工具_2102497280900296705.json, 图片生成/文生图/Qwen-Image-2.1 亚洲人像摄影胶片｜复古质感写真直出_2112382443893387265.json, 图片生成/文生图/Qwen2.1 亚洲摄影人像写真｜4K高清直出质感大片_2112369800302387201.json, 图片生成/文生图/Qwen2.1文生图与图像编辑合集，开源新王t2i i2i多场景覆盖_2103238483472113665.json, 图片生成/文生图/Qwen2.1文生图加图生视频高清合集｜图片视频双修工作流包｜一次收齐_2102244573996212225.json, 图片生成/文生图/Qwen2.1文生图图生视频高清工作流合集V2，多场景覆盖方案_2103548965714223106.json, 图片生成/文生图/千问Qwen2.1文生图图像编辑合集，开源图像新王多场景覆盖方案_2106101872363921410.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_40

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1文生图图生视频高清工作流合集处理工具_2102497280900296705.json、图片生成/文生图/Qwen-Image-2.1 亚洲人像摄影胶片｜复古质感写真直出_2112382443893387265.json、图片生成/文生图/Qwen2.1 亚洲摄影人像写真｜4K高清直出质感大片_2112369800302387201.json、图片生成/文生图/Qwen2.1文生图与图像编辑合集，开源新王t2i i2i多场景覆盖_2103238483472113665.json、图片生成/文生图/Qwen2.1文生图加图生视频高清合集｜图片视频双修工作流包｜一次收齐_2102244573996212225.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 5/7 个有
- `LoadImage` —— 5/7 个有
- `ImageConcatMulti` —— 3/7 个有
- `CR Prompt Text` —— 2/7 个有
- `Color Grading JK` —— 2/7 个有
- `Int` —— 2/7 个有
- `LayerUtility: PurgeVRAM` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `PrimitiveStringMultiline` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（11/7 个样本）：Steps较低可能导致细节不足
