---
name: image_to_image_controlnet_ipadapter_sampler_3
type: Image To Image
frequency: 5
level: strong
coverage: 0.9332
common_nodes: [CheckpointLoaderSimple, ConditioningConcat, ControlNetApplyAdvanced, ControlNetLoader, IPAdapterAdvanced, IPAdapterUnifiedLoader, ImageInvert, ImageScaleToMegapixels, KSampler, LoadImage, PrepImageForClipVision, PreviewImage, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/sd线稿+风格参考图上色_1942396787460091906.json, 图片生成/图生图/sd线稿+风格参考图上色_1971036255712645121.json, 图片生成/图生图/sd线稿controlnet局部重绘_1971466564627316737.json, 图片生成/图生图/【素描秒变彩色】万物上色_1912768553647570946.json, 图片生成/图生图/草图变精致_超绝参考图上色_1912767819606388737.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_sampler_3

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/sd线稿+风格参考图上色_1942396787460091906.json、图片生成/图生图/sd线稿+风格参考图上色_1971036255712645121.json、图片生成/图生图/sd线稿controlnet局部重绘_1971466564627316737.json、图片生成/图生图/【素描秒变彩色】万物上色_1912768553647570946.json、图片生成/图生图/草图变精致_超绝参考图上色_1912767819606388737.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `ConditioningConcat`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `ImageInvert`
- `ImageScaleToMegapixels`
- `KSampler`
- `LoadImage`
- `PrepImageForClipVision`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BNK_CLIPTextEncodeAdvanced` —— 3/5 个有
- `UpscaleModelLoader` —— 3/5 个有
- `CLIPTextEncode` —— 2/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `MaskBlur+` —— 1/5 个有
- `MaskToImage` —— 1/5 个有
- `SetLatentNoiseMask` —— 1/5 个有
- `VHS_VAEEncodeBatched` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 5 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 5 | 100% |
| 采样算法 | euler_ancestral | - | 5 | 100% |
| 调度器 | normal | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| ControlNet 权重 | 0.9 | 0.6 - 0.9 | 5 | 81% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.9，观测区间 0.6 - 0.9，5 个样本，取值集中（一致性 81%）
