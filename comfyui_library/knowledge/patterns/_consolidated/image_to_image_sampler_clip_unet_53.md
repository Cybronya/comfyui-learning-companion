---
name: image_to_image_sampler_clip_unet_53
type: Image To Image
frequency: 7
level: strong
coverage: 0.742571
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, Image Blank, ImageCompositeMasked, JoinImageWithAlpha, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/10.tonnie-kontext扩图_1991944906195226625.json, 图片生成/图生图/11. Kontext万物移除_1997536686689161218.json, 图片生成/图生图/12.tonnie-kontext局部重绘_1997546932853739522.json, 图片生成/图生图/13.tonnie-kontext换装，效果不如fill_1992957068195856385.json, 图片生成/图生图/tonnie-Kontext万物移除_1992947428424957954.json, 图片生成/图生图/tonnie-Kontext扩图_1992936813297860609.json, 图片生成/图生图/tonnie-kontext局部重绘_1992952788219002881.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_53

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/10.tonnie-kontext扩图_1991944906195226625.json、图片生成/图生图/11. Kontext万物移除_1997536686689161218.json、图片生成/图生图/12.tonnie-kontext局部重绘_1997546932853739522.json、图片生成/图生图/13.tonnie-kontext换装，效果不如fill_1992957068195856385.json、图片生成/图生图/tonnie-Kontext万物移除_1992947428424957954.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `Image Blank`
- `ImageCompositeMasked`
- `JoinImageWithAlpha`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/7 个有
- `Get Image Size` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `LoraLoaderModelOnly` —— 3/7 个有
- `Mask Fill Holes` —— 3/7 个有
- `GetImageSize` —— 2/7 个有
- `ImagePadForOutpaint` —— 2/7 个有
- `ModelSamplingFlux` —— 2/7 个有
- `GetImageSize+` —— 1/7 个有
- `InspyrenetRembg` —— 1/7 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/7 个有
- `MaskFillHoles` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 20 | 7 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | beta | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 20，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
