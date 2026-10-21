---
name: text_to_image_controlnet_inpaint_upscale_2
type: Text To Image
frequency: 3
level: moderate
coverage: 0.846333
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CR Latent Input Switch, CR Text, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), ImageScaleBy, ImpactGaussianBlurMask, InpaintModelConditioning, KSampler, LoadImage, Mask Fill Holes, MaskPreview+, ModelPatchLoader, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAELoader]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image 文生图 + 图像重绘_1993849482756505601.json, 图片生成/文生图/Z-image 文生图 + 图像重绘_1997524385407909890.json, 图片生成/文生图/Z-image直出4K_2002998194634145793.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_inpaint_upscale_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image 文生图 + 图像重绘_1993849482756505601.json、图片生成/文生图/Z-image 文生图 + 图像重绘_1997524385407909890.json、图片生成/文生图/Z-image直出4K_2002998194634145793.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Latent Input Switch`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImpactGaussianBlurMask`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `Mask Fill Holes`
- `MaskPreview+`
- `ModelPatchLoader`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DyPE_FLUX` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `VAEDecodeTiled` —— 2/3 个有
- `AILab_QwenVL` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `VAEDecode` —— 1/3 个有
- `VAEEncode` —— 1/3 个有
- `VAEEncodeTiled` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 2048 | 1024 - 2048 | 3 | 72% |
| 高度 | 3072 | 1024 - 3072 | 3 | 60% |
| 采样步数 | 10 | 9 - 10 | 3 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 0.41 - 1 | 3 | 65% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 2/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 2048，观测区间 1024 - 2048，3 个样本
- 高度 中位数 3072，观测区间 1024 - 3072，3 个样本
- 采样步数 中位数 10，观测区间 9 - 10，3 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.41 - 1，3 个样本
- 高发问题（2/3 个样本）：发现KSampler但没有VAEDecode
