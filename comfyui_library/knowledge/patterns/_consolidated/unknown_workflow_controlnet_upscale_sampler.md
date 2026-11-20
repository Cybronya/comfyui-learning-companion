---
name: unknown_workflow_controlnet_upscale_sampler
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.6222
common_nodes: [BrushNet, BrushNetLoader, CannyEdgePreprocessor, ControlNetApplyAdvanced, ControlNetLoader, Efficient Loader, Image Comparer (rgthree), ImageScale, ImageScaleBy, ImageToMask, ImageUpscaleWithModel, KSampler (Efficient), LayerMask: MaskGrow, LayerMask: SegmentAnythingUltra V2, LayerUtility: ExtendCanvas, LayerUtility: ImageBlend, LoadImage, MaskToImage, PreviewImage, SaveImage, TextInput_, UpscaleModelLoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/Qwen动作迁移工作流（4步加速）_2078835752565301249.json, 图片生成/图生图/产品不变换背景（Flux精修版）_1985610522949300225.json, 图片生成/图生图/产品换背景（高还原度）_1990685291251994626.json, 图片生成/图生图/工作流项目篇11-人像摄影工作流—蒙版做的好，效果越好Flux优化+flux.2分布流打光_2051945160363261953.json, 图片生成/文生图/SDXL+controlnet控制+SD放大+换背景精修工作流_1988876688975081474.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_sampler

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen动作迁移工作流（4步加速）_2078835752565301249.json、图片生成/图生图/产品不变换背景（Flux精修版）_1985610522949300225.json、图片生成/图生图/产品换背景（高还原度）_1990685291251994626.json、图片生成/图生图/工作流项目篇11-人像摄影工作流—蒙版做的好，效果越好Flux优化+flux.2分布流打光_2051945160363261953.json、图片生成/文生图/SDXL+controlnet控制+SD放大+换背景精修工作流_1988876688975081474.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 5 个 workflow 都包含：
- `BrushNet`
- `BrushNetLoader`
- `CannyEdgePreprocessor`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `Efficient Loader`
- `Image Comparer (rgthree)`
- `ImageScale`
- `ImageScaleBy`
- `ImageToMask`
- `ImageUpscaleWithModel`
- `KSampler (Efficient)`
- `LayerMask: MaskGrow`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ExtendCanvas`
- `LayerUtility: ImageBlend`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `TextInput_`
- `UpscaleModelLoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 4/5 个有
- `ConditioningZeroOut` —— 4/5 个有
- `DetailerForEachDebug` —— 4/5 个有
- `DualCLIPLoader` —— 4/5 个有
- `EmptyLatentImage` —— 4/5 个有
- `ImpactDilateMask` —— 4/5 个有
- `MaskToSEGS` —— 4/5 个有
- `PreviewMask_` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `VAELoader` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `MathExpression|pysssss` —— 3/5 个有
- `CLIPTextEncode` —— 2/5 个有
- `IPAdapterAdvanced` —— 2/5 个有
- `IPAdapterUnifiedLoader` —— 2/5 个有
- `easy imageScaleDownToSize` —— 2/5 个有
- `CFGGuider` —— 1/5 个有
- `CLIPLoader` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `EmptyFlux2LatentImage` —— 1/5 个有
- `Flux2Scheduler` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `KSamplerSelect` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `RandomNoise` —— 1/5 个有
- `ReferenceLatent` —— 1/5 个有
- `SamplerCustomAdvanced` —— 1/5 个有
- `UltimateSDUpscale` —— 1/5 个有
- `VAEDecode` —— 1/5 个有
- `VAEEncode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.3 | 0.3 - 0.45 | 5 | 82% |
| 采样步数 | 28 | 25 - 30 | 5 | 94% |
| Prompt 约束强度(CFG) | 5 | 4.5 - 5 | 5 | 96% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | karras | - | 5 | 100% |
| 重绘幅度 | 1 | 0.8 - 1 | 5 | 92% |
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.3，观测区间 0.3 - 0.45，5 个样本，取值集中（一致性 82%）
- 采样步数 中位数 28，观测区间 25 - 30，5 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 4.5 - 5，5 个样本，取值集中（一致性 96%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 karras，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，5 个样本，取值集中（一致性 92%）
- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
