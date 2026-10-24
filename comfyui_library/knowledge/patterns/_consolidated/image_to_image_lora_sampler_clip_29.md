---
name: image_to_image_lora_sampler_clip_29
type: Image To Image
frequency: 8
level: strong
coverage: 0.934625
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext渲染级光影重塑产品精修_1977993025672597505.json, 图片生成/图生图/Kontext窗帘溶图v2_2064172765846003714.json, 图片生成/图生图/Kontext窗帘移除_2065682037486473217.json, 图片生成/图生图/Kontext窗帘风景提取_2064271356920942593.json, 图片生成/图生图/Kontext首饰溶图_1992752723617533953.json, 图片生成/图生图/Q-四宫格表情包_1962753115034370050.json, 图片生成/图生图/QY7-千像归一（kontext）单图版 一键融合打光，溶图kontext_1967603421962526721.json, 图片生成/图生图/个人用精修_2061776161872633857.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_29

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Kontext渲染级光影重塑产品精修_1977993025672597505.json、图片生成/图生图/Kontext窗帘溶图v2_2064172765846003714.json、图片生成/图生图/Kontext窗帘移除_2065682037486473217.json、图片生成/图生图/Kontext窗帘风景提取_2064271356920942593.json、图片生成/图生图/Kontext首饰溶图_1992752723617533953.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
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
- `ConstrainImage|pysssss` —— 5/8 个有
- `Image Comparer (rgthree)` —— 5/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/8 个有
- `Image Filter Adjustments` —— 2/8 个有
- `SimpleMathSlider+` —— 2/8 个有
- `CropFace` —— 1/8 个有
- `ImpactInt` —— 1/8 个有
- `MagCache` —— 1/8 个有
- `Note Plus (mtb)` —— 1/8 个有
- `PlaySound|pysssss` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `easy imageInsetCrop` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 27.5 | 20 - 30 | 8 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 75% |
| 调度器 | ddim_uniform | - | 8 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 27.5，观测区间 20 - 30，8 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 75%
- 调度器 最常用 ddim_uniform，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
