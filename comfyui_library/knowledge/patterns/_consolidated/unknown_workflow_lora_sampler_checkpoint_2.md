---
name: unknown_workflow_lora_sampler_checkpoint_2
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.846556
common_nodes: [CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus_lrzjason, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 人物证件照无水印版_2019647692418322433.json, 图片生成/图生图/Qwen-Rapid-AIO电商产品溶图矫正角度，重新纠正光源_2054467334085062657.json, 图片生成/图生图/Qwen-Rapid-AIO电商产品溶图矫正角度，重新纠正光源_2057720344152207361.json, 图片生成/图生图/一键证件照自动美颜+换发型_服装万能证件照_2079884897178705922.json, 图片生成/图生图/一键证件照自动美颜+换发型_服装万能证件照_2080470101836517377.json, 图片生成/图生图/全能电商产品溶图自动矫正角度，重新纠正光源_2041830014605336577.json, 图片生成/图生图/电商产品溶图 图生图_2034458183934152705.json, 图片生成/图生图/电商产品溶图，自动矫正角度，重新纠正光源_2101208468156936194.json, 图片生成/图生图/电商产品溶图，自动矫正角度，重新纠正光源_2102202784425799681.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_checkpoint_2

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen 人物证件照无水印版_2019647692418322433.json、图片生成/图生图/Qwen-Rapid-AIO电商产品溶图矫正角度，重新纠正光源_2054467334085062657.json、图片生成/图生图/Qwen-Rapid-AIO电商产品溶图矫正角度，重新纠正光源_2057720344152207361.json、图片生成/图生图/一键证件照自动美颜+换发型_服装万能证件照_2079884897178705922.json、图片生成/图生图/一键证件照自动美颜+换发型_服装万能证件照_2080470101836517377.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 9 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 6/9 个有
- `Image Comparer (rgthree)` —— 6/9 个有
- `Int` —— 6/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/9 个有
- `easy cleanGpuUsed` —— 6/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 5 | 9 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 67% |
| 调度器 | normal | - | 9 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1024 | 1016 - 1024 | 9 | 100% |
| 高度 | 1440 | 1440 - 1536 | 9 | 97% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 5，9 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 67%
- 调度器 最常用 normal，9 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1016 - 1024，9 个样本，取值集中（一致性 100%）
- 高度 中位数 1440，观测区间 1440 - 1536，9 个样本，取值集中（一致性 97%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
