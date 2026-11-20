---
name: unknown_workflow_controlnet_upscale_sampler
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.599364
common_nodes: [BrushNet, BrushNetLoader, CannyEdgePreprocessor, ControlNetApplyAdvanced, ControlNetLoader, Efficient Loader, Image Comparer (rgthree), ImageScale, ImageScaleBy, ImageToMask, ImageUpscaleWithModel, KSampler (Efficient), LayerMask: MaskGrow, LayerMask: SegmentAnythingUltra V2, LayerUtility: ExtendCanvas, LayerUtility: ImageBlend, LoadImage, MaskToImage, PreviewImage, SaveImage, TextInput_, UpscaleModelLoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/Qwen动作迁移工作流（4步加速）_2078835752565301249.json, 图片生成/图生图/产品不变换背景（Flux精修版）_1985610522949300225.json, 图片生成/图生图/产品换背景（高还原度）_1990685291251994626.json, 图片生成/图生图/工作流项目篇11-人像摄影工作流—蒙版做的好，效果越好Flux优化+flux.2分布流打光_2051945160363261953.json, 图片生成/文生图/SDXL+controlnet控制+SD放大+换背景精修工作流_1988876688975081474.json, 平台全量/产品不变换背景_1980430973030608897.json, 平台全量/产品不变换背景（Flux精修版）_2008007768636133378.json, 平台全量/产品不变换背景（Flux精修版）_2061375590552395777.json, 平台全量/产品换背景（高还原度）_1954860648795561985.json, 平台全量/产品细节不变换背景_1953650392561319938.json, 平台全量/工作流项目篇7-电商场景图制作(产品不变换背景Flux精修版)_1975876206421741570.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_sampler

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen动作迁移工作流（4步加速）_2078835752565301249.json、图片生成/图生图/产品不变换背景（Flux精修版）_1985610522949300225.json、图片生成/图生图/产品换背景（高还原度）_1990685291251994626.json、图片生成/图生图/工作流项目篇11-人像摄影工作流—蒙版做的好，效果越好Flux优化+flux.2分布流打光_2051945160363261953.json、图片生成/文生图/SDXL+controlnet控制+SD放大+换背景精修工作流_1988876688975081474.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 11 个 workflow 都包含：
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
- `CLIPTextEncodeFlux` —— 10/11 个有
- `ConditioningZeroOut` —— 10/11 个有
- `DetailerForEachDebug` —— 10/11 个有
- `DualCLIPLoader` —— 10/11 个有
- `EmptyLatentImage` —— 10/11 个有
- `ImpactDilateMask` —— 10/11 个有
- `MaskToSEGS` —— 10/11 个有
- `PreviewMask_` —— 10/11 个有
- `UNETLoader` —— 10/11 个有
- `VAELoader` —— 10/11 个有
- `easy cleanGpuUsed` —— 10/11 个有
- `MathExpression|pysssss` —— 9/11 个有
- `CLIPTextEncode` —— 2/11 个有
- `IPAdapterAdvanced` —— 2/11 个有
- `IPAdapterUnifiedLoader` —— 2/11 个有
- `easy imageScaleDownToSize` —— 2/11 个有
- `CFGGuider` —— 1/11 个有
- `CLIPLoader` —— 1/11 个有
- `CR Text` —— 1/11 个有
- `EmptyFlux2LatentImage` —— 1/11 个有
- `Flux2Scheduler` —— 1/11 个有
- `GetImageSize` —— 1/11 个有
- `ImageScaleToTotalPixels` —— 1/11 个有
- `KSamplerSelect` —— 1/11 个有
- `LayerUtility: PurgeVRAM` —— 1/11 个有
- `RandomNoise` —— 1/11 个有
- `ReferenceLatent` —— 1/11 个有
- `SamplerCustomAdvanced` —— 1/11 个有
- `UltimateSDUpscale` —— 1/11 个有
- `VAEDecode` —— 1/11 个有
- `VAEEncode` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.3 | 0.3 - 0.45 | 11 | 86% |
| 采样步数 | 28 | 25 - 30 | 11 | 96% |
| Prompt 约束强度(CFG) | 5 | 4.5 - 5 | 11 | 97% |
| 采样算法 | euler | - | 11 | 91% |
| 调度器 | karras | - | 11 | 100% |
| 重绘幅度 | 1 | 0.8 - 1 | 11 | 94% |
| 宽度 | 512 | 512 - 512 | 10 | 100% |
| 高度 | 512 | 512 - 512 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.3，观测区间 0.3 - 0.45，11 个样本，取值集中（一致性 86%）
- 采样步数 中位数 28，观测区间 25 - 30，11 个样本，取值集中（一致性 96%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 4.5 - 5，11 个样本，取值集中（一致性 97%）
- 采样算法 最常用 euler，11 个样本，一致性 91%
- 调度器 最常用 karras，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，11 个样本，取值集中（一致性 94%）
- 宽度 中位数 512，观测区间 512 - 512，10 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，10 个样本，取值集中（一致性 100%）
