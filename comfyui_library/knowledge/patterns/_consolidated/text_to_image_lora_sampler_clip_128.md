---
name: text_to_image_lora_sampler_clip_128
type: Text To Image
frequency: 12
level: weak
coverage: 0.87025
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2083752313956687874.json, 图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2101942874756698113.json, 图片生成/图生图/FireRed-Image-Edit 1.1-室内全景图-高清直出_2045816852143673345.json, 图片生成/图生图/FireRed-Image-Edit 1.1-户外全景图-高清直出_2045819047106846721.json, 图片生成/图生图/FireRed-Image-Edit 1.1-材质优化提升-高清直出_2045093509073473537.json, 图片生成/图生图/FireRed-Image-Edit_1.1-人物面部+全身三视图-高清直出_2105120165930295297.json, 图片生成/图生图/FireRed-Image-Edit_1.1-人物面部+全身三视图-高清直出_2105497558364807170.json, 图片生成/图生图/MOSS-Image人物三视图生成，面部+全身多角度高清直出角色设计利器_2114426707334746114.json, 图片生成/图生图/Moss-Image-人物面部+全身三视图-高清直出_2113912819136679938.json, 图片生成/图生图/Moss-Image-人物面部+全身三视图-高清直出｜人物角色图生图_2114297170357739522.json, 图片生成/图生图/Qwen Edit 2511单图编辑全能手｜电商产品个人写真都能改｜局部重绘精细_2102611970536067073.json, 图片生成/图生图/Qwen Edit 2511电商产品图编辑利器｜个人照片也能精修｜写实风局部重绘_2102615492870631426.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_128

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2083752313956687874.json、图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2101942874756698113.json、图片生成/图生图/FireRed-Image-Edit 1.1-室内全景图-高清直出_2045816852143673345.json、图片生成/图生图/FireRed-Image-Edit 1.1-户外全景图-高清直出_2045819047106846721.json、图片生成/图生图/FireRed-Image-Edit 1.1-材质优化提升-高清直出_2045093509073473537.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RunningHub Deepcleaner` —— 9/12 个有
- `SeedVR2` —— 9/12 个有
- `CustomAddLabel` —— 6/12 个有
- `孤海注释` —— 6/12 个有
- `ImageScaleToTotalPixels` —— 4/12 个有
- `solarL_SaveImagesToZip` —— 4/12 个有
- `Image Comparer (rgthree)` —— 3/12 个有
- `SeedVR2LoadDiTModel` —— 3/12 个有
- `SeedVR2LoadVAEModel` —— 3/12 个有
- `SeedVR2VideoUpscaler` —— 3/12 个有
- `CheckpointLoaderSimple` —— 2/12 个有
- `GetImageSizeAndCount` —— 2/12 个有
- `ImageConcanate` —— 2/12 个有
- `ImageScaleBy` —— 2/12 个有
- `Text Multiline` —— 2/12 个有
- `GetImageSize` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 12 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 12 | 24% |
| 采样算法 | euler | - | 12 | 67% |
| 调度器 | simple | - | 12 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 1920 | 80 - 2048 | 12 | 33% |
| 高度 | 1052 | 80 - 1080 | 12 | 37% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，12 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 euler，12 个样本，一致性 67%
- 调度器 最常用 simple，12 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 1920，观测区间 80 - 2048，12 个样本，取值分散，一致性仅 33%
- 高度 中位数 1052，观测区间 80 - 1080，12 个样本，取值分散，一致性仅 37%
- 高发问题（16/12 个样本）：Steps较低可能导致细节不足
