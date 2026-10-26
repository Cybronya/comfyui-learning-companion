---
name: image_to_image_lora_sampler_unet_127
type: Image To Image
frequency: 5
level: moderate
coverage: 0.8326
common_nodes: [CFGNorm, CLIPLoader, Image Comparer (rgthree), ImageConcanate, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit单图编辑+LLM大模型提示词（效果更加精准）_1958361112091770881.json, 图片生成/图生图/Qwen-image-edit：时光修复师，旧忆新生，完美复原！老照片修复_图像修复_图像精修_编辑_1958906559764049922.json, 图片生成/图生图/QwenEditPlus常用编辑_1978410330219024386.json, 图片生成/图生图/千问Qwen-image-edit：像素级掌控，图像编辑新纪元！图像编辑_图生图_修图_设计_1958872031519518721.json, 图片生成/图生图/最新Qwen-Image-Edit2509：指令式AI画笔，单图编辑，所指即所改！_1970432534721011714.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_127

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit单图编辑+LLM大模型提示词（效果更加精准）_1958361112091770881.json、图片生成/图生图/Qwen-image-edit：时光修复师，旧忆新生，完美复原！老照片修复_图像修复_图像精修_编辑_1958906559764049922.json、图片生成/图生图/QwenEditPlus常用编辑_1978410330219024386.json、图片生成/图生图/千问Qwen-image-edit：像素级掌控，图像编辑新纪元！图像编辑_图生图_修图_设计_1958872031519518721.json、图片生成/图生图/最新Qwen-Image-Edit2509：指令式AI画笔，单图编辑，所指即所改！_1970432534721011714.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_LLMAPI_NODE` —— 4/5 个有
- `Text Multiline` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `RepeatLatentBatch` —— 3/5 个有
- `Any Switch (rgthree)` —— 1/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `FastFilmGrain` —— 1/5 个有
- `FastLaplacianSharpen` —— 1/5 个有
- `LatentUpscaleBy` —— 1/5 个有
- `TextEncodeQwenImageEditPlus` —— 1/5 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 5 | 43% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 5 | 54% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | beta | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，5 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 beta，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
