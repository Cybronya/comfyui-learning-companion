---
name: unknown_workflow_inpaint_sampler_clip_9
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.911625
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, FluxGuidance, ImageConcanate, ImageToMask, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/20250409物体迁移_1909954953488859137.json, 图片生成/图生图/FLUX  redux万物迁移_1985947090641723393.json, 图片生成/图生图/FLUX-redux-万物迁移_1953070587368435713.json, 图片生成/图生图/FLUX_FILL_服装替换工作流_250423_1915792243381440513.json, 图片生成/图生图/产品替换-flux2_2093881686802124802.json, 图片生成/图生图/产品替换-flux2_2093903856055963650.json, 图片生成/图生图/产品替换_产品迁移-2.0_1955631871608721409.json, 视频生成/图生视频/产品替换-flux_2075840561986236417.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_9

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/20250409物体迁移_1909954953488859137.json、图片生成/图生图/FLUX  redux万物迁移_1985947090641723393.json、图片生成/图生图/FLUX-redux-万物迁移_1953070587368435713.json、图片生成/图生图/FLUX_FILL_服装替换工作流_250423_1915792243381440513.json、图片生成/图生图/产品替换-flux2_2093881686802124802.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageConcanate`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskToImage`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `StyleModelApply` —— 7/8 个有
- `GetImageSize+` —— 6/8 个有
- `ImageCrop` —— 6/8 个有
- `RMBG` —— 6/8 个有
- `easy imageSize` —— 5/8 个有
- `Anything Everywhere3` —— 4/8 个有
- `DifferentialDiffusion` —— 4/8 个有
- `Int` —— 4/8 个有
- `ModelSamplingFlux` —— 4/8 个有
- `Anything Everywhere` —— 2/8 个有
- `DetailTransfer` —— 1/8 个有
- `Image Blank` —— 1/8 个有
- `ImageCrop+` —— 1/8 个有
- `ImageResize+` —— 1/8 个有
- `LayerMask: SegmentAnythingUltra` —— 1/8 个有
- `LayerUtility: HLFrequencyDetailRestore` —— 1/8 个有
- `Mask Fill Holes` —— 1/8 个有
- `MaskPreview+` —— 1/8 个有
- `StyleModelApplyAdvanced` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 8 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | normal | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，8 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 normal，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
