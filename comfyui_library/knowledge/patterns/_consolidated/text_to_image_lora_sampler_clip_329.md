---
name: text_to_image_lora_sampler_clip_329
type: Text To Image
frequency: 6
level: strong
coverage: 0.904333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, ConditioningZeroOut, DF_Text_Box, EmptyLatentImage, Flux2Scheduler, GH_CropRestore, GH_MaskCropV2, GetImageSize+, GuHaiMaskDetect, Image Comparer (rgthree), JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, Mask Invert, RandomNoise, ReferenceLatent, SAM3Segment, SamplerCustomAdvanced, SaveImage, SimpleMath+, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy ifElse, solarL_SaveImagesToZip, 图像缩放V2_孤海, 孤海-遮罩混合运算, 孤海遮罩分析, 布尔孤海, 数学运算_孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Klein换发型V2 单人多人全身换发型处理工具_2099950966194921473.json, 图片生成/图生图/Klein换发型V2_单人多人全身换发型处理工具_2100514929504768001.json, 图片生成/图生图/Klein换发型V2处理工具｜单人多人全身换发型_2100853756182224898.json, 图片生成/图生图/klein换发型换头工作流｜图生图换脸快速出图_2100821675100164098.json, 图片生成/图生图/双人照片一键影棚合影｜Klein 9B全家福合成工作流_2096329930433974274.json, 图片生成/图生图/换发型V2-klein版来了｜头发替换自然服帖，发色发型随便试_2099437858925928449.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_329

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Klein换发型V2 单人多人全身换发型处理工具_2099950966194921473.json、图片生成/图生图/Klein换发型V2_单人多人全身换发型处理工具_2100514929504768001.json、图片生成/图生图/Klein换发型V2处理工具｜单人多人全身换发型_2100853756182224898.json、图片生成/图生图/klein换发型换头工作流｜图生图换脸快速出图_2100821675100164098.json、图片生成/图生图/双人照片一键影棚合影｜Klein 9B全家福合成工作流_2096329930433974274.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `DF_Text_Box`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GH_CropRestore`
- `GH_MaskCropV2`
- `GetImageSize+`
- `GuHaiMaskDetect`
- `Image Comparer (rgthree)`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `Mask Invert`
- `RandomNoise`
- `ReferenceLatent`
- `SAM3Segment`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy ifElse`
- `solarL_SaveImagesToZip`
- `图像缩放V2_孤海`
- `孤海-遮罩混合运算`
- `孤海遮罩分析`
- `布尔孤海`
- `数学运算_孤海`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 5/6 个有
- `EmptyImage` —— 3/6 个有
- `PreviewImage` —— 3/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足
