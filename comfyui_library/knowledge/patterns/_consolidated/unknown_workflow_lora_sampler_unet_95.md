---
name: unknown_workflow_lora_sampler_unet_95
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.810375
common_nodes: [CLIPLoader, CR Text, ConditioningZeroOut, EmptyLatentImage, FluxKontextImageScale, ImpactSwitch, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader, easy imageConcat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/WH-AI-Studio电商换脸工作流(一致性完美版)_2017977236460150785.json, 图片生成/图生图/千问Edit2511单图编辑版_2004219532371783682.json, 图片生成/图生图/千问Edit2511多图编辑版_2004223606701916162.json, 图片生成/图生图/千问Edit2511多图编辑版_api_2031567329150115842.json, 图片生成/图生图/单图编辑+一致性超强（Qwen Edit2511）_2003851550328012802.json, 图片生成/图生图/多图编辑+一致性超强（Qwen Edit2511）_2003829045265637377.json, 图片生成/图生图/🪐千问新王炸！Edit2511来了！更好的一致性！单图编辑版_2003643255369703426.json, 图片生成/图生图/🪐千问新王炸！Edit2511来了！更好的一致性！多图编辑版_2003653367052288001.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_95

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/WH-AI-Studio电商换脸工作流(一致性完美版)_2017977236460150785.json、图片生成/图生图/千问Edit2511单图编辑版_2004219532371783682.json、图片生成/图生图/千问Edit2511多图编辑版_2004223606701916162.json、图片生成/图生图/千问Edit2511多图编辑版_api_2031567329150115842.json、图片生成/图生图/单图编辑+一致性超强（Qwen Edit2511）_2003851550328012802.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `FluxKontextImageScale`
- `ImpactSwitch`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageConcat`

**可变部分**（部分 workflow 才有）：
- `FluxResolutionNode` —— 7/8 个有
- `RH_LLMAPI_NODE` —— 5/8 个有
- `easy showAnything` —— 5/8 个有
- `Int` —— 2/8 个有
- `Note Plus (mtb)` —— 2/8 个有
- `PlaySound|pysssss` —— 2/8 个有
- `Crop Face` —— 1/8 个有
- `GetImage` —— 1/8 个有
- `LayerMask: PersonMaskUltra V2` —— 1/8 个有
- `Load RetinaFace` —— 1/8 个有
- `MaskColorize` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1080 | 8 | 68% |
| 高度 | 512 | 512 - 1920 | 8 | 32% |
| 采样步数 | 8 | 8 - 8 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 8 | 71% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1080，8 个样本
- 高度 中位数 512，观测区间 512 - 1920，8 个样本，取值分散，一致性仅 32%
- 采样步数 中位数 8，观测区间 8 - 8，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
