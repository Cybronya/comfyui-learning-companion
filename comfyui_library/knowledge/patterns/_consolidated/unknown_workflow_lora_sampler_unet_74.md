---
name: unknown_workflow_lora_sampler_unet_74
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.975
common_nodes: [CFGNorm, CLIPLoader, CR Prompt Text, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FireRed 局部重绘改图_2083841089588523009.json, 图片生成/图生图/FireRedImageedit1.1小红书局部重绘改图_2053381577794699265.json, 图片生成/图生图/FireRedImageedit1.1小红书局部重绘改图_2056041789731164161.json, 图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑_2033156894868639745.json, 图片生成/图生图/小红书人物换装 双图编辑_2034550287024791553.json, 图片生成/图生图/小红书人物换装+局部变大+双图编辑_2034677242252496898.json, 图片生成/图生图/小红书开源模型FireRed-Image-edit1.1局部重绘改图p图改字_2029809441138286593.json, 图片生成/图生图/超好用🔥人物一键换装-双图编辑_2063984968640061441.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_74

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/FireRed 局部重绘改图_2083841089588523009.json、图片生成/图生图/FireRedImageedit1.1小红书局部重绘改图_2053381577794699265.json、图片生成/图生图/FireRedImageedit1.1小红书局部重绘改图_2056041789731164161.json、图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑_2033156894868639745.json、图片生成/图生图/小红书人物换装 双图编辑_2034550287024791553.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Prompt Text`
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
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/8 个有
- `EmptyLatentImage` —— 4/8 个有
- `Image Comparer (rgthree)` —— 4/8 个有
- `InpaintModelConditioning` —— 4/8 个有
- `Int` —— 3/8 个有
- `MaskFillHoles` —— 3/8 个有
- `easy int` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1536 | 1536 - 1536 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，4 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
