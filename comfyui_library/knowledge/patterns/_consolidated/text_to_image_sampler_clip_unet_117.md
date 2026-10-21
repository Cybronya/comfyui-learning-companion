---
name: text_to_image_sampler_clip_unet_117
type: Text To Image
frequency: 3
level: strong
coverage: 0.885
common_nodes: [ApplyFBCacheOnModel, CLIPTextEncode, DF_Get_image_size, DualCLIPLoader, EmptyLatentImage, Flex2Conditioner, GroundingDinoModelLoader (segment anything2), ImageConcanate, ImageScaleToTotalPixels, JWImageResizeByLongerSide, KSampler, LoadImage, Note Plus (mtb), PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [GroundingDinoModelLoader (segment anything2), Note Plus (mtb)]
members: [图片生成/文生图/1916415071411703809.json, 图片生成/文生图/1916417413187829761.json, 图片生成/文生图/1916419825193648129.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_117

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1916415071411703809.json、图片生成/文生图/1916417413187829761.json、图片生成/文生图/1916419825193648129.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyFBCacheOnModel`
- `CLIPTextEncode`
- `DF_Get_image_size`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Flex2Conditioner`
- `GroundingDinoModelLoader (segment anything2)`
- `ImageConcanate`
- `ImageScaleToTotalPixels`
- `JWImageResizeByLongerSide`
- `KSampler`
- `LoadImage`
- `Note Plus (mtb)`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AnyLineArtPreprocessor_aux` —— 1/3 个有
- `DepthAnythingPreprocessor` —— 1/3 个有
- `OpenposePreprocessor` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 840 | 840 - 840 | 3 | 100% |
| 高度 | 1256 | 1256 - 1256 | 3 | 100% |
| 采样步数 | 30 | 30 - 30 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | deis | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 840，观测区间 840 - 840，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1256，观测区间 1256 - 1256，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 30 - 30，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 deis，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：GroundingDinoModelLoader (segment anything2)、Note Plus (mtb)
