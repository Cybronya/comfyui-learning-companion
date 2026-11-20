---
name: unknown_workflow_inpaint_sampler_clip_41
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.6418
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageConcanate, ImageCrop, ImageResize+, InpaintCrop, InpaintModelConditioning, InpaintStitch, KSampler, LoadImage, PreviewBridge, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/ComFyUI + FLUX 服装模特_1922202039659724802.json, 图片生成/图生图/FLUX万物迁移工作流_2080931467076661250.json, 图片生成/图生图/万物迁移FLUX_2003089726859091969.json, 图片生成/图生图/万物迁移FLUX_2010309532425129985.json, 平台全量/FLUX万物迁移工作流_2008887423425585154.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_41

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/ComFyUI + FLUX 服装模特_1922202039659724802.json、图片生成/图生图/FLUX万物迁移工作流_2080931467076661250.json、图片生成/图生图/万物迁移FLUX_2003089726859091969.json、图片生成/图生图/万物迁移FLUX_2010309532425129985.json、平台全量/FLUX万物迁移工作流_2008887423425585154.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageConcanate`
- `ImageCrop`
- `ImageResize+`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `KSampler`
- `LoadImage`
- `PreviewBridge`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 4/5 个有
- `ImageScaleBy` —— 4/5 个有
- `ImageUpscaleWithModel` —— 4/5 个有
- `MathExpression|pysssss` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `UpscaleModelLoader` —— 4/5 个有
- `easy imageInsetCrop` —— 4/5 个有
- `GrowMask` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `Image To Mask` —— 1/5 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/5 个有
- `LayerUtility: ExtendCanvas` —— 1/5 个有
- `MaskToImage` —— 1/5 个有
- `preview_mask` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 5 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，5 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
