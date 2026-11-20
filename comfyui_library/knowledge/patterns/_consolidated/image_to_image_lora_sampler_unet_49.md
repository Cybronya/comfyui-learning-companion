---
name: image_to_image_lora_sampler_unet_49
type: Image To Image
frequency: 12
level: moderate
coverage: 0.9525
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2课 文生图 图生图工作流_2104903322997186561.json, 图片生成/图生图/F.2Klein提取3d立体服装_2053799596253556738.json, 图片生成/图生图/F.2Klein提取3d立体服装_2056216125565874178.json, 图片生成/图生图/F.2Klein提取3d立体服装_2057635695820369921.json, 图片生成/图生图/F.2Klein提取3d立体服装_2058364672834891778.json, 图片生成/图生图/F.2Klein提取3d立体服装_2058380006920904706.json, 图片生成/图生图/FireRed-Image-Edit1.1单图编辑换装_2031741074665902081.json, 图片生成/图生图/Flux2-Klein9b一键提取3d立体服装_2038251793729200129.json, 图片生成/图生图/Flux2-Klein一键提取3d立体服装_2038862090676473857.json, 图片生成/图生图/Qwen-Edit  动漫转真人+zimage+放大_2058045653837762562.json, 图片生成/图生图/Qwen-Edit-2511 一致性增强_2051942635396452354.json, 图片生成/图生图/【动漫转真人】极速流_Qwen+Z-image_真实洗图_2031187547338051585.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_49

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/2课 文生图 图生图工作流_2104903322997186561.json、图片生成/图生图/F.2Klein提取3d立体服装_2053799596253556738.json、图片生成/图生图/F.2Klein提取3d立体服装_2056216125565874178.json、图片生成/图生图/F.2Klein提取3d立体服装_2057635695820369921.json、图片生成/图生图/F.2Klein提取3d立体服装_2058364672834891778.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 11/12 个有
- `ConditioningZeroOut` —— 11/12 个有
- `CR Text` —— 9/12 个有
- `Int` —— 8/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/12 个有
- `Flux2KleinEditTextEncode_EditUtils` —— 7/12 个有
- `FluxKontextMultiReferenceLatentMethod` —— 4/12 个有
- `Image Comparer (rgthree)` —— 4/12 个有
- `ImageScaleBy` —— 4/12 个有
- `PreviewImage` —— 4/12 个有
- `TextEncodeQwenImageEditPlus` —— 4/12 个有
- `CLIPTextEncode` —— 3/12 个有
- `ImageScaleToTotalPixels` —— 3/12 个有
- `SeedVR2LoadDiTModel` —— 3/12 个有
- `SeedVR2LoadVAEModel` —— 3/12 个有
- `SeedVR2VideoUpscaler` —— 3/12 个有
- `easy cleanGpuUsed` —— 2/12 个有
- `Anything Everywhere3` —— 1/12 个有
- `CR Seed` —— 1/12 个有
- `Fast Groups Bypasser (rgthree)` —— 1/12 个有
- `ImageStitch` —— 1/12 个有
- `LayerUtility: ImageReel` —— 1/12 个有
- `LayerUtility: ImageReelComposit` —— 1/12 个有
- `QwenImageLatentAspectRatio` —— 1/12 个有
- `TextInput_` —— 1/12 个有
- `WujiCleaner` —— 1/12 个有
- `easy float` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 12 | 22% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 83% |
| 调度器 | simple | - | 12 | 83% |
| 重绘幅度 | 1 | 0.1 - 1 | 12 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，12 个样本，取值分散，一致性仅 22%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 83%
- 调度器 最常用 simple，12 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 0.1 - 1，12 个样本
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
