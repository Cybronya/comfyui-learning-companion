---
name: text_to_image_inpaint_upscale_sampler
type: Text To Image
frequency: 6
level: weak
coverage: 0.847
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), ImageScaleBy, ImpactGaussianBlurMask, InpaintModelConditioning, KSampler, LoadImage, MaskPreview+, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAELoader]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image 文生图 + 图像重绘_1997862331348660225.json, 图片生成/图生图/Zimage万能工作流(文生图，图生图，局部重绘，线条，深度，姿势 控制，高清放大）_1997989363134922754.json, 图片生成/文生图/Qwen-Image-2512-图片重绘_文生图_2007853900451291137.json, 图片生成/文生图/Z-image 文生图 + 图像重绘_1993849482756505601.json, 图片生成/文生图/Z-image 文生图 + 图像重绘_1997524385407909890.json, 图片生成/文生图/Z-image直出4K_2002998194634145793.json]
source: knowledge_consolidation
---

# text_to_image_inpaint_upscale_sampler

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Z-image 文生图 + 图像重绘_1997862331348660225.json、图片生成/图生图/Zimage万能工作流(文生图，图生图，局部重绘，线条，深度，姿势 控制，高清放大）_1997989363134922754.json、图片生成/文生图/Qwen-Image-2512-图片重绘_文生图_2007853900451291137.json、图片生成/文生图/Z-image 文生图 + 图像重绘_1993849482756505601.json、图片生成/文生图/Z-image 文生图 + 图像重绘_1997524385407909890.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImpactGaussianBlurMask`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `MaskPreview+`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 5/6 个有
- `CR Latent Input Switch` —— 5/6 个有
- `CR Text` —— 5/6 个有
- `ConditioningZeroOut` —— 5/6 个有
- `Mask Fill Holes` —— 5/6 个有
- `ModelPatchLoader` —— 5/6 个有
- `QwenImageDiffsynthControlnet` —— 5/6 个有
- `VAEDecode` —— 4/6 个有
- `VAEEncode` —— 4/6 个有
- `PreviewAny` —— 3/6 个有
- `AILab_QwenVL` —— 2/6 个有
- `DyPE_FLUX` —— 2/6 个有
- `ModelSamplingAuraFlow` —— 2/6 个有
- `VAEDecodeTiled` —— 2/6 个有
- `AILab_MiniCPM_4_V` —— 1/6 个有
- `CR Prompt Text` —— 1/6 个有
- `ConditioningClamp` —— 1/6 个有
- `Latent Switch (JPS)` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `Mask Invert` —— 1/6 个有
- `VAEEncodeTiled` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 480 - 2048 | 6 | 55% |
| 高度 | 1280 | 512 - 3072 | 6 | 41% |
| 采样步数 | 10 | 9 - 20 | 6 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 6 | 0% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 0.675 | 0.41 - 1 | 6 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 2/6 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 480 - 2048，6 个样本
- 高度 中位数 1280，观测区间 512 - 3072，6 个样本，取值分散，一致性仅 41%
- 采样步数 中位数 10，观测区间 9 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，6 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 0.675，观测区间 0.41 - 1，6 个样本
