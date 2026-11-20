---
name: unknown_workflow_lora_sampler_unet_150
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7718
common_nodes: [CFGNorm, CLIPLoader, CR Index, CR Text, ConditioningZeroOut, GetNode, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, QwenEditConfigPreparer, SaveImage, Seed (rgthree), SetNode, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy imageScaleDownToSize, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/28photoretouching_2049469543893962754.json, 图片生成/图生图/qwen-edit-图片精修-深度优化版4.0_2013194815093084162.json, 平台全量/Qwen-edit 人物模特皮肤质感 修图 服装电商产品精修 金属 电器 高清级照片精修_2029438717412253697.json, 平台全量/电商产品精修 Qwen-edit  内附不同产品提示词 深度优化版 照片精修深度优化版 更好的纹理效_2039885028955525122.json, 平台全量/电商产品质感精修 Qwen-edit  内附不同产品提示词 深度优化版 照片精修 更好的纹理效果_2039933888281186306.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_150

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/反推提示词/28photoretouching_2049469543893962754.json、图片生成/图生图/qwen-edit-图片精修-深度优化版4.0_2013194815093084162.json、平台全量/Qwen-edit 人物模特皮肤质感 修图 服装电商产品精修 金属 电器 高清级照片精修_2029438717412253697.json、平台全量/电商产品精修 Qwen-edit  内附不同产品提示词 深度优化版 照片精修深度优化版 更好的纹理效_2039885028955525122.json、平台全量/电商产品质感精修 Qwen-edit  内附不同产品提示词 深度优化版 照片精修 更好的纹理效果_2039933888281186306.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Index`
- `CR Text`
- `ConditioningZeroOut`
- `GetNode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `QwenEditConfigPreparer`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy imageScaleDownToSize`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/5 个有
- `LayerUtility: ImageReel` —— 4/5 个有
- `LayerUtility: ImageReelComposit` —— 4/5 个有
- `MuyeTextEditOutput` —— 4/5 个有
- `RTXVideoSuperResolution` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler_ancestral | - | 5 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，5 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
