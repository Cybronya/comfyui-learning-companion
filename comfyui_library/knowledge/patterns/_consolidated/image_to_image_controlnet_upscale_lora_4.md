---
name: image_to_image_controlnet_upscale_lora_4
type: Image To Image
frequency: 2
level: weak
coverage: 0.489
common_nodes: [AILab_QwenVL, AIO_Preprocessor, Anything Everywhere3, CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, DWPreprocessor, Fast Groups Bypasser (rgthree), GetImageSize, GetNode, ImageResizeKJv2, ImageSmartSharpen+, ImpactSwitch, JWInteger, KSampler, LatentPixelScale, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, MuterSwitcher, PreviewImage, RebatchLatents, RepeatLatentBatch, SaveImage, SetNode, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, ZImageFunControlnet, easy boolean, easy imageRemBg, easy seed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/造相Z-image Controlnet union 姿势_深度_线稿_重绘 四合一 pose参考_1996350694477152257.json, 图片生成/文生图/造相Z-image Controlnet union 姿势_深度_线稿_重绘 四合一 pose参考_2013930008091299841.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_lora_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/造相Z-image Controlnet union 姿势_深度_线稿_重绘 四合一 pose参考_1996350694477152257.json、图片生成/文生图/造相Z-image Controlnet union 姿势_深度_线稿_重绘 四合一 pose参考_2013930008091299841.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：49%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `AIO_Preprocessor`
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `DWPreprocessor`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetNode`
- `ImageResizeKJv2`
- `ImageSmartSharpen+`
- `ImpactSwitch`
- `JWInteger`
- `KSampler`
- `LatentPixelScale`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `MuterSwitcher`
- `PreviewImage`
- `RebatchLatents`
- `RepeatLatentBatch`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `ZImageFunControlnet`
- `easy boolean`
- `easy imageRemBg`
- `easy seed`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | heun | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 heun，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
