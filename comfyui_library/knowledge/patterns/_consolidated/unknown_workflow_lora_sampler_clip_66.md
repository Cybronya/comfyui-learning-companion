---
name: unknown_workflow_lora_sampler_clip_66
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.917714
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/剪纸风格-myshell_1967455683580923905.json, 图片生成/文生图/剪纸风格_1963167950662512641.json, 图片生成/文生图/动漫出图Qwen工作流_2019691912264945666.json, 图片生成/文生图/动漫出图Qwen工作流_2053018053553737730.json, 图片生成/文生图/千问工作流_2083184424287563777.json, 图片生成/文生图/千问文生图_1985931273690591234.json, 图片生成/文生图/千问文生图_1987591657719836673.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_66

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/剪纸风格-myshell_1967455683580923905.json、图片生成/文生图/剪纸风格_1963167950662512641.json、图片生成/文生图/动漫出图Qwen工作流_2019691912264945666.json、图片生成/文生图/动漫出图Qwen工作流_2053018053553737730.json、图片生成/文生图/千问工作流_2083184424287563777.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 2/7 个有
- `TextInput_` —— 2/7 个有
- `CR Simple Prompt List` —— 1/7 个有
- `GlobalSeed //Inspire` —— 1/7 个有
- `ShellAgentPluginInputText` —— 1/7 个有
- `ShellAgentPluginSaveImage` —— 1/7 个有
- `StringFunction|pysssss` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 40 | 7 | 22% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 7 | 53% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 40，7 个样本，取值分散，一致性仅 22%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（5/7 个样本）：Steps较低可能导致细节不足
