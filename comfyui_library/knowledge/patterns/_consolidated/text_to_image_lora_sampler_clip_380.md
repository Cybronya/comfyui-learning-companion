---
name: text_to_image_lora_sampler_clip_380
type: Text To Image
frequency: 5
level: strong
coverage: 0.8382
common_nodes: [BatchImagesNode, CLIPLoader, CLIPTextEncode, CenterCropImages, EmptyImage, EmptyLatentImage, GetImageSize, GetNode, ImageFromBatch, ImageScaleBy, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, ResolutionSelector, SaveImage, SetNode, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy forLoopEnd, easy forLoopStart, easy imageSplitGrid, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1 Storyboard 2K Upscale分镜加超分，图生图高清处理工_2105811626178998273.json, 图片生成/图生图/Qwen Image 2.1短剧真人写实角色卡生成器，人设立绘快速批量出图_2114457440451383298.json, 图片生成/图生图/qwen image 2.1 storyboard 2k upscale 分镜加超分_2105128611027177473.json, 图片生成/图生图/qwen_image角色数据分镜图生图，2k放大一键出故事板_2110458197722095617.json, 图片生成/图生图/qwen_image角色数据分镜图生图，2k放大一键出故事板_2113471622056337409.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_380

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 Storyboard 2K Upscale分镜加超分，图生图高清处理工_2105811626178998273.json、图片生成/图生图/Qwen Image 2.1短剧真人写实角色卡生成器，人设立绘快速批量出图_2114457440451383298.json、图片生成/图生图/qwen image 2.1 storyboard 2k upscale 分镜加超分_2105128611027177473.json、图片生成/图生图/qwen_image角色数据分镜图生图，2k放大一键出故事板_2110458197722095617.json、图片生成/图生图/qwen_image角色数据分镜图生图，2k放大一键出故事板_2113471622056337409.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CenterCropImages`
- `EmptyImage`
- `EmptyLatentImage`
- `GetImageSize`
- `GetNode`
- `ImageFromBatch`
- `ImageScaleBy`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ResolutionSelector`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageSplitGrid`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 4/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
