---
name: unknown_workflow_inpaint_sampler_clip_75
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.479
common_nodes: [CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, EmptyImage, FluxGuidance, GetNode, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), GrowMask, ImageConcanate, ImageResizeKJ, InpaintModelConditioning, KSampler, LoadImage, MaskPreview+, PreviewImage, ReduxAdvanced, SAMLoader, SaveImage, SetNode, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/2025_顶级虚拟试穿_workflow_SoilSihgStudio_1895504246614196226.json, 平台全量/人物角色一致性，指定人物换指定动作，适合视频脚本分镜制作_1971478315464867841.json, 平台全量/服装电商（2_5）：图-换脸+换装+换姿势+换背景 _ Redux+FluxFill_1925364946534866945.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_75

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2025_顶级虚拟试穿_workflow_SoilSihgStudio_1895504246614196226.json、平台全量/人物角色一致性，指定人物换指定动作，适合视频脚本分镜制作_1971478315464867841.json、平台全量/服装电商（2_5）：图-换脸+换装+换姿势+换背景 _ Redux+FluxFill_1925364946534866945.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：48%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyImage`
- `FluxGuidance`
- `GetNode`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `GrowMask`
- `ImageConcanate`
- `ImageResizeKJ`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `MaskPreview+`
- `PreviewImage`
- `ReduxAdvanced`
- `SAMLoader`
- `SaveImage`
- `SetNode`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ControlNetApplyAdvanced` —— 2/3 个有
- `ControlNetLoader` —— 2/3 个有
- `ImageAndMaskPreview` —— 2/3 个有
- `ImageCrop` —— 2/3 个有
- `ImageToMask` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `MaskToImage` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `CR Image Input Switch` —— 1/3 个有
- `DepthAnythingV2Preprocessor` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `GetImageRangeFromBatch` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageCompositeMasked` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `PlaySound|pysssss` —— 1/3 个有
- `Preview Chooser` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `TeaCache` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 0.725 | - | 2 | 83% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.725，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
