---
name: text_to_image_lora_sampler_clip_424
type: Text To Image
frequency: 4
level: strong
coverage: 0.841
common_nodes: [AdaptiveLongestEdge_EditUtils, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, CropWithPadInfo_EditUtils, EditTextEncode_EditUtils, EmptyLatentImage, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Flux2KleinOutputExtractor_EditUtils, Flux2Scheduler, Image Comparer (rgthree), JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux Klein 9B一键无缝融图，输入主体描述上传处理图片图生图方案_2103924861985976322.json, 图片生成/图生图/服装批量改色｜FK2一致性精修图生图处理_2090202184720936961.json, 图片生成/图生图/服装批量改色｜flux2一致性精修图生图处理_2090362556530651138.json, 图片生成/图生图/服装批量改色｜flux2一致性精修图生图处理_2090617813999374337.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_424

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux Klein 9B一键无缝融图，输入主体描述上传处理图片图生图方案_2103924861985976322.json、图片生成/图生图/服装批量改色｜FK2一致性精修图生图处理_2090202184720936961.json、图片生成/图生图/服装批量改色｜flux2一致性精修图生图处理_2090362556530651138.json、图片生成/图生图/服装批量改色｜flux2一致性精修图生图处理_2090617813999374337.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `AdaptiveLongestEdge_EditUtils`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `CropWithPadInfo_EditUtils`
- `EditTextEncode_EditUtils`
- `EmptyLatentImage`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Flux2KleinOutputExtractor_EditUtils`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `GetImageSize` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `easy promptList` —— 3/4 个有
- `孤海注释` —— 2/4 个有
- `DF_Get_image_size` —— 1/4 个有
- `Text` —— 1/4 个有
- `easy promptReplace` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
