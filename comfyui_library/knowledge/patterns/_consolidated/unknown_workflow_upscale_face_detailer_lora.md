---
name: unknown_workflow_upscale_face_detailer_lora
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.740667
common_nodes: [BasicGuider, BasicScheduler, CFGZeroStarAndInit, CLIPTextEncode, CR Text, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FaceDetailer, FluxGuidance, GetNode, ImpactInt, KSamplerSelect, ModelSamplingFlux, PatchModelPatcherOrder, Power Lora Loader (rgthree), RH_LLMAPI_NODE, RandomNoise, SAMLoader, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SetNode, UNETLoader, UltimateSDUpscale, UltralyticsDetectorProvider, Upscale Model Loader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: [CR Text, Power Lora Loader (rgthree), Seed (rgthree), Upscale Model Loader]
members: [图片生成/文生图/1944235914703015938.json, 图片生成/文生图/1944334469094625282.json, 视频生成/图生视频/1944334469094625282.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_face_detailer_lora

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1944235914703015938.json、图片生成/文生图/1944334469094625282.json、视频生成/图生视频/1944334469094625282.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CFGZeroStarAndInit`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FaceDetailer`
- `FluxGuidance`
- `GetNode`
- `ImpactInt`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `PatchModelPatcherOrder`
- `Power Lora Loader (rgthree)`
- `RH_LLMAPI_NODE`
- `RandomNoise`
- `SAMLoader`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `UNETLoader`
- `UltimateSDUpscale`
- `UltralyticsDetectorProvider`
- `Upscale Model Loader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、Power Lora Loader (rgthree)、Seed (rgthree)、Upscale Model Loader
