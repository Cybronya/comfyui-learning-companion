---
name: image_to_image_sampler_unet_vae_30
type: Image To Image
frequency: 7
level: strong
coverage: 0.876
common_nodes: [ConditioningZeroOut, FluxKontextImageScale, Image Comparer (rgthree), KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问QwenEdit 2511一致性图像编辑_2003754623812968450.json, 图片生成/图生图/千问QwenEdit plus一致性图像编辑_1970379059131785217.json, 图片生成/图生图/千问图像编辑，一致性编辑，无像素漂移，感谢Jason_1965208291238400002.json, 图片生成/图生图/去水印_1995428633756020737.json, 图片生成/图生图/图片去水印-Kontext版_1973776280980164610.json, 图片生成/图生图/图片去水印-Kontext版_1979713173710344193.json, 图片生成/图生图/图片去水印_2046787355851362305.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_30

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/千问QwenEdit 2511一致性图像编辑_2003754623812968450.json、图片生成/图生图/千问QwenEdit plus一致性图像编辑_1970379059131785217.json、图片生成/图生图/千问图像编辑，一致性编辑，无像素漂移，感谢Jason_1965208291238400002.json、图片生成/图生图/去水印_1995428633756020737.json、图片生成/图生图/图片去水印-Kontext版_1973776280980164610.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `ConditioningZeroOut`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `ReferenceLatent` —— 5/7 个有
- `DualCLIPLoader` —— 4/7 个有
- `FluxGuidance` —— 4/7 个有
- `CLIPLoader` —— 3/7 个有
- `GroundingDinoModelLoader (segment anything)` —— 3/7 个有
- `GroundingDinoSAMSegment (segment anything)` —— 3/7 个有
- `LoraLoaderModelOnly` —— 3/7 个有
- `MaskPreview` —— 3/7 个有
- `SAMModelLoader (segment anything)` —— 3/7 个有
- `CR Prompt Text` —— 2/7 个有
- `Text` —— 2/7 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/7 个有
- `FancyTimerNode` —— 1/7 个有
- `easy getNode` —— 1/7 个有
- `easy setNode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 7 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
