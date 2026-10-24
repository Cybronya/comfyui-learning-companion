---
name: text_to_image_sampler_clip_unet_124
type: Text To Image
frequency: 5
level: strong
coverage: 0.946
common_nodes: [ApplyFBCacheOnModel, CLIPTextEncode, DF_Get_image_size, DualCLIPLoader, EmptyLatentImage, Flex2Conditioner, ImageConcanate, ImageScaleToTotalPixels, KSampler, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flex.2局部二阶段重绘工作流V1_1916364099486154753.json, 图片生成/图生图/视频首帧Flex.2深度替换图_1924671178982813697.json, 图片生成/文生图/Flex.2无CN姿势控制文生图工作流V1_1916417413187829761.json, 图片生成/文生图/Flex.2无CN深度控制文生图工作流V1_1916415071411703809.json, 图片生成/文生图/Flex.2无CN线稿控制文生图工作流V1_1916419825193648129.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_124

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flex.2局部二阶段重绘工作流V1_1916364099486154753.json、图片生成/图生图/视频首帧Flex.2深度替换图_1924671178982813697.json、图片生成/文生图/Flex.2无CN姿势控制文生图工作流V1_1916417413187829761.json、图片生成/文生图/Flex.2无CN深度控制文生图工作流V1_1916415071411703809.json、图片生成/文生图/Flex.2无CN线稿控制文生图工作流V1_1916419825193648129.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `ApplyFBCacheOnModel`
- `CLIPTextEncode`
- `DF_Get_image_size`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Flex2Conditioner`
- `ImageConcanate`
- `ImageScaleToTotalPixels`
- `KSampler`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GroundingDinoModelLoader (segment anything2)` —— 4/5 个有
- `JWImageResizeByLongerSide` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `Note Plus (mtb)` —— 4/5 个有
- `DepthAnythingPreprocessor` —— 3/5 个有
- `AnyLineArtPreprocessor_aux` —— 1/5 个有
- `EG_ZZ_SSKZ` —— 1/5 个有
- `GroundingDinoSAM2Segment (segment anything2)` —— 1/5 个有
- `ImageFromBatch+` —— 1/5 个有
- `OpenposePreprocessor` —— 1/5 个有
- `SAM2ModelLoader (segment anything2)` —— 1/5 个有
- `SetLatentNoiseMask` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 840 | 840 - 840 | 5 | 100% |
| 高度 | 1256 | 1256 - 1256 | 5 | 100% |
| 采样步数 | 30 | 30 - 30 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | deis | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 840，观测区间 840 - 840，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1256，观测区间 1256 - 1256，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 30 - 30，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 deis，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
