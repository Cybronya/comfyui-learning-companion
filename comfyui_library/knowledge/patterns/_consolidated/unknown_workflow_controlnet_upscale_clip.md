---
name: unknown_workflow_controlnet_upscale_clip
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.596091
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchLoader, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/001.Z-image生图巅峰013.深度控制洗图+放大-高显存_2033744666503421954.json, 图片生成/图生图/001.Z-image生图巅峰014.线稿控制洗图+放大-高显存.json_2033747543804354562.json, 图片生成/图生图/251207-05.深度控制洗图放大-高显存_1997726098249158657.json, 图片生成/图生图/251207-06.线稿控制洗图放大-高显存_1997726912220999682.json, 图片生成/图生图/LH-DMT版本-2.生图片类-025.Z_image深度控制洗图放大-高显存_2016493126872993793.json, 图片生成/图生图/LH-DMT版本-2.生图片类-026.Z_image线稿控制洗图放大-高显存_2016493151422259202.json, 图片生成/图生图/Z_Image_Controlnet_Union_1996610921038495745.json, 图片生成/图生图/图片洗图 图片复刻_2021042086287515650.json, 图片生成/文生图/25.12.21-Z-IMAGE+CN2.1+洗图放大_2002459473228754946.json, 图片生成/文生图/Z-IMAGE终极版自动洗图流+CN2.1+高清放大_2001589034491211777.json, 图片生成/文生图/Z-Image 超强ControlNet全自动洗图流_1996161265351475201.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_clip

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/001.Z-image生图巅峰013.深度控制洗图+放大-高显存_2033744666503421954.json、图片生成/图生图/001.Z-image生图巅峰014.线稿控制洗图+放大-高显存.json_2033747543804354562.json、图片生成/图生图/251207-05.深度控制洗图放大-高显存_1997726098249158657.json、图片生成/图生图/251207-06.线稿控制洗图放大-高显存_1997726912220999682.json、图片生成/图生图/LH-DMT版本-2.生图片类-025.Z_image深度控制洗图放大-高显存_2016493126872993793.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 11 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchLoader`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 10/11 个有
- `ImageScaleToTotalPixels` —— 10/11 个有
- `Qwen3_VQA` —— 10/11 个有
- `ShowText|pysssss` —— 10/11 个有
- `EmptySD3LatentImage` —— 9/11 个有
- `Image Comparer (rgthree)` —— 9/11 个有
- `ImageScaleBy` —— 9/11 个有
- `KSampler` —— 9/11 个有
- `LayerUtility: ImageReel` —— 9/11 个有
- `LayerUtility: ImageReelComposit` —— 9/11 个有
- `Fast Groups Bypasser (rgthree)` —— 7/11 个有
- `easy cleanGpuUsed` —— 7/11 个有
- `EmptyLatentImage` —— 2/11 个有
- `KSamplerAdvanced` —— 2/11 个有
- `ModelSamplingAuraFlow` —— 2/11 个有
- `easy seed` —— 2/11 个有
- `Float` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 10 | 11 | 0% |
| 采样算法 | er_sde | - | 11 | 73% |
| 调度器 | simple | - | 11 | 82% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1920 | - | 2 | 100% |
| 高度 | 1080 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 10，11 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 er_sde，11 个样本，一致性 73%
- 调度器 最常用 simple，11 个样本，一致性 82%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1080，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
