---
name: image_to_image_sampler_clip_unet_34
type: Image To Image
frequency: 11
level: strong
coverage: 0.827091
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, Image Blank, ImageCompositeMasked, JoinImageWithAlpha, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/10.tonnie-kontext扩图_1991944906195226625.json, 图片生成/图生图/11. Kontext万物移除_1997536686689161218.json, 图片生成/图生图/12.tonnie-kontext局部重绘_1997546932853739522.json, 图片生成/图生图/13.tonnie-kontext换装，效果不如fill_1992957068195856385.json, 图片生成/图生图/tonnie-Kontext万物移除_1992947428424957954.json, 图片生成/图生图/tonnie-Kontext扩图_1992936813297860609.json, 图片生成/图生图/tonnie-kontext局部重绘_1992952788219002881.json, 平台全量/Kontext扩图-完美过渡 flux kontext扩图工作流_1998189901998882818.json, 平台全量/flux kontext局部重绘工作流升级版_1943314762694336514.json, 平台全量/flux kontext扩图工作流_1942225772222550017.json, 平台全量/flux kontext移除工作流_1941129735458156545.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_34

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/10.tonnie-kontext扩图_1991944906195226625.json、图片生成/图生图/11. Kontext万物移除_1997536686689161218.json、图片生成/图生图/12.tonnie-kontext局部重绘_1997546932853739522.json、图片生成/图生图/13.tonnie-kontext换装，效果不如fill_1992957068195856385.json、图片生成/图生图/tonnie-Kontext万物移除_1992947428424957954.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
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
- `ConditioningZeroOut` —— 9/11 个有
- `FluxKontextImageScale` —— 8/11 个有
- `Get Image Size` —— 7/11 个有
- `LoraLoaderModelOnly` —— 6/11 个有
- `Mask Fill Holes` —— 5/11 个有
- `PreviewImage` —— 5/11 个有
- `ImagePadForOutpaint` —— 4/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/11 个有
- `GetImageSize` —— 2/11 个有
- `ModelSamplingFlux` —— 2/11 个有
- `GetImageSize+` —— 1/11 个有
- `InspyrenetRembg` —— 1/11 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/11 个有
- `MaskFillHoles` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 20 | 11 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | beta | - | 11 | 73% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 20，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 73%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
