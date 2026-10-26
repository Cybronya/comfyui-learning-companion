---
name: image_to_image_lora_sampler_clip_39
type: Image To Image
frequency: 7
level: strong
coverage: 0.922
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext-Place it产品融图_1947940421021380609.json, 图片生成/图生图/Kontext-put it here产品替换_1948620293857247233.json, 图片生成/图生图/Kontext-一键转画风_1948255124436201474.json, 图片生成/图生图/Kontext-图片精修_1960220426934890498.json, 图片生成/图生图/Kontext-静物图提取lora_1960182192410406913.json, 图片生成/图生图/PS高阶-光影优化V2_1963143771179429889.json, 图片生成/图生图/QY7-千像归一（kontext）单图版 一键融合打光，溶图kontext_1967603421962526721.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_39

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Kontext-Place it产品融图_1947940421021380609.json、图片生成/图生图/Kontext-put it here产品替换_1948620293857247233.json、图片生成/图生图/Kontext-一键转画风_1948255124436201474.json、图片生成/图生图/Kontext-图片精修_1960220426934890498.json、图片生成/图生图/Kontext-静物图提取lora_1960182192410406913.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
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
- `FluxKontextImageScale` —— 5/7 个有
- `ImageConcatMulti` —— 4/7 个有
- `easy imageScaleDownToSize` —— 4/7 个有
- `Note Plus (mtb)` —— 3/7 个有
- `JjkShowText` —— 2/7 个有
- `Label (rgthree)` —— 2/7 个有
- `RH_Translator` —— 2/7 个有
- `Text Find and Replace` —— 2/7 个有
- `TextInput_` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `PlaySound|pysssss` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
