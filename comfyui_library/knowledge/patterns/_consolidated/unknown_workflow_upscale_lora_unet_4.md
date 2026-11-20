---
name: unknown_workflow_upscale_lora_unet_4
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.89725
common_nodes: [CLIPLoader, GetImageSize, GrowMaskWithBlur, Image Comparer (rgthree), ImageColorMatchAdobe+, LayerColor: Exposure, LayerFilter: FilmV2, LayerMask: PersonMaskUltra V2, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, PrimitiveInt, RHHiddenNodes, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAELoader, ZML_ImageSelectorNode, easy imageConcat, easy imageRemBg]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/“手机里全是废片？朋友圈直接封神！”FireRed_千问Qwen一键换背景场景换装+换头换脸可选！_2071492088218341378.json, 平台全量/千问QWEN换背景场景换装+换头可选！_2076937095834333186.json, 平台全量/千问QWEN换背景场景换装+换头可选！_2077203547833323521.json, 平台全量/土味自拍_到_国际超模_！商用级别！克莱因FluxKlein换背景场景+换装！换头可选，自然无痕！_2067593214256832513.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_unet_4

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/“手机里全是废片？朋友圈直接封神！”FireRed_千问Qwen一键换背景场景换装+换头换脸可选！_2071492088218341378.json、平台全量/千问QWEN换背景场景换装+换头可选！_2076937095834333186.json、平台全量/千问QWEN换背景场景换装+换头可选！_2077203547833323521.json、平台全量/土味自拍_到_国际超模_！商用级别！克莱因FluxKlein换背景场景+换装！换头可选，自然无痕！_2067593214256832513.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `GetImageSize`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageColorMatchAdobe+`
- `LayerColor: Exposure`
- `LayerFilter: FilmV2`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `RHHiddenNodes`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAELoader`
- `ZML_ImageSelectorNode`
- `easy imageConcat`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `FlexLoraLoaderModelOnly` —— 3/4 个有
- `ImageScale` —— 3/4 个有
- `QwenImageIntegratedKSampler` —— 3/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `KSampler` —— 1/4 个有
- `PainterFluxImageEdit` —— 1/4 个有
- `VAEDecode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 图生图 image-to-image | - | 4 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | 1440 | 1440 - 1440 | 3 | 100% |
| 调度器 | 1440 | 1440 - 1440 | 3 | 100% |
| 重绘幅度 | 3.81742e+14 | 1 - 9.31005e+14 | 4 | 17% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 图生图 image-to-image，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1440，观测区间 1440 - 1440，3 个样本，取值集中（一致性 100%）
- 调度器 中位数 1440，观测区间 1440 - 1440，3 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 3.81742e+14，观测区间 1 - 9.31005e+14，4 个样本，取值分散，一致性仅 17%
- 风险：重绘幅度 观测到 9.31005e+14，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
