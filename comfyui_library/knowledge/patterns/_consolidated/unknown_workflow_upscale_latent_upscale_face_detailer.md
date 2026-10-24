---
name: unknown_workflow_upscale_latent_upscale_face_detailer
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [Efficient Loader, FaceDetailer, KSampler (Efficient), LatentUpscaleBy, Noise Control Script, SAMLoader, SaveImage, UltralyticsDetectorProvider]
problems: []
missing: []
members: [图片生成/图生图/Cy2基础工作流_2083001837002776577.json, 图片生成/文生图/Cy2基础工作流_2047141231335055361.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_face_detailer

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Cy2基础工作流_2083001837002776577.json、图片生成/文生图/Cy2基础工作流_2047141231335055361.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `Efficient Loader`
- `FaceDetailer`
- `KSampler (Efficient)`
- `LatentUpscaleBy`
- `Noise Control Script`
- `SAMLoader`
- `SaveImage`
- `UltralyticsDetectorProvider`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.5 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
