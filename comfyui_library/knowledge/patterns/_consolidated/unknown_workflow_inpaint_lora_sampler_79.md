---
name: unknown_workflow_inpaint_lora_sampler_79
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [AddMaskForICLora, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DownloadAndLoadFlorence2Model, DownloadAndLoadSAM2Model, DualCLIPLoaderGGUF, Florence2Run, Florence2toCoordinates, FluxGuidance, GetImageSize+, INPAINT_ExpandMask, ImageCrop+, ImageResize+, InpaintModelConditioning, KSampler, LoadImage, MaskPreview+, Sam2Segmentation, SaveImage, SimpleComparison+, SimpleCondition+, StyleModelApply, StyleModelLoader, UnetLoaderGGUF, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX.电商换装_2028359486963978242.json, 平台全量/FLUX.电商换装_1891866706665705473.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_79

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/FLUX.电商换装_2028359486963978242.json、平台全量/FLUX.电商换装_1891866706665705473.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `AddMaskForICLora`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DownloadAndLoadFlorence2Model`
- `DownloadAndLoadSAM2Model`
- `DualCLIPLoaderGGUF`
- `Florence2Run`
- `Florence2toCoordinates`
- `FluxGuidance`
- `GetImageSize+`
- `INPAINT_ExpandMask`
- `ImageCrop+`
- `ImageResize+`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `MaskPreview+`
- `Sam2Segmentation`
- `SaveImage`
- `SimpleComparison+`
- `SimpleCondition+`
- `StyleModelApply`
- `StyleModelLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
