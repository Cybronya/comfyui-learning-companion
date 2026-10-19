---
name: unknown_workflow_lora_sampler_clip_95
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9285
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [CR Text]
members: [图片生成/图生图/2070875464536776706.json, 视频生成/图生视频/2034914535194238977.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_95

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2070875464536776706.json、视频生成/图生视频/2034914535194238977.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `Int` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `TextEncodeQwenImageEditPlus` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 6.5 | - | 2 | 77% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler_ancestral | - | 2 | 50% |
| 重绘幅度 | sgm_uniform | - | 2 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6.5，样本不足，未给区间，2 个样本
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，2 个样本，一致性 50%
- 重绘幅度 最常用 sgm_uniform，2 个样本，一致性 50%
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
