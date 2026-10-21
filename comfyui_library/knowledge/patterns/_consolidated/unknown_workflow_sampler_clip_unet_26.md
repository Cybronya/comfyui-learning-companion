---
name: unknown_workflow_sampler_clip_unet_26
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.952571
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Int, KSamplerAdvanced, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Krea2双采美感超强_文生图_2071509119319756801.json, 图片生成/文生图/Krea2文生图（双模型双采美感强化）_2071588892037443585.json, 图片生成/文生图/Pornmaster_krea2_t2i_Raw+Turbo_2098728229115879426.json, 图片生成/文生图/Z-Image+Base&Turbo双重采样工作流_2058016487142674434.json, 图片生成/文生图/Z-Image-Turbo文生图双重采样_2018553894216929282.json, 图片生成/文生图/Z-Image-turb随机性出图多张_2037904618847473665.json, 图片生成/文生图/Z-Image-turb随机性出图多张_2072122771399864322.json, 图片生成/文生图/Z-Image-turb随机性出图多张_2072127037019611138.json, 图片生成/文生图/Z-Image-turb随机性出图多张_2072848197558554626.json, 图片生成/文生图/Z-Image-turb随机性出图多张_2077553813770293249.json, 图片生成/文生图/Z-Image-turb随机性出图多张_2077559193019699201.json, 图片生成/文生图/Z-Image-turb随机性出图多张_2081938785293651969.json, 图片生成/文生图/Z-image-Turbo文生图 双重采样_2020839379777884161.json, 图片生成/文生图/文生图 双采 行为艺术 黑兽9优化版_2065363132853612544.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_26

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Krea2双采美感超强_文生图_2071509119319756801.json、图片生成/文生图/Krea2文生图（双模型双采美感强化）_2071588892037443585.json、图片生成/文生图/Pornmaster_krea2_t2i_Raw+Turbo_2098728229115879426.json、图片生成/文生图/Z-Image+Base&Turbo双重采样工作流_2058016487142674434.json、图片生成/文生图/Z-Image-Turbo文生图双重采样_2018553894216929282.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Int`
- `KSamplerAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 12/14 个有
- `ConditioningZeroOut` —— 9/14 个有
- `LoraLoaderModelOnly` —— 9/14 个有
- `PrimitiveStringMultiline` —— 7/14 个有
- `ModelSamplingAuraFlow` —— 6/14 个有
- `Seed (rgthree)` —— 4/14 个有
- `CompressImages` —— 3/14 个有
- `CR Prompt Text` —— 2/14 个有
- `TTResolutionSelector` —— 2/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 14 | 100% |
| Prompt 约束强度(CFG) | 8 | 3 - 8 | 14 | 58% |
| 采样算法 | 1 | 1 - 1.5 | 14 | 88% |
| 调度器 | euler | - | 14 | 100% |
| 重绘幅度 | simple | - | 14 | 79% |
| 宽度 | 1308 | 832 - 1536 | 14 | 80% |
| 高度 | 1984 | 1216 - 2048 | 14 | 85% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，14 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 3 - 8，14 个样本
- 采样算法 中位数 1，观测区间 1 - 1.5，14 个样本，取值集中（一致性 88%）
- 调度器 最常用 euler，14 个样本，一致性 100%
- 重绘幅度 最常用 simple，14 个样本，一致性 79%
- 宽度 中位数 1308，观测区间 832 - 1536，14 个样本
- 高度 中位数 1984，观测区间 1216 - 2048，14 个样本，取值集中（一致性 85%）
