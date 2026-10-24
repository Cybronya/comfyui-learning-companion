---
name: unknown_workflow_lora_sampler_checkpoint_16
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.854
common_nodes: [Anything Everywhere, CLIPLoader, CheckpointLoaderSimple, ConditioningZeroOut, Fast Groups Bypasser (rgthree), FluxKontextMultiReferenceLatentMethod, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, Qwen3_VQA, QwenMultiangleCameraNode, SaveImage, ShowText|pysssss, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy getNode, easy promptLine, easy promptList, easy setNode, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenEdit2511&AIO自动分镜_精准镜头控制_2010972494848598018.json, 图片生成/图生图/【推荐，一键出分镜】QwenEdit2511&AIO自动分镜_精准镜头控制_2011866253106880514.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_checkpoint_16

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/QwenEdit2511&AIO自动分镜_精准镜头控制_2010972494848598018.json、图片生成/图生图/【推荐，一键出分镜】QwenEdit2511&AIO自动分镜_精准镜头控制_2011866253106880514.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPLoader`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `Qwen3_VQA`
- `QwenMultiangleCameraNode`
- `SaveImage`
- `ShowText|pysssss`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy getNode`
- `easy promptLine`
- `easy promptList`
- `easy setNode`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta57 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta57，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
