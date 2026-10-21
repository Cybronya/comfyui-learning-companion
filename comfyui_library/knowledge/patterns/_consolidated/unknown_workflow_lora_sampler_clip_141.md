---
name: unknown_workflow_lora_sampler_clip_141
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9285
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, KSamplerAdvanced, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [CR Text]
members: [图片生成/图生图/2070875464536776706.json, 图片生成/文生图/超自然人像生成：qwen-image-2512加Z-image双采样器文生图_2022543014375198722.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_141

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2070875464536776706.json、图片生成/文生图/超自然人像生成：qwen-image-2512加Z-image双采样器文生图_2022543014375198722.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `Int` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 50% |
| Prompt 约束强度(CFG) | 9 | - | 2 | 89% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler_ancestral | - | 2 | 50% |
| 重绘幅度 | sgm_uniform | - | 2 | 50% |
| 宽度 | 1280 | - | 1 | 100% |
| 高度 | 720 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，2 个样本，一致性 50%
- 重绘幅度 最常用 sgm_uniform，2 个样本，一致性 50%
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
