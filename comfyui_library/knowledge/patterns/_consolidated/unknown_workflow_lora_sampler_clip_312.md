---
name: unknown_workflow_lora_sampler_clip_312
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.812
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, FluxGuidance, KSamplerSelect, LoadImage, LoraLoader, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/万物Labubu_pd_1933410445787340801.json, 平台全量/Flux Redux - Best Style Transfer Tool_1863412991952662529.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_312

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/万物Labubu_pd_1933410445787340801.json、平台全量/Flux Redux - Best Style Transfer Tool_1863412991952662529.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ApplyFBCacheOnModel` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `ImageSmartSharpen+` —— 1/2 个有
- `JWImageResizeByLongerSide` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `PD_GetImageSize` —— 1/2 个有
- `TextInput_` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 856 | - | 1 | 100% |
| 高度 | 1152 | - | 1 | 100% |
| LoRA 模型强度 | 0.975 | - | 2 | 77% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.975，样本不足，未给区间，2 个样本
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
