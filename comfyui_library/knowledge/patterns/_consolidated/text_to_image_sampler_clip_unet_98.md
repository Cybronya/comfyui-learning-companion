---
name: text_to_image_sampler_clip_unet_98
type: Text To Image
frequency: 7
level: weak
coverage: 0.861714
common_nodes: [BatchImagesNode, CLIPLoader, CLIPTextEncode, ComfySwitchNode, ConditioningZeroOut, EmptyLatentImage, EmptySD3LatentImage, GetImageSize, Image Comparer (rgthree), ImagesConcanateToGrid, KSampler, LoadImage, ModelSamplingAuraFlow, PreviewAny, PrimitiveStringMultiline, QwenImage21Cache, ResolutionSelector, SaveImage, Seed (rgthree), TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1文生图+图片编辑-实用版_2102374646296440834.json, 图片生成/图生图/【AI军火商】Qwen Image 2.1文生图+图片编辑-实用版_2107311397913845762.json, 图片生成/图生图/图片批次与图片列表_2113602731146563585.json, 图片生成/文生图/Qwen Image 2.1文生图与图片编辑实用版，双模式合一的图生图工作流_2102819239848665090.json, 图片生成/文生图/Qwen Image 2.1文生图加图片编辑实用版｜生图修图一气呵成_2102590122079375361.json, 数字人/数字人/Qwen Image 2.1文生图加图片编辑实用版工作流，数字人图生图处理方案_2107983478271856641.json, 视频生成/图生视频/Qwen_Image_2.1文生图与图片编辑实用版，双模式合一的图生图工作流_2106550821646331905.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_98

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1文生图+图片编辑-实用版_2102374646296440834.json、图片生成/图生图/【AI军火商】Qwen Image 2.1文生图+图片编辑-实用版_2107311397913845762.json、图片生成/图生图/图片批次与图片列表_2113602731146563585.json、图片生成/文生图/Qwen Image 2.1文生图与图片编辑实用版，双模式合一的图生图工作流_2102819239848665090.json、图片生成/文生图/Qwen Image 2.1文生图加图片编辑实用版｜生图修图一气呵成_2102590122079375361.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImagesConcanateToGrid`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `Seed (rgthree)`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 6/7 个有
- `AddLabel` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `easy anythingIndexSwitch` —— 6/7 个有
- `easy promptList` —— 5/7 个有
- `JjkText` —— 4/7 个有
- `solarL_SaveImagesToZip` —— 4/7 个有
- `Label (rgthree)` —— 3/7 个有
- `孤海注释` —— 3/7 个有
- `PreviewImage` —— 2/7 个有
- `CR SDXL Aspect Ratio` —— 1/7 个有
- `CreateList` —— 1/7 个有
- `EmptyFlux2LatentImage` —— 1/7 个有
- `EmptyImage` —— 1/7 个有
- `easy imageBatchToImageList` —— 1/7 个有
- `easy imageListToImageBatch` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 25 | 7 | 20% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 7 | 42% |
| 采样算法 | er_sde | - | 7 | 57% |
| 调度器 | beta | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 1024 | 7 | 4% |
| 高度 | 80 | 80 - 1024 | 7 | 4% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 25，7 个样本，取值分散，一致性仅 20%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，7 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 er_sde，7 个样本，一致性 57%
- 调度器 最常用 beta，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，7 个样本，取值分散，一致性仅 4%
- 高度 中位数 80，观测区间 80 - 1024，7 个样本，取值分散，一致性仅 4%
- 高发问题（17/7 个样本）：Steps较低可能导致细节不足
