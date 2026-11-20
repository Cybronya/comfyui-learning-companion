---
name: unknown_workflow_inpaint_sampler_clip_95
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.89
common_nodes: [CLIPTextEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, PreviewImage, ReduxAdvanced, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX_fill+redux-电商换服装_1917398502257922049.json, 平台全量/Flux接近完美的丰胸工作流_1906896962761920514.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_95

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/FLUX_fill+redux-电商换服装_1917398502257922049.json、平台全量/Flux接近完美的丰胸工作流_1906896962761920514.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ReduxAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Color Panel` —— 1/2 个有
- `CR Simple Image Compare` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `Image To Mask` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `JWImageResizeByLongerSide` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `Note _O` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 0.85 | - | 2 | 82% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 重绘幅度 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 82%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
