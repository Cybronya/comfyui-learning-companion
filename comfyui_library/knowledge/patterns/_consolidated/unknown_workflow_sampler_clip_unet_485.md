---
name: unknown_workflow_sampler_clip_unet_485
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.842
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, FluxResolutionNode, KSamplerAdvanced, ModelSamplingAuraFlow, PrimitiveFloat, PrimitiveInt, SaveImage, UNETLoader, VAEDecode, VAEEncodeTiled, VAELoader, easy int]
problems: []
missing: []
members: [图片生成/文生图/动漫制造机_2055631147148824577.json, 图片生成/文生图/动漫制造机_2055683424748351489.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_485

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/动漫制造机_2055631147148824577.json、图片生成/文生图/动漫制造机_2055683424748351489.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `FluxResolutionNode`
- `KSamplerAdvanced`
- `ModelSamplingAuraFlow`
- `PrimitiveFloat`
- `PrimitiveInt`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncodeTiled`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 20 | - | 2 | 100% |
| 采样算法 | 8 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | kl_optimal | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 kl_optimal，2 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
