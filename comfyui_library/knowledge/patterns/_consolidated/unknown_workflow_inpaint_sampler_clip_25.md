---
name: unknown_workflow_inpaint_sampler_clip_25
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9482
common_nodes: [BackgroundScaler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, EmptyImage, FluxGuidance, ImageConcanate, ImageToMask, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, PreviewBridge, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy imageInsetCrop]
problems: []
missing: []
members: [图片生成/图生图/【AI由北】万物迁移 服装通用_1900752010574970881.json, 图片生成/图生图/【AI由北】万物迁移 电商产品通用_1901648013259857922.json, 图片生成/图生图/万物迁移_1922474027976183810.json, 图片生成/图生图/模特+首饰穿戴海报 一键生图系列_1909418174545338370.json, 图片生成/图生图/电商产品-万物迁移-指定场景_1939509036557508610.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_25

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/【AI由北】万物迁移 服装通用_1900752010574970881.json、图片生成/图生图/【AI由北】万物迁移 电商产品通用_1901648013259857922.json、图片生成/图生图/万物迁移_1922474027976183810.json、图片生成/图生图/模特+首饰穿戴海报 一键生图系列_1909418174545338370.json、图片生成/图生图/电商产品-万物迁移-指定场景_1939509036557508610.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `BackgroundScaler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyImage`
- `FluxGuidance`
- `ImageConcanate`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskToImage`
- `PreviewBridge`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageInsetCrop`

**可变部分**（部分 workflow 才有）：
- `InpaintCrop` —— 4/5 个有
- `InpaintStitch` —— 4/5 个有
- `LayerMask: BiRefNetUltra` —— 4/5 个有
- `GetNode` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `LayerMask: BiRefNetUltraV2` —— 1/5 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/5 个有
- `LayerMask: MaskEdgeUltraDetail V2` —— 1/5 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/5 个有
- `PreviewImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
