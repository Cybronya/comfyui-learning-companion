---
name: unknown_workflow_inpaint_sampler_clip_130
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.563
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, FluxGuidance, GetNode, InpaintModelConditioning, KSampler, LoadImage, PreviewImage, SaveImage, SetNode, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/电商服装自定义换装-产品换背景_1885977101181546497.json, 平台全量/软装改图工作流_1925760315294699521.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_130

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/电商服装自定义换装-产品换背景_1885977101181546497.json、平台全量/软装改图工作流_1925760315294699521.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetNode`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AddMaskForICLora` —— 1/2 个有
- `ConstrainImage|pysssss` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageCrop` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `PreviewBridge` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 1.5 | - | 2 | 67% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1.5，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
