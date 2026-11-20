---
name: unknown_workflow_sampler_clip_unet_130
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.7987
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CropWithPadInfo_EditUtils, EditTextEncode_EditUtils, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Flux2KleinOutputExtractor_EditUtils, GetNode, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux.2-Kelin9b服装花纹图案材质迁移_2059551610786893826.json, 图片生成/图生图/Flux.2-Kelin9b服装花纹图案材质迁移_2064562636724981762.json, 图片生成/图生图/Flux.2-Kelin服装材质花纹替换_2055455131566649345.json, 图片生成/图生图/Flux.2-Kelin服装材质花纹替换_2060199934435094530.json, 图片生成/图生图/flux2-klein提取线稿_2039330469845671938.json, 图片生成/图生图/一键提取线稿，无像素偏移_2039123243243675650.json, 图片生成/图生图/一键提取线稿，无像素偏移_2039168210997616642.json, 图片生成/文生图/Klein——材质替换_2047863366642835457.json, 平台全量/万物迁移——Klein双手绘局部重绘_2028849501011709953.json, 平台全量/材质替换——Klein_2038817808447971330.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_130

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Flux.2-Kelin9b服装花纹图案材质迁移_2059551610786893826.json、图片生成/图生图/Flux.2-Kelin9b服装花纹图案材质迁移_2064562636724981762.json、图片生成/图生图/Flux.2-Kelin服装材质花纹替换_2055455131566649345.json、图片生成/图生图/Flux.2-Kelin服装材质花纹替换_2060199934435094530.json、图片生成/图生图/flux2-klein提取线稿_2039330469845671938.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CropWithPadInfo_EditUtils`
- `EditTextEncode_EditUtils`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Flux2KleinOutputExtractor_EditUtils`
- `GetNode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 7/10 个有
- `LayerUtility: PurgeVRAM V2` —— 7/10 个有
- `LoraLoaderModelOnly` —— 7/10 个有
- `UpscaleModelLoader` —— 7/10 个有
- `easy imageSizeByLongerSide` —— 7/10 个有
- `easy int` —— 7/10 个有
- `CR Prompt Text` —— 6/10 个有
- `Image Input Switch` —— 6/10 个有
- `ZML_ArithmeticComparison` —— 6/10 个有
- `ttN concat` —— 6/10 个有
- `Int` —— 4/10 个有
- `easy cleanGpuUsed` —— 3/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `ImageConcanate` —— 1/10 个有
- `ImpactSwitch` —— 1/10 个有
- `InpaintCrop` —— 1/10 个有
- `InpaintStitch` —— 1/10 个有
- `KOOK_ImageCompression` —— 1/10 个有
- `LayerUtility: CropByMask V2` —— 1/10 个有
- `MaskFillHoles` —— 1/10 个有
- `QwenEditConfigPreparer` —— 1/10 个有
- `easy positive` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 7 | 10 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.3 | 10 | 87% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 7，10 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.3，10 个样本，取值集中（一致性 87%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
