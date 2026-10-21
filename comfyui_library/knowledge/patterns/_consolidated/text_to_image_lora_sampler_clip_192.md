---
name: text_to_image_lora_sampler_clip_192
type: Text To Image
frequency: 6
level: weak
coverage: 0.8505
common_nodes: [AILab_QwenVL, AddLabel, BatchImagesNode, CLIPLoader, CLIPTextEncode, ComfySwitchNode, ConditioningZeroOut, EmptyLatentImage, EmptySD3LatentImage, GetImageSize, Image Comparer (rgthree), ImagesConcanateToGrid, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewAny, PrimitiveStringMultiline, QwenImage21Cache, ResolutionSelector, SaveImage, Seed (rgthree), TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch]
problems: [Steps较低可能导致细节不足]
missing: [Label (rgthree), easy anythingIndexSwitch, Seed (rgthree), easy promptList]
members: [图片生成/图生图/2102374646296440834.json, 图片生成/图生图/【AI军火商】Qwen Image 2.1文生图+图片编辑-实用版_2107311397913845762.json, 图片生成/文生图/Qwen Image 2.1文生图与图片编辑实用版，双模式合一的图生图工作流_2102819239848665090.json, 图片生成/文生图/Qwen Image 2.1文生图加图片编辑实用版｜生图修图一气呵成_2102590122079375361.json, 数字人/数字人/Qwen Image 2.1文生图加图片编辑实用版工作流，数字人图生图处理方案_2107983478271856641.json, 视频生成/图生视频/Qwen_Image_2.1文生图与图片编辑实用版，双模式合一的图生图工作流_2106550821646331905.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_192

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/2102374646296440834.json、图片生成/图生图/【AI军火商】Qwen Image 2.1文生图+图片编辑-实用版_2107311397913845762.json、图片生成/文生图/Qwen Image 2.1文生图与图片编辑实用版，双模式合一的图生图工作流_2102819239848665090.json、图片生成/文生图/Qwen Image 2.1文生图加图片编辑实用版｜生图修图一气呵成_2102590122079375361.json、数字人/数字人/Qwen Image 2.1文生图加图片编辑实用版工作流，数字人图生图处理方案_2107983478271856641.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `AILab_QwenVL`
- `AddLabel`
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
- `LoraLoaderModelOnly`
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
- `easy anythingIndexSwitch`

**可变部分**（部分 workflow 才有）：
- `easy promptList` —— 5/6 个有
- `JjkText` —— 4/6 个有
- `solarL_SaveImagesToZip` —— 4/6 个有
- `孤海注释` —— 3/6 个有
- `Label (rgthree)` —— 2/6 个有
- `EmptyImage` —— 1/6 个有
- `PreviewImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 25 | 6 | 10% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 6 | 51% |
| 采样算法 | er_sde | - | 6 | 67% |
| 调度器 | beta | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 1024 | 6 | 0% |
| 高度 | 80 | 80 - 1024 | 6 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 25，6 个样本，取值分散，一致性仅 10%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，6 个样本
- 采样算法 最常用 er_sde，6 个样本，一致性 67%
- 调度器 最常用 beta，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，6 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，6 个样本，取值分散，一致性仅 0%
- 高发问题（16/6 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Label (rgthree)、easy anythingIndexSwitch、Seed (rgthree)、easy promptList
