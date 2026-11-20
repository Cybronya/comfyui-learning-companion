---
name: unknown_workflow_lora_sampler_unet_273
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7895
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, Fast Groups Muter (rgthree), ImageLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ModelSamplingAuraFlow, PrimitiveStringMultiline, ProcessString, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy int, easy promptLine, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image-edit-2511_AI动漫分镜图_2015701960917258241.json, 图片生成/图生图/Qwen-image-edit-2511_多角度生成_2016054100756013058.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_273

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen-image-edit-2511_AI动漫分镜图_2015701960917258241.json、图片生成/图生图/Qwen-image-edit-2511_多角度生成_2016054100756013058.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `Fast Groups Muter (rgthree)`
- `ImageLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PrimitiveStringMultiline`
- `ProcessString`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy int`
- `easy promptLine`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `CR Text Replace` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `MultiplePathsInput` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
