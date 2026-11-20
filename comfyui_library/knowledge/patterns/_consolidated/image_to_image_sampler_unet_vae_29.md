---
name: image_to_image_sampler_unet_vae_29
type: Image To Image
frequency: 9
level: strong
coverage: 0.895667
common_nodes: [ConditioningZeroOut, FluxKontextImageScale, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问QwenEdit 2511一致性图像编辑_2003754623812968450.json, 图片生成/图生图/千问QwenEdit plus一致性图像编辑_1970379059131785217.json, 图片生成/图生图/千问图像编辑，一致性编辑，无像素漂移，感谢Jason_1965208291238400002.json, 图片生成/图生图/去水印_1995428633756020737.json, 图片生成/图生图/去水印_水印去除-kontext_1963971515945504769.json, 图片生成/图生图/图像高清去模糊deblur(Kontext-LORA版)_1943499477413994497.json, 图片生成/图生图/图片去水印-Kontext版_1973776280980164610.json, 图片生成/图生图/图片去水印-Kontext版_1979713173710344193.json, 图片生成/图生图/图片去水印_2046787355851362305.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_29

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/千问QwenEdit 2511一致性图像编辑_2003754623812968450.json、图片生成/图生图/千问QwenEdit plus一致性图像编辑_1970379059131785217.json、图片生成/图生图/千问图像编辑，一致性编辑，无像素漂移，感谢Jason_1965208291238400002.json、图片生成/图生图/去水印_1995428633756020737.json、图片生成/图生图/去水印_水印去除-kontext_1963971515945504769.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `ConditioningZeroOut`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 8/9 个有
- `CLIPTextEncode` —— 7/9 个有
- `ReferenceLatent` —— 7/9 个有
- `DualCLIPLoader` —— 6/9 个有
- `FluxGuidance` —— 6/9 个有
- `PreviewImage` —— 5/9 个有
- `LoraLoaderModelOnly` —— 4/9 个有
- `CLIPLoader` —— 3/9 个有
- `GroundingDinoModelLoader (segment anything)` —— 3/9 个有
- `GroundingDinoSAMSegment (segment anything)` —— 3/9 个有
- `MaskPreview` —— 3/9 个有
- `SAMModelLoader (segment anything)` —— 3/9 个有
- `CR Prompt Text` —— 2/9 个有
- `Text` —— 2/9 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/9 个有
- `FancyTimerNode` —— 1/9 个有
- `ImageStitch` —— 1/9 个有
- `easy getNode` —— 1/9 个有
- `easy setNode` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 9 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
