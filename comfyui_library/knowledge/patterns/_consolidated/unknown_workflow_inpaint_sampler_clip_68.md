---
name: unknown_workflow_inpaint_sampler_clip_68
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.95
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ImagePadForOutpaint, KSampler, LoadImage, SaveImage, VAEDecode, VAEEncodeForInpaint]
problems: []
missing: []
members: [图片生成/图生图/「背景延展 _ Outpainting」_2110961289022492673.json, 图片生成/图生图/扩图_2057399705939832833.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_68

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/「背景延展 _ Outpainting」_2110961289022492673.json、图片生成/图生图/扩图_2057399705939832833.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ImagePadForOutpaint`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncodeForInpaint`

**可变部分**（部分 workflow 才有）：
- `ImageCompositeMasked` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22 | - | 2 | 91% |
| Prompt 约束强度(CFG) | 5.75 | - | 2 | 96% |
| 采样算法 | dpmpp_2m_sde | - | 2 | 50% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 5.75，样本不足，未给区间，2 个样本，取值集中（一致性 96%）
- 采样算法 最常用 dpmpp_2m_sde，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
