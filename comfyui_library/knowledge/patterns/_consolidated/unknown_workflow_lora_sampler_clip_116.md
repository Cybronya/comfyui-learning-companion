---
name: unknown_workflow_lora_sampler_clip_116
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8272
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/最强最新Qwen image2512文生图工作流0707_2074521092005388289.json, 图片生成/文生图/最新qwen image2512文生图基础工作流_2013152895679602689.json, 图片生成/文生图/最新qwen+image2512文生图基础工作流_2094968730156621826.json, 图片生成/文生图/沙雕动漫修仙玄幻人物三视图（加速版）_1988478076659130370.json, 图片生成/文生图/沙雕动漫怪兽神兽多视图三视图（加速版）_2002568995201007617.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_116

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/最强最新Qwen image2512文生图工作流0707_2074521092005388289.json、图片生成/文生图/最新qwen image2512文生图基础工作流_2013152895679602689.json、图片生成/文生图/最新qwen+image2512文生图基础工作流_2094968730156621826.json、图片生成/文生图/沙雕动漫修仙玄幻人物三视图（加速版）_1988478076659130370.json、图片生成/文生图/沙雕动漫怪兽神兽多视图三视图（加速版）_2002568995201007617.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 3/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `QwenImageLatentAspectRatio` —— 3/5 个有
- `CR Text Concatenate` —— 2/5 个有
- `RMBG` —— 2/5 个有
- `SDXLEmptyLatentSizePicker+` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 4 - 15 | 5 | 49% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1344x768 (1.75) | - | 2 | 100% |
| 高度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 15，观测区间 4 - 15，5 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 最常用 1344x768 (1.75)，2 个样本，一致性 100%
- 高度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
