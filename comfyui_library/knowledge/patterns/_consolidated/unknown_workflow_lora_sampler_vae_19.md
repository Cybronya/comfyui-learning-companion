---
name: unknown_workflow_lora_sampler_vae_19
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.89225
common_nodes: [CLIPLoader, ConditioningZeroOut, CropWithPadInfo, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, QwenEditConfigPreparer, QwenEditOutputExtractor, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/局部重绘-Qwen-Eidt-2511-模板_2050108545886109698.json, 图片生成/图生图/老孙AI零偏移遮罩精细改图_2094250916902952962.json, 平台全量/局部重绘·超真实移除、修手等_2007497072643153921.json, 视频生成/图生视频/单图编辑+遮罩区域+局部重绘_2068053816934756353.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_19

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/局部重绘-Qwen-Eidt-2511-模板_2050108545886109698.json、图片生成/图生图/老孙AI零偏移遮罩精细改图_2094250916902952962.json、平台全量/局部重绘·超真实移除、修手等_2007497072643153921.json、视频生成/图生视频/单图编辑+遮罩区域+局部重绘_2068053816934756353.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `CropWithPadInfo`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `ImageAndMaskPreview` —— 2/4 个有
- `InpaintCrop` —— 2/4 个有
- `InpaintCropImproved` —— 2/4 个有
- `InpaintStitch` —— 2/4 个有
- `InpaintStitchImproved` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `SeedVR2LoadDiTModel` —— 2/4 个有
- `SeedVR2LoadVAEModel` —— 2/4 个有
- `SeedVR2VideoUpscaler` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 4 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
