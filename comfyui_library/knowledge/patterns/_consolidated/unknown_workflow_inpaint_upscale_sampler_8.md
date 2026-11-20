---
name: unknown_workflow_inpaint_upscale_sampler_8
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.783
common_nodes: [CLIPLoader, CLIPTextEncode, ChordLoadModel, ChordMaterialEstimation, ChordNormalToHeight, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, ETN_LoadImageBase64, EmptyImage, FluxGuidance, Image Comparer (rgthree), Image Overlay, ImageCompositeMasked, ImageCrop, ImageScale, ImageScaleBy, ImageToMask, InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LoadImage, MaskToImage, PreviewImage, ResizeAndPadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image-turbo-材质贴图生成器_2041329252448083969.json, 图片生成/文生图/Zimage文生图+无缝处理+材质贴图_2004031509545795586.json, 图片生成/文生图/纹理生成_2015978668824207362.json, 平台全量/PBR材质生成_2007238587309367297.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_sampler_8

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Z-image-turbo-材质贴图生成器_2041329252448083969.json、图片生成/文生图/Zimage文生图+无缝处理+材质贴图_2004031509545795586.json、图片生成/文生图/纹理生成_2015978668824207362.json、平台全量/PBR材质生成_2007238587309367297.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ChordLoadModel`
- `ChordMaterialEstimation`
- `ChordNormalToHeight`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `ETN_LoadImageBase64`
- `EmptyImage`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `Image Overlay`
- `ImageCompositeMasked`
- `ImageCrop`
- `ImageScale`
- `ImageScaleBy`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskGrow`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `ResizeAndPadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `CR SDXL Aspect Ratio` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `Int` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy seed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12.5 | 8 - 15 | 4 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 50% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12.5，观测区间 8 - 15，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
