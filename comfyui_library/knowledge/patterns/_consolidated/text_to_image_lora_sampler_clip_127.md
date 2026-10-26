---
name: text_to_image_lora_sampler_clip_127
type: Text To Image
frequency: 12
level: strong
coverage: 0.865917
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2.FireRed 四视图_2083463075734319105.json, 图片生成/图生图/FireRed-Image-Edit 1.1 +Qwen2511图片编辑工作流-高清直出_2036793276518375425.json, 图片生成/图生图/FireRed-Image-Edit 1.1-[人像] 原生肌理·去AI·去塑料-电影感-高清直出_2045102299755847682.json, 图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清出图_2073975079939174402.json, 图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2045792387779272705.json, 图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2072023589460733953.json, 图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2073677104536965122.json, 图片生成/图生图/FireRed-Image-Edit 1.1-人物面部三视图-高清直出_2079070655621976066.json, 图片生成/图生图/FireRed-Image-Edit 1.1-场景一致性_2045840113577500674.json, 图片生成/图生图/FireRed-Image-Edit 1.1-面部三视图-高清直出_2045087093600292865.json, 图片生成/图生图/FireRed-Image图片编辑工作流-高清直出_2038431463573561346.json, 图片生成/图生图/FireRed_Edit图像编辑与扩图重绘_2026977014363721729.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_127

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/2.FireRed 四视图_2083463075734319105.json、图片生成/图生图/FireRed-Image-Edit 1.1 +Qwen2511图片编辑工作流-高清直出_2036793276518375425.json、图片生成/图生图/FireRed-Image-Edit 1.1-[人像] 原生肌理·去AI·去塑料-电影感-高清直出_2045102299755847682.json、图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清出图_2073975079939174402.json、图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2045792387779272705.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 11/12 个有
- `SeedVR2` —— 11/12 个有
- `CustomAddLabel` —— 7/12 个有
- `RunningHub Deepcleaner` —— 7/12 个有
- `GetImageSize` —— 5/12 个有
- `ImageScaleToTotalPixels` —— 5/12 个有
- `PreviewImage` —— 5/12 个有
- `easy cleanGpuUsed` —— 4/12 个有
- `DrawMaskOnImage` —— 2/12 个有
- `ImagePadForOutpaint` —— 2/12 个有
- `DuckHideNode` —— 1/12 个有
- `Fast Groups Muter (rgthree)` —— 1/12 个有
- `Label (rgthree)` —— 1/12 个有
- `PlaySound|pysssss` —— 1/12 个有
- `SeedVR2BlockSwap` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1920 | 720 - 2048 | 12 | 68% |
| 高度 | 1080 | 1024 - 1280 | 12 | 92% |
| 采样步数 | 8 | 4 - 8 | 12 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 92% |
| 调度器 | simple | - | 12 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1920，观测区间 720 - 2048，12 个样本
- 高度 中位数 1080，观测区间 1024 - 1280，12 个样本，取值集中（一致性 92%）
- 采样步数 中位数 8，观测区间 4 - 8，12 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 92%
- 调度器 最常用 simple，12 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（16/12 个样本）：Steps较低可能导致细节不足
