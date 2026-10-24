---
name: unknown_workflow_lora_sampler_clip_292
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.862
common_nodes: [CFGZeroStarAndInit, CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, EmptyHunyuanLatentVideo, ImpactInt, KSampler, LoraLoader, RHHiddenNodes, RH_LLMAPI_NODE, SaveImage, ShowText|pysssss, Text Find and Replace, Text Load Line From File, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy forLoopEnd, easy forLoopStart, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/wan通义万相最强批量文生图写实工作流（直出2K且提示词优化）_1949336324483031041.json, 图片生成/文生图/wan通义万相最强批量文生图写实工作流（直出2K且提示词优化）_1949349633655545857.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_292

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/wan通义万相最强批量文生图写实工作流（直出2K且提示词优化）_1949336324483031041.json、图片生成/文生图/wan通义万相最强批量文生图写实工作流（直出2K且提示词优化）_1949349633655545857.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGZeroStarAndInit`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `EmptyHunyuanLatentVideo`
- `ImpactInt`
- `KSampler`
- `LoraLoader`
- `RHHiddenNodes`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `ShowText|pysssss`
- `Text Find and Replace`
- `Text Load Line From File`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_2s | - | 2 | 100% |
| 调度器 | bong_tangent | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0.7 | - | 2 | 57% |
| LoRA 文本强度 | 0.7 | - | 2 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，2 个样本，一致性 100%
- 调度器 最常用 bong_tangent，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.7，样本不足，未给区间，2 个样本
- LoRA 文本强度 中位数 0.7，样本不足，未给区间，2 个样本
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
