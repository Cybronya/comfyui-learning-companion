---
name: unknown_workflow_lora_sampler_unet_90
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.816111
common_nodes: [CLIPLoader, CR Text, ConditioningZeroOut, EmptyLatentImage, FluxKontextImageScale, ImpactSwitch, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader, easy imageConcat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/WH-AI-Studio电商换脸工作流(一致性完美版)_2017977236460150785.json, 图片生成/图生图/千问Edit2511单图编辑版_2004219532371783682.json, 图片生成/图生图/千问Edit2511多图编辑版_2004223606701916162.json, 图片生成/图生图/千问Edit2511多图编辑版_api_2031567329150115842.json, 图片生成/图生图/单图编辑+一致性超强（Qwen Edit2511）_2003851550328012802.json, 图片生成/图生图/多图编辑+一致性超强（Qwen Edit2511）_2003829045265637377.json, 图片生成/图生图/🪐千问新王炸！Edit2511来了！更好的一致性！单图编辑版_2003643255369703426.json, 图片生成/图生图/🪐千问新王炸！Edit2511来了！更好的一致性！多图编辑版_2003653367052288001.json, 平台全量/图片多模态编辑_2059395156285157378.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_90

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/WH-AI-Studio电商换脸工作流(一致性完美版)_2017977236460150785.json、图片生成/图生图/千问Edit2511单图编辑版_2004219532371783682.json、图片生成/图生图/千问Edit2511多图编辑版_2004223606701916162.json、图片生成/图生图/千问Edit2511多图编辑版_api_2031567329150115842.json、图片生成/图生图/单图编辑+一致性超强（Qwen Edit2511）_2003851550328012802.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 9 个 workflow 都包含：
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
- `FluxResolutionNode` —— 8/9 个有
- `RH_LLMAPI_NODE` —— 6/9 个有
- `easy showAnything` —— 6/9 个有
- `Int` —— 3/9 个有
- `PlaySound|pysssss` —— 3/9 个有
- `Note Plus (mtb)` —— 2/9 个有
- `Crop Face` —— 1/9 个有
- `GetImage` —— 1/9 个有
- `LayerMask: PersonMaskUltra V2` —— 1/9 个有
- `Load RetinaFace` —— 1/9 个有
- `MaskColorize` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1080 | 9 | 69% |
| 高度 | 512 | 512 - 1920 | 9 | 34% |
| 采样步数 | 8 | 8 - 8 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 9 | 72% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1080，9 个样本
- 高度 中位数 512，观测区间 512 - 1920，9 个样本，取值分散，一致性仅 34%
- 采样步数 中位数 8，观测区间 8 - 8，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
