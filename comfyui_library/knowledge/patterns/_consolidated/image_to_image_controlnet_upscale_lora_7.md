---
name: image_to_image_controlnet_upscale_lora_7
type: Image To Image
frequency: 3
level: strong
coverage: 0.807
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, EmptySD3LatentImage, GetImageSize, GetImageSizeAndCount, Image Comparer (rgthree), ImageScaleBy, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, ZImageFunControlnet]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z模型Controlnet2_inpaint高级工作流-课程同步流程_2002322533489754113.json, 图片生成/文生图/Z-Image-Turbo-Controlnet2 + Inpaint_2002209734201622530.json, 图片生成/文生图/Z-Image文生图+局部重绘+放大分辨率：实现家用显卡也能生成4K高清图！_2002986532715786242.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_lora_7

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Z模型Controlnet2_inpaint高级工作流-课程同步流程_2002322533489754113.json、图片生成/文生图/Z-Image-Turbo-Controlnet2 + Inpaint_2002209734201622530.json、图片生成/文生图/Z-Image文生图+局部重绘+放大分辨率：实现家用显卡也能生成4K高清图！_2002986532715786242.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `EmptySD3LatentImage`
- `GetImageSize`
- `GetImageSizeAndCount`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `ZImageFunControlnet`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `ImpactGaussianBlurMask` —— 1/3 个有
- `InpaintModelConditioning` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `Mask Fill Holes` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_2s | - | 3 | 100% |
| 调度器 | beta57 | - | 3 | 100% |
| 重绘幅度 | 0.5 | 0.5 - 0.5 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，3 个样本，一致性 100%
- 调度器 最常用 beta57，3 个样本，一致性 100%
- 重绘幅度 中位数 0.5，观测区间 0.5 - 0.5，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
