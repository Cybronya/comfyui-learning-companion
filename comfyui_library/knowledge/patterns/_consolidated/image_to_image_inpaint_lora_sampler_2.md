---
name: image_to_image_inpaint_lora_sampler_2
type: Image To Image
frequency: 7
level: moderate
coverage: 0.509857
common_nodes: [AIO_Preprocessor, CLIPLoader, ConditioningZeroOut, GetImageSize, GetNode, ImageAndMaskPreview, ImageCompositeMasked, ImageResizeKJv2, ImageScale, ImageSmartSharpen+, InpaintCropImproved, InpaintStitchImproved, KSampler, LayerMask: MaskGrow, LayerUtility: CropByMask V2, LoadImage, LoraLoaderModelOnly, PreviewImage, RebatchLatents, RepeatLatentBatch, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, workflow>mask cover]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit-2509 人像换脸_2091503546717003778.json, 图片生成/图生图/Qwen_edit+plus+2509-换头换脸 图生图_2027627095748255746.json, 图片生成/图生图/最佳人像换脸工作流+手动遮罩-邻家AI大女孩_2043979158841204737.json, 图片生成/图生图/👨🏻Qwen_edit plus 2509-最简易换脸工作流_1997526287839346689.json, 平台全量/👨🏻Qwen_edit plus 2509-换头_换脸-F2P-聚焦裁剪-手动遮罩版_1988830877750800385.json, 平台全量/👨🏻Qwen_edit plus 2509-替换场景中的人物_角色置入场景-聚焦裁剪-手动遮罩_1997484622114144257.json, 平台全量/👨🏻Qwen_edit plus 2509-替换服装_换装_穿搭_服装迁移-聚焦裁剪-手动遮罩_1997492166853345282.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_lora_sampler_2

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit-2509 人像换脸_2091503546717003778.json、图片生成/图生图/Qwen_edit+plus+2509-换头换脸 图生图_2027627095748255746.json、图片生成/图生图/最佳人像换脸工作流+手动遮罩-邻家AI大女孩_2043979158841204737.json、图片生成/图生图/👨🏻Qwen_edit plus 2509-最简易换脸工作流_1997526287839346689.json、平台全量/👨🏻Qwen_edit plus 2509-换头_换脸-F2P-聚焦裁剪-手动遮罩版_1988830877750800385.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：51%

## 共有节点

全部 7 个 workflow 都包含：
- `AIO_Preprocessor`
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
- `LayerMask: MaskGrow`
- `LayerUtility: CropByMask V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RebatchLatents`
- `RepeatLatentBatch`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `workflow>mask cover`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 6/7 个有
- `Anything Everywhere3` —— 6/7 个有
- `LayerFilter: FilmV2` —— 6/7 个有
- `LayerMask: PersonMaskUltra V2` —— 6/7 个有
- `TextEncodeQwenImageEditPlus` —— 6/7 个有
- `easy cleanGpuUsed` —— 6/7 个有
- `easy imageRemBg` —— 6/7 个有
- `ApplyInstantID` —— 5/7 个有
- `CLIPTextEncode` —— 5/7 个有
- `CheckpointLoaderSimple` —— 5/7 个有
- `ControlNetLoader` —— 5/7 个有
- `DifferentialDiffusion` —— 5/7 个有
- `Fast Groups Muter (rgthree)` —— 5/7 个有
- `InpaintModelConditioning` —— 5/7 个有
- `InstantIDFaceAnalysis` —— 5/7 个有
- `InstantIDModelLoader` —— 5/7 个有
- `Anything Everywhere` —— 1/7 个有
- `CropWithPadInfo` —— 1/7 个有
- `LatentUpscale` —— 1/7 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/7 个有
- `QwenEditConfigPreparer` —— 1/7 个有
- `Text` —— 1/7 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 20 | 7 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | dpmpp_2m | - | 7 | 57% |
| 调度器 | karras | - | 7 | 57% |
| 重绘幅度 | 0.4 | 0.37 - 1 | 7 | 52% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 20，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，7 个样本，一致性 57%
- 调度器 最常用 karras，7 个样本，一致性 57%
- 重绘幅度 中位数 0.4，观测区间 0.37 - 1，7 个样本
- 高发问题（8/7 个样本）：Steps较低可能导致细节不足
