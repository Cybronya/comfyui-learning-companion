---
name: unknown_workflow_lora_sampler_unet_135
type: Unknown Workflow
frequency: 5
level: strong
coverage: 1
common_nodes: [CFGNorm, CLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FireRed 局部重绘改图_2083841089588523009.json, 图片生成/图生图/FireRedImageedit1.1小红书局部重绘改图_2053381577794699265.json, 图片生成/图生图/FireRedImageedit1.1小红书局部重绘改图_2056041789731164161.json, 图片生成/图生图/千问图像编辑2511 双图编辑一致性_2013173412998418434.json, 图片生成/图生图/小红书开源模型FireRed-Image-edit1.1局部重绘改图p图改字_2029809441138286593.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_135

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/FireRed 局部重绘改图_2083841089588523009.json、图片生成/图生图/FireRedImageedit1.1小红书局部重绘改图_2053381577794699265.json、图片生成/图生图/FireRedImageedit1.1小红书局部重绘改图_2056041789731164161.json、图片生成/图生图/千问图像编辑2511 双图编辑一致性_2013173412998418434.json、图片生成/图生图/小红书开源模型FireRed-Image-edit1.1局部重绘改图p图改字_2029809441138286593.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 4/5 个有
- `ConditioningZeroOut` —— 4/5 个有
- `InpaintModelConditioning` —— 4/5 个有
- `Int` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `MaskFillHoles` —— 3/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/5 个有
- `TextInput_` —— 1/5 个有
- `easy int` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
