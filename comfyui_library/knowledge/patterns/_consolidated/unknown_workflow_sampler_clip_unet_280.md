---
name: unknown_workflow_sampler_clip_unet_280
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9376
common_nodes: [CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-千问多字体直出-字体设计 中文字体设计_1993312885105426433.json, 图片生成/文生图/Qwen-小红书风格封面设计工作流_1979207949715410946.json, 图片生成/文生图/Z image生图_1997316490393227266.json, 图片生成/文生图/qwen-image 20步稳定生图_1954932098835496961.json, 图片生成/文生图/通义千问Qwen-image文生图：媲美即梦出图_1952728050552270850.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_280

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Qwen-千问多字体直出-字体设计 中文字体设计_1993312885105426433.json、图片生成/文生图/Qwen-小红书风格封面设计工作流_1979207949715410946.json、图片生成/文生图/Z image生图_1997316490393227266.json、图片生成/文生图/qwen-image 20步稳定生图_1954932098835496961.json、图片生成/文生图/通义千问Qwen-image文生图：媲美即梦出图_1952728050552270850.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `ModelSamplingAuraFlow` —— 4/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `EmptySD3LatentImage` —— 2/5 个有
- `LatentUpscaleBy` —— 1/5 个有
- `Lora Loader Stack (rgthree)` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `TextCombinerSix` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 9 - 30 | 5 | 66% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 4 | 5 | 64% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 9 - 30，5 个样本
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 4，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
