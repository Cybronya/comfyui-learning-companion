---
name: unknown_workflow_lora_sampler_clip_324
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8895
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, KSamplerSelect, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/矢量风格插画Flux+矢量Lora生图_1932014239752323074.json, 图片生成/文生图/简易贴纸制作工作流_1913052188661481473.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_324

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/矢量风格插画Flux+矢量Lora生图_1932014239752323074.json、图片生成/文生图/简易贴纸制作工作流_1913052188661481473.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `KSamplerSelect`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BlurFusionForegroundEstimation` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `GetMaskByBiRefNet` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LoadRembgByBiRefNetModel` —— 1/2 个有
- `RembgByBiRefNet` —— 1/2 个有
- `StringFunction|pysssss` —— 1/2 个有
- `TextCombinerTwo` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.95 | - | 2 | 95% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.95，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
