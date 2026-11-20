---
name: unknown_workflow_inpaint_lora_sampler_48
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.899
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DeepTranslatorTextNode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImagePadForOutpaint, InpaintModelConditioning, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/ACE++合二为一_1893210305856745473.json, 图片生成/图生图/OneReward扩图工作流_1988900867971624962.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_48

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/ACE++合二为一_1893210305856745473.json、图片生成/图生图/OneReward扩图工作流_1988900867971624962.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DeepTranslatorTextNode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImagePadForOutpaint`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `ColorCorrect` —— 1/2 个有
- `Cut By Mask` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `ReduxAdvanced` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `StyleModelLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 29 | - | 2 | 28% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 29，样本不足，未给区间，2 个样本，取值分散，一致性仅 28%
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
