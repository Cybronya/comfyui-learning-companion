---
name: unknown_workflow_controlnet_inpaint_sampler_7
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8602
common_nodes: [ApplyInstantID, CLIPTextEncode, CheckpointLoaderSimple, ColorMatch, ControlNetApplyAdvanced, ControlNetLoader, CropFace, DifferentialDiffusion, ImageFromBatch, ImpactMakeImageBatch, ImpactSEGSToMaskBatch, ImpactSimpleDetectorSEGS, InpaintCrop, InpaintModelConditioning, InpaintStitch, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerMask: MaskGrow, LoadImage, MaskFromBatch+, MaskToImage, PreviewImage, SAMLoader, SaveImage, UltralyticsDetectorProvider, VAEDecode, easy forLoopEnd, easy forLoopStart, easy imageCount]
problems: []
missing: []
members: [图片生成/图生图/单，多人换脸工作流_2059153660030050306.json, 图片生成/图生图/多人换脸_双人换脸_多人合照V3.0 (2)_1989714890313093121.json, 平台全量/双人换脸-简洁候选_2071275305674825730.json, 平台全量/旅拍机-淘汰-单人多人205915-运行失败_2071280262004166657.json, 平台全量/旅拍机-淘汰-双人换脸简洁候选-SAM加载失败_2071276678403416065.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_sampler_7

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/单，多人换脸工作流_2059153660030050306.json、图片生成/图生图/多人换脸_双人换脸_多人合照V3.0 (2)_1989714890313093121.json、平台全量/双人换脸-简洁候选_2071275305674825730.json、平台全量/旅拍机-淘汰-单人多人205915-运行失败_2071280262004166657.json、平台全量/旅拍机-淘汰-双人换脸简洁候选-SAM加载失败_2071276678403416065.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `ApplyInstantID`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `CropFace`
- `DifferentialDiffusion`
- `ImageFromBatch`
- `ImpactMakeImageBatch`
- `ImpactSEGSToMaskBatch`
- `ImpactSimpleDetectorSEGS`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LayerMask: MaskGrow`
- `LoadImage`
- `MaskFromBatch+`
- `MaskToImage`
- `PreviewImage`
- `SAMLoader`
- `SaveImage`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`

**可变部分**（部分 workflow 才有）：
- `ApplyPulid` —— 4/5 个有
- `FaceAnalysisModels` —— 4/5 个有
- `FaceEmbedDistance` —— 4/5 个有
- `Image Comparer (rgthree)` —— 4/5 个有
- `LoraLoader` —— 4/5 个有
- `PulidEvaClipLoader` —— 4/5 个有
- `PulidInsightFaceLoader` —— 4/5 个有
- `PulidModelLoader` —— 4/5 个有
- `ReActorFaceSwap` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.45 | 0.45 - 0.45 | 5 | 100% |
| LoRA 模型强度 | 1.1 | 1 - 1.2 | 4 | 91% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |
| 采样步数 | 15 | 15 - 15 | 5 | 100% |
| Prompt 约束强度(CFG) | 2 | 1.5 - 2 | 5 | 89% |
| 采样算法 | euler_ancestral | - | 5 | 100% |
| 调度器 | sgm_uniform | - | 5 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.6 | 5 | 82% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.45，观测区间 0.45 - 0.45，5 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1.1，观测区间 1 - 1.2，4 个样本，取值集中（一致性 91%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 15，观测区间 15 - 15，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，观测区间 1.5 - 2，5 个样本，取值集中（一致性 89%）
- 采样算法 最常用 euler_ancestral，5 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.6，5 个样本，取值集中（一致性 82%）
