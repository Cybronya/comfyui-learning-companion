---
name: unknown_workflow_sampler_clip_unet_547
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9375
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSamplerSelect, ModelSamplingFlux, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, String Literal, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/Flux with face detailer_1866026566013853698.json, 平台全量/Flux模型-时尚杂志摄影_1823178390001356802.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_547

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Flux with face detailer_1866026566013853698.json、平台全量/Flux模型-时尚杂志摄影_1823178390001356802.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `String Literal`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BilboXPhotoPrompt` —— 1/2 个有
- `CR Apply LoRA Stack` —— 1/2 个有
- `CR LoRA Stack` —— 1/2 个有
- `CR Text Input Switch` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `FaceDetailer` —— 1/2 个有
- `Int Literal` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `SAMLoader` —— 1/2 个有
- `UltralyticsDetectorProvider` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 864 | - | 2 | 96% |
| 高度 | 1248 | - | 2 | 97% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 864，样本不足，未给区间，2 个样本，取值集中（一致性 96%）
- 高度 中位数 1248，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
