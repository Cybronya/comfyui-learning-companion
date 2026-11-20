---
name: unknown_workflow_lora_sampler_clip_255
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.843
common_nodes: [AV_LoraLoader, BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext产品精修Plus x Redux_1975527009570959362.json, 图片生成/图生图/Kontext产品精修_1975519464328400898.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_255

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Kontext产品精修Plus x Redux_1975527009570959362.json、图片生成/图生图/Kontext产品精修_1975519464328400898.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `AV_LoraLoader`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 1/2 个有
- `CLIPVisionLoader` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RMBG` —— 1/2 个有
- `StyleModelApply` —— 1/2 个有
- `StyleModelLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
