---
name: unknown_workflow_lora_sampler_unet_70
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.7653
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图生图丨美食解构海报_2054801927573123073.json, 图片生成/图生图/换装+换衣+电商+FireRed-Image-Edit+多件服饰批量叠穿_2092526645906329601.json, 图片生成/图生图/模特套图工作流_1979044192452251649.json, 图片生成/图生图/模特套图工作流_1995150910940753922.json, 图片生成/图生图/电商产品图片加文字做电商主图 FireRed_2027939825982115841.json, 图片生成/图生图/电商产品贴图 FireRed 1.1_2039972727704002561.json, 图片生成/图生图/电商假人模特转真人+FireRed+1.1_2045761264483307521.json, 图片生成/图生图/直播宠物写真 FireRed 1.1_2060324746780307457.json, 图片生成/图生图/直播生成证件照 保持人物一致性+FireRed+1.1_2051579794864783362.json, 图片生成/文生图/Qwen_手写字体生成_2054073147015614466.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_70

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/图生图丨美食解构海报_2054801927573123073.json、图片生成/图生图/换装+换衣+电商+FireRed-Image-Edit+多件服饰批量叠穿_2092526645906329601.json、图片生成/图生图/模特套图工作流_1979044192452251649.json、图片生成/图生图/模特套图工作流_1995150910940753922.json、图片生成/图生图/电商产品图片加文字做电商主图 FireRed_2027939825982115841.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 8/10 个有
- `Image Comparer (rgthree)` —— 7/10 个有
- `RH_LLMAPI_NODE` —— 2/10 个有
- `easy promptList` —— 2/10 个有
- `easy showAnything` —— 2/10 个有
- `seed _O` —— 2/10 个有
- `MultiTextConcatenate` —— 1/10 个有
- `PreviewAny` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `Text _O` —— 1/10 个有
- `TextCombinerTwo` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 10 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 80% |
| 调度器 | beta | - | 10 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 80%
- 调度器 最常用 beta，10 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（15/10 个样本）：Steps较低可能导致细节不足
