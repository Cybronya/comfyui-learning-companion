---
name: unknown_workflow_sampler_vae_64
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.938
common_nodes: [CR SDXL Aspect Ratio, EmptyLatentImage, KSampler, KSampler (Efficient), LoadImage, RHHiddenNodes, SaveImage, Text Concatenate, Text Multiline, TextEncodeQwenImageEditPlus, VAEDecode, workflow>g1, workflow>image handle g2]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/G-N-QEAv5-双人图像编辑、动作交互、人物一致性_1981287481838567426.json, 图片生成/图生图/G-N-QEAv5工作流-米1021双人图像编辑、动作交互、人物一致性_1980528125870260225.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_64

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/G-N-QEAv5-双人图像编辑、动作交互、人物一致性_1981287481838567426.json、图片生成/图生图/G-N-QEAv5工作流-米1021双人图像编辑、动作交互、人物一致性_1980528125870260225.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CR SDXL Aspect Ratio`
- `EmptyLatentImage`
- `KSampler`
- `KSampler (Efficient)`
- `LoadImage`
- `RHHiddenNodes`
- `SaveImage`
- `Text Concatenate`
- `Text Multiline`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `workflow>g1`
- `workflow>image handle g2`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1536 | - | 2 | 100% |
| 高度 | 2048 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 2048，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
