---
name: unknown_workflow_sampler_clip_vae_71
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.805
common_nodes: [Bjornulf_ShowInt, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, ImageConcanate, KSampler, NunchakuFluxDiTLoader, PreviewImage, RHBatchImages:, RHExtractImage, RHUploadZip, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader, easy forLoopEnd, easy forLoopStart, easy imageCount, easy joinImageBatch, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/批量清除文字，批量去水印-ai去水印_2031646955297837057.json, 图片生成/文生图/for循环 批量去除产品 工作流_1963301439051378689.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_71

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/批量清除文字，批量去水印-ai去水印_2031646955297837057.json、图片生成/文生图/for循环 批量去除产品 工作流_1963301439051378689.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `Bjornulf_ShowInt`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageConcanate`
- `KSampler`
- `NunchakuFluxDiTLoader`
- `PreviewImage`
- `RHBatchImages:`
- `RHExtractImage`
- `RHUploadZip`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`
- `easy joinImageBatch`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `ImageStitch` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `LoadImageOutput` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `NunchakuFluxLoraLoader` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `RepeatLatentBatch` —— 1/2 个有
- `TextInput_` —— 1/2 个有
- `UNETLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 采样步数 | 14 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
