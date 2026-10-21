---
name: unknown_workflow_sampler_clip_unet_178
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.886667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, ImpactInt, KSamplerAdvanced, ModelSamplingSD3, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text, Note Plus (mtb), Switch any [Crystools], CR Text Concatenate]
members: [图片生成/文生图/1950520595349950466.json, 图片生成/文生图/1969678776999288833.json, 图片生成/文生图/LH-DMT-017.WAN2.2文生图_2016175288681504770.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_178

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1950520595349950466.json、图片生成/文生图/1969678776999288833.json、图片生成/文生图/LH-DMT-017.WAN2.2文生图_2016175288681504770.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `ImpactInt`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `Float` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `Switch any [Crystools]` —— 1/3 个有
- `easy positive` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 12 | 12 - 25 | 3 | 62% |
| 采样算法 | 1 | 1 - 5 | 3 | 19% |
| 调度器 | euler | - | 3 | 67% |
| 重绘幅度 | beta | - | 3 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 12，观测区间 12 - 25，3 个样本
- 采样算法 中位数 1，观测区间 1 - 5，3 个样本，取值分散，一致性仅 19%
- 调度器 最常用 euler，3 个样本，一致性 67%
- 重绘幅度 最常用 beta，3 个样本，一致性 67%
- 风险：Prompt 约束强度(CFG) 观测到 25，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、Note Plus (mtb)、Switch any [Crystools]、CR Text Concatenate
