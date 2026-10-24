---
name: unknown_workflow_inpaint_sampler_clip_67
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9615
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageResize+, InpaintModelConditioning, KSampler, LoadImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/inpaint换装_2064937761035087873.json, 图片生成/图生图/换服装_1925438719170650113.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_67

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/inpaint换装_2064937761035087873.json、图片生成/图生图/换服装_1925438719170650113.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageResize+`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 1/2 个有
- `ImageCrop` —— 1/2 个有
- `ImageRemoveAlpha+` —— 1/2 个有
- `InpaintCropImproved` —— 1/2 个有
- `InpaintStitchImproved` —— 1/2 个有
- `LayerMask: BiRefNetUltra` —— 1/2 个有
- `LayerMask: MaskPreview` —— 1/2 个有
- `PreviewBridge` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `easy makeImageForICLora` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
