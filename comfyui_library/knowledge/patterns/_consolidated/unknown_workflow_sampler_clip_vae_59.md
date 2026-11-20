---
name: unknown_workflow_sampler_clip_vae_59
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.80625
common_nodes: [Bjornulf_ShowInt, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, NunchakuFluxDiTLoader, PreviewImage, RHBatchImages:, RHExtractImage, RHUploadZip, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader, easy forLoopEnd, easy forLoopStart, easy imageCount, easy joinImageBatch, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/批量清除文字，批量去水印-ai去水印_2031646955297837057.json, 图片生成/文生图/for循环 批量去除产品 工作流_1963301439051378689.json, 平台全量/批处理—去文字-去水印_1973693372038819842.json, 平台全量/批量处理-kontext-擦除海报文字-去水印_1957698955691880450.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_59

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/批量清除文字，批量去水印-ai去水印_2031646955297837057.json、图片生成/文生图/for循环 批量去除产品 工作流_1963301439051378689.json、平台全量/批处理—去文字-去水印_1973693372038819842.json、平台全量/批量处理-kontext-擦除海报文字-去水印_1957698955691880450.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `Bjornulf_ShowInt`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
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
- `CR Text Concatenate` —— 3/4 个有
- `FluxKontextImageScale` —— 3/4 个有
- `ImageConcanate` —— 3/4 个有
- `ImpactSwitch` —— 3/4 个有
- `NunchakuFluxLoraLoader` —— 3/4 个有
- `RH_Translator` —— 3/4 个有
- `RepeatLatentBatch` —— 3/4 个有
- `TextInput_` —— 3/4 个有
- `AddLabel` —— 2/4 个有
- `LoraLoader` —— 2/4 个有
- `UNETLoader` —— 2/4 个有
- `ImageStitch` —— 1/4 个有
- `LoadImageOutput` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 8 | 8 - 20 | 4 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
