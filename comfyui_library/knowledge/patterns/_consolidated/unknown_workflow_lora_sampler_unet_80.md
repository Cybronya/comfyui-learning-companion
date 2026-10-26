---
name: unknown_workflow_lora_sampler_unet_80
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.825778
common_nodes: [CLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/纸雕qwen编辑_2006298270800285697.json, 图片生成/图生图/雪1.tonnie-edit 2509-提示词换装_2002550729497821185.json, 图片生成/图生图/雪10.tonnie-edit 2509-创建人物手办_2002809078772559873.json, 图片生成/图生图/雪2.tonnie-edit 2509-毛坯房装修_2002555895177441282.json, 图片生成/图生图/雪3.tonnie-edit 2509-参考图换装_2002559549150228481.json, 图片生成/图生图/雪4.tonnie-edit 2509-aux改变姿态_2002562915486035970.json, 图片生成/图生图/雪5.tonnie-edit 2509-翻新老旧照片_2002793142682304513.json, 图片生成/图生图/雪6.tonnie-edit 2509-去除马赛克_2002794745388777473.json, 图片生成/图生图/雪7.tonnie-edit 2509-提取服装_2002798214925414402.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_80

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/纸雕qwen编辑_2006298270800285697.json、图片生成/图生图/雪1.tonnie-edit 2509-提示词换装_2002550729497821185.json、图片生成/图生图/雪10.tonnie-edit 2509-创建人物手办_2002809078772559873.json、图片生成/图生图/雪2.tonnie-edit 2509-毛坯房装修_2002555895177441282.json、图片生成/图生图/雪3.tonnie-edit 2509-参考图换装_2002559549150228481.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 8/9 个有
- `ConditioningZeroOut` —— 7/9 个有
- `EmptyLatentImage` —— 7/9 个有
- `Image Comparer (rgthree)` —— 4/9 个有
- `AIO_Preprocessor` —— 1/9 个有
- `CLIPTextEncode` —— 1/9 个有
- `EmptySD3LatentImage` —— 1/9 个有
- `Image Levels Adjustment` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `RMBG` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 9 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 768 | 768 - 768 | 7 | 100% |
| 高度 | 1280 | 1280 - 1280 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，9 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 768 - 768，7 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 1280 - 1280，7 个样本，取值集中（一致性 100%）
- 高发问题（5/9 个样本）：Steps较低可能导致细节不足
