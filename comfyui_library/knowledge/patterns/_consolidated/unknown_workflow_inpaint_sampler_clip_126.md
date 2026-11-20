---
name: unknown_workflow_inpaint_sampler_clip_126
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.909
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageConcanate, ImageCrop+, ImageResize+, ImageToMask, InpaintCrop, InpaintModelConditioning, InpaintStitch, KSampler, LayerUtility: ColorImage, LoadImage, MaskToImage, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy imageSize]
problems: []
missing: []
members: [平台全量/【星汇工作流】万物迁移Pro_1909549374517424130.json, 平台全量/电商服饰+智能更换服装+手动遮罩_1971595784175153153.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_126

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/【星汇工作流】万物迁移Pro_1909549374517424130.json、平台全量/电商服饰+智能更换服装+手动遮罩_1971595784175153153.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageConcanate`
- `ImageCrop+`
- `ImageResize+`
- `ImageToMask`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `KSampler`
- `LayerUtility: ColorImage`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoader` —— 1/2 个有
- `DeepTranslatorTextNode` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `LayerMask: BiRefNetUltra` —— 1/2 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `ResizeMask` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有
- `UltimateSDUpscale` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy showTensorShape` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
