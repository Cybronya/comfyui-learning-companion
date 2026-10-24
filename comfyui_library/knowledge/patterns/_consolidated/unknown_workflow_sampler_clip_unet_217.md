---
name: unknown_workflow_sampler_clip_unet_217
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.796
common_nodes: [CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/自己用：小红书封面感海报_1993496492359041026.json, 图片生成/文生图/Qwen-image + LoRA 文生图工作流_2091479119539298306.json, 图片生成/文生图/Qwen-image 字体设计工作流_2091481144717041665.json, 图片生成/文生图/Qwen-小红书风格潮流拼贴海报_1968001076735651842.json, 图片生成/文生图/文生图-产品创意海报_2059206447187193858.json, 图片生成/文生图/文生图丨美食解构海报_2052972195072225281.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_217

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/自己用：小红书封面感海报_1993496492359041026.json、图片生成/文生图/Qwen-image + LoRA 文生图工作流_2091479119539298306.json、图片生成/文生图/Qwen-image 字体设计工作流_2091481144717041665.json、图片生成/文生图/Qwen-小红书风格潮流拼贴海报_1968001076735651842.json、图片生成/文生图/文生图-产品创意海报_2059206447187193858.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `JjkText` —— 4/6 个有
- `LoadImage` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `TextCombinerTwo` —— 3/6 个有
- `Anything Everywhere` —— 1/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `EmptySD3LatentImage` —— 1/6 个有
- `RH_Captioner` —— 1/6 个有
- `RH_LLMAPI_NODE` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20.5 | 8 - 30 | 6 | 65% |
| Prompt 约束强度(CFG) | 4.05 | 1 - 5.5 | 6 | 63% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20.5，观测区间 8 - 30，6 个样本
- Prompt 约束强度(CFG) 中位数 4.05，观测区间 1 - 5.5，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
