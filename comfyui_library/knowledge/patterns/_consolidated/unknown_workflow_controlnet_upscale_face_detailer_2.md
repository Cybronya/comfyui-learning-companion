---
name: unknown_workflow_controlnet_upscale_face_detailer_2
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8685
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, ControlNetApplySD3, ControlNetLoader, DetailDaemonSamplerNode, DualCLIPLoader, EmptySD3LatentImage, FaceDetailer, FluxGuidance, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, MultiplySigmas, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, UltimateSDUpscale, UltralyticsDetectorProvider, Upscale Model Loader, VAEDecode, VAELoader]
problems: []
missing: [Upscale Model Loader]
members: [图片生成/文生图/1920679986523471873.json, 图片生成/文生图/1924796362821726210.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_face_detailer_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1920679986523471873.json、图片生成/文生图/1924796362821726210.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DetailDaemonSamplerNode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FaceDetailer`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `MultiplySigmas`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `UltimateSDUpscale`
- `UltralyticsDetectorProvider`
- `Upscale Model Loader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DF_Get_image_size` —— 1/2 个有
- `SetUnionControlNetType` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | - | 2 | 86% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 这些节点还没有知识卡，系统对它们的理解有限：Upscale Model Loader
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
