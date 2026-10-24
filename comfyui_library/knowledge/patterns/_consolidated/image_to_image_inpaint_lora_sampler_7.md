---
name: image_to_image_inpaint_lora_sampler_7
type: Image To Image
frequency: 4
level: moderate
coverage: 0.5045
common_nodes: [AIO_Preprocessor, Any Switch (rgthree), CLIPLoader, ConditioningZeroOut, GetImageSize, GetNode, ImageAndMaskPreview, ImageCompositeMasked, ImageResizeKJv2, ImageScale, ImageSmartSharpen+, InpaintCropImproved, InpaintStitchImproved, KSampler, LayerFilter: FilmV2, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LayerUtility: CropByMask V2, LoadImage, LoraLoaderModelOnly, PreviewImage, RebatchLatents, RepeatLatentBatch, SaveImage, SetNode, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, workflow>mask cover]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit-2509 人像换脸_2091503546717003778.json, 图片生成/图生图/Qwen_edit+plus+2509-换头换脸 图生图_2027627095748255746.json, 图片生成/图生图/最佳人像换脸工作流+手动遮罩-邻家AI大女孩_2043979158841204737.json, 图片生成/图生图/👨🏻Qwen_edit plus 2509-最简易换脸工作流_1997526287839346689.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_lora_sampler_7

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit-2509 人像换脸_2091503546717003778.json、图片生成/图生图/Qwen_edit+plus+2509-换头换脸 图生图_2027627095748255746.json、图片生成/图生图/最佳人像换脸工作流+手动遮罩-邻家AI大女孩_2043979158841204737.json、图片生成/图生图/👨🏻Qwen_edit plus 2509-最简易换脸工作流_1997526287839346689.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：50%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `Any Switch (rgthree)`
- `CLIPLoader`
- `ConditioningZeroOut`
- `GetImageSize`
- `GetNode`
- `ImageAndMaskPreview`
- `ImageCompositeMasked`
- `ImageResizeKJv2`
- `ImageScale`
- `ImageSmartSharpen+`
- `InpaintCropImproved`
- `InpaintStitchImproved`
- `KSampler`
- `LayerFilter: FilmV2`
- `LayerMask: MaskGrow`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropByMask V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RebatchLatents`
- `RepeatLatentBatch`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `workflow>mask cover`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 3/4 个有
- `ApplyInstantID` —— 3/4 个有
- `CLIPTextEncode` —— 3/4 个有
- `CheckpointLoaderSimple` —— 3/4 个有
- `ControlNetLoader` —— 3/4 个有
- `DifferentialDiffusion` —— 3/4 个有
- `Fast Groups Muter (rgthree)` —— 3/4 个有
- `InpaintModelConditioning` —— 3/4 个有
- `InstantIDFaceAnalysis` —— 3/4 个有
- `InstantIDModelLoader` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `easy imageRemBg` —— 3/4 个有
- `Anything Everywhere` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 4 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | dpmpp_2m | - | 4 | 75% |
| 调度器 | karras | - | 4 | 75% |
| 重绘幅度 | 0.4 | 0.4 - 1 | 4 | 53% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，4 个样本，一致性 75%
- 调度器 最常用 karras，4 个样本，一致性 75%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 1，4 个样本
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
