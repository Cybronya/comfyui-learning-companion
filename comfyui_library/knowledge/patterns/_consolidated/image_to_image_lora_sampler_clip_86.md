---
name: image_to_image_lora_sampler_clip_86
type: Image To Image
frequency: 5
level: strong
coverage: 0.824
common_nodes: [Anything Everywhere3, CLIPTextEncode, CR Text, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, RH_Translator, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/光影-梦幻光影-工作流_1955142308644601858.json, 图片生成/图生图/光影-梦幻光影-工作流_1965767182925893633.json, 图片生成/图生图/梦幻光影-多彩打光-图生图_2031907252721946625.json, 平台全量/flux kontext 单图示例（包含擦除，转绘，添加，修复，去水印等15个示例）_1937171150583840769.json, 平台全量/光影-梦幻光影-工作流_1949026453221453825.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_86

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/光影-梦幻光影-工作流_1955142308644601858.json、图片生成/图生图/光影-梦幻光影-工作流_1965767182925893633.json、图片生成/图生图/梦幻光影-多彩打光-图生图_2031907252721946625.json、平台全量/flux kontext 单图示例（包含擦除，转绘，添加，修复，去水印等15个示例）_1937171150583840769.json、平台全量/光影-梦幻光影-工作流_1949026453221453825.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RH_Translator`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImpactSwitch` —— 4/5 个有
- `LayerUtility: PurgeVRAM V2` —— 4/5 个有
- `ModelSamplingFlux` —— 4/5 个有
- `NunchakuFluxDiTLoader` —— 4/5 个有
- `NunchakuFluxLoraLoader` —— 4/5 个有
- `Text Find and Replace` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `DeepTranslatorTextNode` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `UnetLoaderGGUF` —— 1/5 个有
- `easy seed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 9 - 20 | 5 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | normal | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 9 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 normal，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（15/5 个样本）：Steps较低可能导致细节不足
