---
name: unknown_workflow_lora_sampler_clip_116
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.674
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, Text Multiline, UnetLoaderGGUF, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: PurgeVRAM V2, Text Concatenate, Text Multiline, CR SDXL Aspect Ratio]
members: [图片生成/文生图/1954712420105252865.json, 图片生成/文生图/1954718876200267778.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_116

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1954712420105252865.json、图片生成/文生图/1954718876200267778.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Text Multiline`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CFGZeroStar` —— 1/2 个有
- `CR SDXL Aspect Ratio` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `SeedVR2` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 89% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM V2、Text Concatenate、Text Multiline、CR SDXL Aspect Ratio
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
