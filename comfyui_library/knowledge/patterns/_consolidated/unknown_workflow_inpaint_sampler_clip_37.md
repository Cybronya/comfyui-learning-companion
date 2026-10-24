---
name: unknown_workflow_inpaint_sampler_clip_37
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.92725
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GetImageSize, InpaintModelConditioning, Joy_caption_two, Joy_caption_two_load, KSampler, LayerUtility: ImageShift, LoadImage, MathExpression|pysssss, PreviewImage, SaveImage, StringConcatenate, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/无缝衔接——四方连续（升级版）_2009277350545985537.json, 图片生成/图生图/无缝贴图 _ 贴图无缝处理_1965422039286824962.json, 图片生成/图生图/无缝贴图——四方连续（升级版）_1978667632985526273.json, 图片生成/图生图/砖形无缝贴图_1970702047538540546.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_37

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/无缝衔接——四方连续（升级版）_2009277350545985537.json、图片生成/图生图/无缝贴图 _ 贴图无缝处理_1965422039286824962.json、图片生成/图生图/无缝贴图——四方连续（升级版）_1978667632985526273.json、图片生成/图生图/砖形无缝贴图_1970702047538540546.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetImageSize`
- `InpaintModelConditioning`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `LayerUtility: ImageShift`
- `LoadImage`
- `MathExpression|pysssss`
- `PreviewImage`
- `SaveImage`
- `StringConcatenate`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageAndMaskPreview` —— 3/4 个有
- `ImageConcatFromBatch` —— 3/4 个有
- `ImageResize+` —— 3/4 个有
- `ImageRotate` —— 3/4 个有
- `ImageToMask` —— 3/4 个有
- `MaskBlur+` —— 3/4 个有
- `RHHiddenNodes` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `easy int` —— 3/4 个有
- `ImageBatchRepeatInterleaving` —— 2/4 个有
- `Label (rgthree)` —— 2/4 个有
- `CropMask` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `ImageCrop` —— 1/4 个有
- `ImpactMakeImageBatch` —— 1/4 个有
- `MaskMathOps` —— 1/4 个有
- `MaskPreview` —— 1/4 个有
- `UNETLoader` —— 1/4 个有
- `easy makeImageForICLora` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
