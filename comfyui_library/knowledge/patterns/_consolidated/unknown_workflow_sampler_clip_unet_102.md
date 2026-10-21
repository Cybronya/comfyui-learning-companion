---
name: unknown_workflow_sampler_clip_unet_102
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.882714
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图，ZImage，强 DOPSD_1993892831561449474.json, 图片生成/文生图/文生图，ZImage，强 DOPSD，自用封面_2068318813740953602.json, 图片生成/文生图/更快 更强 支持中文 Z turbo_1993984068826103810.json, 图片生成/文生图/最强最新Qwen image2512文生图工作流0707_2074521092005388289.json, 图片生成/文生图/最新qwen image2512文生图基础工作流_2013152895679602689.json, 图片生成/文生图/最新qwen+image2512文生图基础工作流_2094968730156621826.json, 图片生成/文生图/真人感文生图_1996075408321888258.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_102

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/文生图，ZImage，强 DOPSD_1993892831561449474.json、图片生成/文生图/文生图，ZImage，强 DOPSD，自用封面_2068318813740953602.json、图片生成/文生图/更快 更强 支持中文 Z turbo_1993984068826103810.json、图片生成/文生图/最强最新Qwen image2512文生图工作流0707_2074521092005388289.json、图片生成/文生图/最新qwen image2512文生图基础工作流_2013152895679602689.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenImageLatentAspectRatio` —— 6/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `CFGNorm` —— 3/7 个有
- `ModelSamplingAuraFlow` —— 3/7 个有
- `MuyeTextEditOutput` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `Text Multiline` —— 3/7 个有
- `EmptySD3LatentImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 9 - 15 | 7 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 9 - 15，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
