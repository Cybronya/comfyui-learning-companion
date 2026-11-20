---
name: unknown_workflow_sampler_clip_unet_319
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8872
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/千问2512文生图海报、图片设计_2093310820385116161.json, 图片生成/文生图/唯一讲述着专用Z-image造像_2000531408500162562.json, 图片生成/文生图/最强最新Qwen image2512文生图工作流0707_2074521092005388289.json, 图片生成/文生图/最新qwen image2512文生图基础工作流_2013152895679602689.json, 图片生成/文生图/最新qwen+image2512文生图基础工作流_2094968730156621826.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_319

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/千问2512文生图海报、图片设计_2093310820385116161.json、图片生成/文生图/唯一讲述着专用Z-image造像_2000531408500162562.json、图片生成/文生图/最强最新Qwen image2512文生图工作流0707_2074521092005388289.json、图片生成/文生图/最新qwen image2512文生图基础工作流_2013152895679602689.json、图片生成/文生图/最新qwen+image2512文生图基础工作流_2094968730156621826.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `QwenImageLatentAspectRatio` —— 4/5 个有
- `Text Multiline` —— 4/5 个有
- `CFGNorm` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `LoraLoader` —— 2/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `VideoLinearCFGGuidance` —— 1/5 个有
- `easy promptConcat` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 8 - 15 | 5 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 5 | 0% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 15，观测区间 8 - 15，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，5 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
