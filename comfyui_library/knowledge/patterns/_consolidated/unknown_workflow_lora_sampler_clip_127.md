---
name: unknown_workflow_lora_sampler_clip_127
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.946667
common_nodes: [AdvancedLyingSigmaSampler, BasicScheduler, CFGZeroStar, CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, JoinStringMulti, KSamplerSelect, LoraLoaderModelOnly, ModelSamplingAuraFlow, SamplerCustom, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-image-邵氏武侠风格工作流_2029716281011736578.json, 图片生成/文生图/Z-image-邵氏武侠风格工作流_2082008160352690178.json, 图片生成/文生图/Z-image邵氏风格工作流_2023426462694510593.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_127

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image-邵氏武侠风格工作流_2029716281011736578.json、图片生成/文生图/Z-image-邵氏武侠风格工作流_2082008160352690178.json、图片生成/文生图/Z-image邵氏风格工作流_2023426462694510593.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `AdvancedLyingSigmaSampler`
- `BasicScheduler`
- `CFGZeroStar`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `JoinStringMulti`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SamplerCustom`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `Switch any [Crystools]` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 928 | 928 - 1704 | 3 | 69% |
| 高度 | 1664 | 1280 - 1664 | 3 | 88% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 928，观测区间 928 - 1704，3 个样本
- 高度 中位数 1664，观测区间 1280 - 1664，3 个样本，取值集中（一致性 88%）
