---
name: image_to_image_sampler_clip_unet_67
type: Image To Image
frequency: 8
level: moderate
coverage: 0.92625
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWEN局部重回_1959968462070296578.json, 图片生成/图生图/Qwen Image Inapint模型局部重绘V1_1959993904777080833.json, 图片生成/图生图/Z image Controlnet_2001579206280658946.json, 图片生成/图生图/Z-image-turbo ControNet2.1_2018887460457025538.json, 图片生成/图生图/Z-image图生图_1994327939347054594.json, 图片生成/图生图/千问局部重绘Inpaint控制-QWen-Image-ComfyUI官方_1958745627586879490.json, 图片生成/图生图/千问局部重绘Inpaint控制-QWen-Image_1959234698784485378.json, 平台全量/通义千问中文改字（设计师必备工具）_1963095301659799553.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_67

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/QWEN局部重回_1959968462070296578.json、图片生成/图生图/Qwen Image Inapint模型局部重绘V1_1959993904777080833.json、图片生成/图生图/Z image Controlnet_2001579206280658946.json、图片生成/图生图/Z-image-turbo ControNet2.1_2018887460457025538.json、图片生成/图生图/Z-image图生图_1994327939347054594.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelPatchLoader` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `QwenImageDiffsynthControlnet` —— 7/8 个有
- `ModelSamplingAuraFlow` —— 6/8 个有
- `Text Multiline` —— 6/8 个有
- `ImageAndMaskPreview` —— 5/8 个有
- `ImageStitch` —— 4/8 个有
- `AIO_Preprocessor` —— 2/8 个有
- `ConditioningZeroOut` —— 2/8 个有
- `Image Comparer (rgthree)` —— 2/8 个有
- `ImageScaleToTotalPixels` —— 2/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `easy float` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 8 | 66% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 8 | 63% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 0.75 - 1 | 8 | 91% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，8 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 0.75 - 1，8 个样本，取值集中（一致性 91%）
