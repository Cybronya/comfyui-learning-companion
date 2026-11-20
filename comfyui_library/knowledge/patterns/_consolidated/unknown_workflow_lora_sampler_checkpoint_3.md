---
name: unknown_workflow_lora_sampler_checkpoint_3
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.915714
common_nodes: [CheckpointLoaderSimple, ConditioningZeroOut, FastCanvas, FastCanvasTool, Image Comparer (rgthree), ImageCropper, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus_lrzjason, VAEDecode, easy imageRemBg]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/002.Qwen编辑之王010.电商溶图_2034639419155685377.json, 图片生成/图生图/溶图合成_海报合成-Qwen-Rapid-AiO-SFW-v18 工作流_2010036547650854913.json, 图片生成/图生图/画布溶图_2010259832242184194.json, 平台全量/04.电商产品溶图，自动矫正角度，重新纠正光源_2000792985195474946.json, 平台全量/Qwen 2511 人物换脸，融图打光 电商产品溶图，自动纠正产品角度，矫正透视 重新纠正光源_2009804367066566658.json, 平台全量/电商产品溶图+人物换脸+重新纠正光源_2009630490193563650.json, 平台全量/电商产品溶图，自动矫正角度_2010630796796764161.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_checkpoint_3

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/002.Qwen编辑之王010.电商溶图_2034639419155685377.json、图片生成/图生图/溶图合成_海报合成-Qwen-Rapid-AiO-SFW-v18 工作流_2010036547650854913.json、图片生成/图生图/画布溶图_2010259832242184194.json、平台全量/04.电商产品溶图，自动矫正角度，重新纠正光源_2000792985195474946.json、平台全量/Qwen 2511 人物换脸，融图打光 电商产品溶图，自动纠正产品角度，矫正透视 重新纠正光源_2009804367066566658.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `FastCanvas`
- `FastCanvasTool`
- `Image Comparer (rgthree)`
- `ImageCropper`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `VAEDecode`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 2/7 个有
- `Anything Everywhere3` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | normal | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 normal，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
