---
name: text_to_image_lora_sampler_clip_50
type: Text To Image
frequency: 19
level: strong
coverage: 0.863158
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, SeedVR2, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2.FireRed 四视图_2083463075734319105.json, 图片生成/图生图/FireRed-Image-Edit 1.1 +Qwen2511图片编辑工作流-高清直出_2036793276518375425.json, 图片生成/图生图/FireRed-Image-Edit 1.1-[人像] 原生肌理·去AI·去塑料-电影感-高清直出_2045102299755847682.json, 图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清出图_2073975079939174402.json, 图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2045792387779272705.json, 图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2072023589460733953.json, 图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2073677104536965122.json, 图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2101942874756698113.json, 图片生成/图生图/FireRed-Image-Edit 1.1-人物面部三视图-高清直出_2079070655621976066.json, 图片生成/图生图/FireRed-Image-Edit 1.1-场景一致性_2045840113577500674.json, 图片生成/图生图/FireRed-Image-Edit 1.1-室内全景图-高清直出_2045816852143673345.json, 图片生成/图生图/FireRed-Image-Edit 1.1-户外全景图-高清直出_2045819047106846721.json, 图片生成/图生图/FireRed-Image-Edit 1.1-材质优化提升-高清直出_2045093509073473537.json, 图片生成/图生图/FireRed-Image-Edit 1.1-面部三视图-高清直出_2045087093600292865.json, 图片生成/图生图/FireRed-Image-Edit_1.1-人物面部+全身三视图-高清直出_2105120165930295297.json, 图片生成/图生图/FireRed-Image-Edit_1.1-人物面部+全身三视图-高清直出_2105497558364807170.json, 图片生成/图生图/FireRed-Image图片编辑工作流-高清直出_2038431463573561346.json, 图片生成/图生图/即梦、小云雀、豆包、超能视频2.0真人过审核方法-FireRed-Image-Edit 1.1_2036801337580589057.json, 平台全量/FireRed-Image-Edit 1.1 无缝扩图+局部重绘_2045831289651073025.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_50

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/2.FireRed 四视图_2083463075734319105.json、图片生成/图生图/FireRed-Image-Edit 1.1 +Qwen2511图片编辑工作流-高清直出_2036793276518375425.json、图片生成/图生图/FireRed-Image-Edit 1.1-[人像] 原生肌理·去AI·去塑料-电影感-高清直出_2045102299755847682.json、图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清出图_2073975079939174402.json、图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2045792387779272705.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CustomAddLabel` —— 15/19 个有
- `RunningHub Deepcleaner` —— 13/19 个有
- `GetImageSize` —— 7/19 个有
- `ImageScaleToTotalPixels` —— 7/19 个有
- `PreviewImage` —— 5/19 个有
- `easy cleanGpuUsed` —— 5/19 个有
- `DrawMaskOnImage` —— 2/19 个有
- `ImagePadForOutpaint` —— 2/19 个有
- `Label (rgthree)` —— 2/19 个有
- `DuckHideNode` —— 1/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/19 个有
- `PlaySound|pysssss` —— 1/19 个有
- `SeedVR2BlockSwap` —— 1/19 个有
- `孤海注释` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1920 | 720 - 2048 | 19 | 74% |
| 高度 | 1080 | 1024 - 1280 | 19 | 93% |
| 采样步数 | 8 | 4 - 8 | 19 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 19 | 100% |
| 采样算法 | euler | - | 19 | 95% |
| 调度器 | simple | - | 19 | 95% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1920，观测区间 720 - 2048，19 个样本
- 高度 中位数 1080，观测区间 1024 - 1280，19 个样本，取值集中（一致性 93%）
- 采样步数 中位数 8，观测区间 4 - 8，19 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，19 个样本，一致性 95%
- 调度器 最常用 simple，19 个样本，一致性 95%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 高发问题（21/19 个样本）：Steps较低可能导致细节不足
