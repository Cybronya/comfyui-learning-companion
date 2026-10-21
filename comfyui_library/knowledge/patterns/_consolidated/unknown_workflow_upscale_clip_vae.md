---
name: unknown_workflow_upscale_clip_vae
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.470333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, ImageScaleToTotalPixels, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, PreviewImage, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/25.12.21-Z-IMAGE+CN2.1+洗图放大_2002459473228754946.json, 图片生成/文生图/Z-IMAGE终极版自动洗图流+CN2.1+高清放大_2001589034491211777.json, 图片生成/文生图/Z-Image 超强ControlNet全自动洗图流_1996161265351475201.json, 图片生成/文生图/Z_image-文生图&洗图&高清修复v2_1998028391066558466.json, 图片生成/文生图/Z_image-文生图&洗图&高清修复v2王改革。_2001957068246532098.json, 图片生成/文生图/🦄Z image2026出图🎯天下无腰_2025194956939337729.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_clip_vae

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/25.12.21-Z-IMAGE+CN2.1+洗图放大_2002459473228754946.json、图片生成/文生图/Z-IMAGE终极版自动洗图流+CN2.1+高清放大_2001589034491211777.json、图片生成/文生图/Z-Image 超强ControlNet全自动洗图流_1996161265351475201.json、图片生成/文生图/Z_image-文生图&洗图&高清修复v2_1998028391066558466.json、图片生成/文生图/Z_image-文生图&洗图&高清修复v2王改革。_2001957068246532098.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：47%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ImageScaleToTotalPixels`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `PreviewImage`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 5/6 个有
- `INTConstant` —— 5/6 个有
- `KSamplerAdvanced` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `ModelPatchLoader` —— 5/6 个有
- `QwenImageDiffsynthControlnet` —— 5/6 个有
- `easy seed` —— 5/6 个有
- `CLIPLoader` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 4/6 个有
- `Image Comparer (rgthree)` —— 4/6 个有
- `UNETLoader` —— 4/6 个有
- `VAELoader` —— 4/6 个有
- `CR SDXL Aspect Ratio` —— 3/6 个有
- `GetNode` —— 3/6 个有
- `KSampler` —— 3/6 个有
- `LayerUtility: PurgeVRAM V2` —— 3/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `PlaySound|pysssss` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `CheckpointLoaderSimple` —— 2/6 个有
- `ConditioningSetTimestepRange` —— 2/6 个有
- `EmptyLatentImage` —— 2/6 个有
- `ModelSamplingAuraFlow` —— 2/6 个有
- `EmptySD3LatentImage` —— 1/6 个有
- `ImageScaleBy` —— 1/6 个有
- `LatentColorMatch` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1920 | - | 2 | 100% |
| 高度 | 1080 | - | 2 | 100% |
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 10 | 6 | 18% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1080，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 10，6 个样本，取值分散，一致性仅 18%
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
