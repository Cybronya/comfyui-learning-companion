---
name: unknown_workflow_sampler_clip_unet_401
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.877667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext产品精修Plus x Redux_1975527009570959362.json, 图片生成/图生图/Kontext产品精修_1975519464328400898.json, 平台全量/Kontext一键清除工作流_1964679055893217281.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_401

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Kontext产品精修Plus x Redux_1975527009570959362.json、图片生成/图生图/Kontext产品精修_1975519464328400898.json、平台全量/Kontext一键清除工作流_1964679055893217281.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
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
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AV_LoraLoader` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `CLIPVisionEncode` —— 1/3 个有
- `CLIPVisionLoader` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `INPAINT_MaskedFill` —— 1/3 个有
- `Mask Fill Holes` —— 1/3 个有
- `RMBG` —— 1/3 个有
- `StyleModelApply` —— 1/3 个有
- `StyleModelLoader` —— 1/3 个有

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
