---
name: unknown_workflow_lora_sampler_unet_147
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7984
common_nodes: [CFGNorm, CLIPLoader, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/观行子：人物一致性迁移 F2P 新模型_1983624110100160513.json, 图片生成/图生图/雪5.tonnie-edit 2509-翻新老旧照片_2002793142682304513.json, 图片生成/图生图/雪6.tonnie-edit 2509-去除马赛克_2002794745388777473.json, 图片生成/图生图/雪7.tonnie-edit 2509-提取服装_2002798214925414402.json, 图片生成/图生图/雪9.tonnie-edit 2509-变换镜头_2002806136589959169.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_147

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/观行子：人物一致性迁移 F2P 新模型_1983624110100160513.json、图片生成/图生图/雪5.tonnie-edit 2509-翻新老旧照片_2002793142682304513.json、图片生成/图生图/雪6.tonnie-edit 2509-去除马赛克_2002794745388777473.json、图片生成/图生图/雪7.tonnie-edit 2509-提取服装_2002798214925414402.json、图片生成/图生图/雪9.tonnie-edit 2509-变换镜头_2002806136589959169.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `ACE_ImageFaceCrop` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `Image Levels Adjustment` —— 1/5 个有
- `ImpactWildcardProcessor` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `PresetText|pysssss` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `TextInput_` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | beta | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 768 | 768 - 768 | 5 | 100% |
| 高度 | 1280 | 1024 - 1280 | 5 | 92% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 768 - 768，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 1024 - 1280，5 个样本，取值集中（一致性 92%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
