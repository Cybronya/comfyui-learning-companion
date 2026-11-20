---
name: image_to_image_lora_sampler_clip_35
type: Image To Image
frequency: 9
level: strong
coverage: 0.918778
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext渲染级光影重塑产品精修_1977993025672597505.json, 图片生成/图生图/Kontext窗帘溶图v2_2064172765846003714.json, 图片生成/图生图/Kontext窗帘移除_2065682037486473217.json, 图片生成/图生图/Kontext窗帘风景提取_2064271356920942593.json, 图片生成/图生图/Kontext首饰溶图_1992752723617533953.json, 图片生成/图生图/Q-四宫格表情包_1962753115034370050.json, 图片生成/图生图/kontext服装精修_2020008788572512257.json, 图片生成/图生图/个人用精修_2061776161872633857.json, 平台全量/Kontext渲染级光影重塑产品精修_2060876540610699266.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_35

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Kontext渲染级光影重塑产品精修_1977993025672597505.json、图片生成/图生图/Kontext窗帘溶图v2_2064172765846003714.json、图片生成/图生图/Kontext窗帘移除_2065682037486473217.json、图片生成/图生图/Kontext窗帘风景提取_2064271356920942593.json、图片生成/图生图/Kontext首饰溶图_1992752723617533953.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 9 个 workflow 都包含：
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
- `ConstrainImage|pysssss` —— 7/9 个有
- `Image Comparer (rgthree)` —— 6/9 个有
- `Image Filter Adjustments` —— 3/9 个有
- `SimpleMathSlider+` —— 3/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `CropFace` —— 1/9 个有
- `ImageConcatMulti` —— 1/9 个有
- `ImpactInt` —— 1/9 个有
- `MagCache` —— 1/9 个有
- `easy imageInsetCrop` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 30 | 9 | 85% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | ddim_uniform | - | 9 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 30，9 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 ddim_uniform，9 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
