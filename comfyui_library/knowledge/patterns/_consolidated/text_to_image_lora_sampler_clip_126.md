---
name: text_to_image_lora_sampler_clip_126
type: Text To Image
frequency: 7
level: strong
coverage: 0.811143
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageScaleToTotalPixels, JjkText, KSampler, LoraLoaderModelOnly, PrimitiveStringMultiline, ResolutionSelector, SaveImage, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [ShowAnything|Mie]
members: [图片生成/图生图/2102552758141411330.json, 图片生成/文生图/Qwen Image 2.1多功能官方流，文生图图生图多场景覆盖方案_2106450449720238081.json, 图片生成/文生图/Qwen Image 2.1官流文生图｜多图编辑一站式搞定_2106637714182459393.json, 图片生成/文生图/Qwen image 2.1文生图全套｜模型节点下载链接都备齐_2103098595393228801.json, 图片生成/文生图/Qwen image 2.1文生图带模型节点下载链接 新手友好_2104780019913543682.json, 图片生成/文生图/Qwen image 2.1文生图教程版｜附模型和节点下载链接，开箱即用_2104549164205039618.json, 图片生成/文生图/qwen-image2.1多功能官流整合｜文生图图生图一套全搞定_2106233388154839041.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_126

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/2102552758141411330.json、图片生成/文生图/Qwen Image 2.1多功能官方流，文生图图生图多场景覆盖方案_2106450449720238081.json、图片生成/文生图/Qwen Image 2.1官流文生图｜多图编辑一站式搞定_2106637714182459393.json、图片生成/文生图/Qwen image 2.1文生图全套｜模型节点下载链接都备齐_2103098595393228801.json、图片生成/文生图/Qwen image 2.1文生图带模型节点下载链接 新手友好_2104780019913543682.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 6/7 个有
- `PreviewAny` —— 6/7 个有
- `BatchImagesNode` —— 4/7 个有
- `ComfySwitchNode` —— 4/7 个有
- `LoadImage` —— 4/7 个有
- `PrimitiveBoolean` —— 4/7 个有
- `QwenImage21Cache` —— 4/7 个有
- `RegexExtract` —— 4/7 个有
- `SeedVR2LoadDiTModel` —— 4/7 个有
- `SeedVR2LoadVAEModel` —— 4/7 个有
- `SeedVR2VideoUpscaler` —— 4/7 个有
- `GetImageSize` —— 3/7 个有
- `ImageResizeKJv2` —— 3/7 个有
- `ModelAttentionBackend` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `PrimitiveInt` —— 3/7 个有
- `Seed (rgthree)` —— 3/7 个有
- `StringConcatenate` —— 3/7 个有
- `ShowAnything|Mie` —— 1/7 个有
- `StringFormat` —— 1/7 个有

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
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：ShowAnything|Mie
