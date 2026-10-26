---
name: image_to_image_lora_sampler_unet_136
type: Image To Image
frequency: 5
level: strong
coverage: 0.8368
common_nodes: [CLIPLoader, EmptySD3LatentImage, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/图像编辑 Krea2 Identity 单_双图编辑_2081923868243095554.json, 图片生成/图生图/图片编辑 单_双图编辑 Krea2-Identity_2081930115990253569.json, 图片生成/文生图/pipi-krea2单图编辑单图洗图换图片元素改图改元素洗图神器_2089518838948917250.json, 图片生成/文生图/pipi-krea2换装编辑工作流换衣服模特换装人物换衣换装图片工作流_2089518265252012034.json, 数字人/数字人/Krea2 人物定妆照_2092034511797309441.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_136

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/图像编辑 Krea2 Identity 单_双图编辑_2081923868243095554.json、图片生成/图生图/图片编辑 单_双图编辑 Krea2-Identity_2081930115990253569.json、图片生成/文生图/pipi-krea2单图编辑单图洗图换图片元素改图改元素洗图神器_2089518838948917250.json、图片生成/文生图/pipi-krea2换装编辑工作流换衣服模特换装人物换衣换装图片工作流_2089518265252012034.json、数字人/数字人/Krea2 人物定妆照_2092034511797309441.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `String Literal` —— 2/5 个有
- `easy imageSize` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
