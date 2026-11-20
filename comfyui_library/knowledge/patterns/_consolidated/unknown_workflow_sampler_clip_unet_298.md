---
name: unknown_workflow_sampler_clip_unet_298
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.947
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyLatentImage, Int, KSamplerAdvanced, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Krea2-风格迁移_2075792357995405314.json, 图片生成/文生图/Krea2双采美感超强_文生图_2071509119319756801.json, 图片生成/文生图/Krea2文生图（双模型双采美感强化）_2071588892037443585.json, 图片生成/文生图/Zimage Base+turbo双采样工作流_2074842071952875522.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_298

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Krea2-风格迁移_2075792357995405314.json、图片生成/文生图/Krea2双采美感超强_文生图_2071509119319756801.json、图片生成/文生图/Krea2文生图（双模型双采美感强化）_2071588892037443585.json、图片生成/文生图/Zimage Base+turbo双采样工作流_2074842071952875522.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyLatentImage`
- `Int`
- `KSamplerAdvanced`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `TTResolutionSelector` —— 2/4 个有
- `llama_cpp_instruct_adv` —— 2/4 个有
- `llama_cpp_model_loader` —— 2/4 个有
- `llama_cpp_parameters` —— 2/4 个有
- `INTConstant` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `Text Multiline` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1080 | 4 | 98% |
| 高度 | 1536 | 1536 - 1920 | 4 | 90% |
| 采样步数 | randomize | - | 4 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 4 | 100% |
| 采样算法 | 1 | 1 - 2 | 4 | 65% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1080，4 个样本，取值集中（一致性 98%）
- 高度 中位数 1536，观测区间 1536 - 1920，4 个样本，取值集中（一致性 90%）
- 采样步数 最常用 randomize，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 2，4 个样本
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
