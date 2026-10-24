---
name: text_to_image_controlnet_upscale_sampler
type: Text To Image
frequency: 2
level: weak
coverage: 0.8175
common_nodes: [AILab_QwenVL, AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, GetImageSize, Image Comparer (rgthree), ImageResize+, ImageScaleBy, ImageUpscaleWithModel, ImpactConditionalBranch, ImpactSwitch, Int, KSampler, LatentSwitch, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchLoader, PreviewImage, PrimitiveInt, QwenImageDiffsynthControlnet, SDPoseOODLoader, SDPoseOODProcessor, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader, YOLOModelLoader, easy cleanGpuUsed, easy imageIndexSwitch, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/z-image一键反推提示词+洗图重绘图像+高清修复+直出8K画质_1999684041454612482.json, 图片生成/文生图/Z-image-最全面工作流（反推_CN_高清放大）10K输出_1999450574514946050.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_sampler

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/z-image一键反推提示词+洗图重绘图像+高清修复+直出8K画质_1999684041454612482.json、图片生成/文生图/Z-image-最全面工作流（反推_CN_高清放大）10K输出_1999450574514946050.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `ImpactConditionalBranch`
- `ImpactSwitch`
- `Int`
- `KSampler`
- `LatentSwitch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchLoader`
- `PreviewImage`
- `PrimitiveInt`
- `QwenImageDiffsynthControlnet`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `YOLOModelLoader`
- `easy cleanGpuUsed`
- `easy imageIndexSwitch`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 2048 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 2048，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
