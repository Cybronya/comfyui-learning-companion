---
name: unknown_workflow_sampler_clip_unet_146
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.811875
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CropWithPadInfo_EditUtils, EditTextEncode_EditUtils, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Flux2KleinOutputExtractor_EditUtils, GetNode, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux.2-Kelin9b服装花纹图案材质迁移_2059551610786893826.json, 图片生成/图生图/Flux.2-Kelin9b服装花纹图案材质迁移_2064562636724981762.json, 图片生成/图生图/Flux.2-Kelin服装材质花纹替换_2055455131566649345.json, 图片生成/图生图/Flux.2-Kelin服装材质花纹替换_2060199934435094530.json, 图片生成/图生图/flux2-klein提取线稿_2039330469845671938.json, 图片生成/图生图/一键提取线稿，无像素偏移_2039123243243675650.json, 图片生成/图生图/一键提取线稿，无像素偏移_2039168210997616642.json, 图片生成/文生图/Klein——材质替换_2047863366642835457.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_146

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Flux.2-Kelin9b服装花纹图案材质迁移_2059551610786893826.json、图片生成/图生图/Flux.2-Kelin9b服装花纹图案材质迁移_2064562636724981762.json、图片生成/图生图/Flux.2-Kelin服装材质花纹替换_2055455131566649345.json、图片生成/图生图/Flux.2-Kelin服装材质花纹替换_2060199934435094530.json、图片生成/图生图/flux2-klein提取线稿_2039330469845671938.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 8 个 workflow 都包含：
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
- `CR Prompt Text` —— 5/8 个有
- `Image Input Switch` —— 5/8 个有
- `ImageUpscaleWithModel` —— 5/8 个有
- `LayerUtility: PurgeVRAM V2` —— 5/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `UpscaleModelLoader` —— 5/8 个有
- `ZML_ArithmeticComparison` —— 5/8 个有
- `easy imageSizeByLongerSide` —— 5/8 个有
- `easy int` —— 5/8 个有
- `ttN concat` —— 5/8 个有
- `Int` —— 4/8 个有
- `easy cleanGpuUsed` —— 3/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 7 | 8 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.3 | 8 | 87% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 7，8 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.3，8 个样本，取值集中（一致性 87%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
