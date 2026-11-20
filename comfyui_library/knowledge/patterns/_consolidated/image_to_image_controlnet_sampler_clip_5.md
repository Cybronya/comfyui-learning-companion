---
name: image_to_image_controlnet_sampler_clip_5
type: Image To Image
frequency: 7
level: moderate
coverage: 0.919143
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, ModelPatchLoader, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWEN局部重回_1959968462070296578.json, 图片生成/图生图/Qwen Image Inapint模型局部重绘V1_1959993904777080833.json, 图片生成/图生图/Z image Controlnet_2001579206280658946.json, 图片生成/图生图/Z-image-turbo ControNet2.1_2018887460457025538.json, 图片生成/图生图/千问局部重绘Inpaint控制-QWen-Image-ComfyUI官方_1958745627586879490.json, 图片生成/图生图/千问局部重绘Inpaint控制-QWen-Image_1959234698784485378.json, 图片生成/文生图/zimage-controlnet-2.1（26.1）人物替换工作流_2011523555053281282.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_5

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/QWEN局部重回_1959968462070296578.json、图片生成/图生图/Qwen Image Inapint模型局部重绘V1_1959993904777080833.json、图片生成/图生图/Z image Controlnet_2001579206280658946.json、图片生成/图生图/Z-image-turbo ControNet2.1_2018887460457025538.json、图片生成/图生图/千问局部重绘Inpaint控制-QWen-Image-ComfyUI官方_1958745627586879490.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `ModelPatchLoader`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 5/7 个有
- `ImageAndMaskPreview` —— 4/7 个有
- `Text Multiline` —— 4/7 个有
- `AIO_Preprocessor` —— 3/7 个有
- `ImageStitch` —— 3/7 个有
- `ConditioningZeroOut` —— 2/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `CR Prompt Text` —— 1/7 个有
- `GrowMaskWithBlur` —— 1/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `SetLatentNoiseMask` —— 1/7 个有
- `easy imageSizeBySide` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 7 | 66% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 7 | 60% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，7 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
