---
name: image_to_image_lora_sampler_clip_94
type: Image To Image
frequency: 3
level: strong
coverage: 0.895667
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext-Place it产品融图_1947940421021380609.json, 图片生成/图生图/Kontext-Relighting-重新打光-实现艺术照打光自由V1_2029902628368420865.json, 图片生成/图生图/Kontext-put it here产品替换_1948620293857247233.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_94

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Kontext-Place it产品融图_1947940421021380609.json、图片生成/图生图/Kontext-Relighting-重新打光-实现艺术照打光自由V1_2029902628368420865.json、图片生成/图生图/Kontext-put it here产品替换_1948620293857247233.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkShowText` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `Note Plus (mtb)` —— 2/3 个有
- `RH_Translator` —— 2/3 个有
- `Text Find and Replace` —— 2/3 个有
- `TextInput_` —— 2/3 个有
- `ConstrainImage|pysssss` —— 1/3 个有
- `GLM_Translation_Text` —— 1/3 个有
- `UltimateSDUpscale` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
