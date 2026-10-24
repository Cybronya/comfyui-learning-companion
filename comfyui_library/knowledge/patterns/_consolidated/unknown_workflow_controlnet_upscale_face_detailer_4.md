---
name: unknown_workflow_controlnet_upscale_face_detailer_4
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8885
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, ControlNetApplySD3, ControlNetLoader, DetailDaemonSamplerNode, DualCLIPLoader, EmptySD3LatentImage, FaceDetailer, FluxGuidance, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, MultiplySigmas, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, UltimateSDUpscale, UltralyticsDetectorProvider, Upscale Model Loader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/80年代动画风格角色_1920679986523471873.json, 图片生成/文生图/一键生成年代感动画风格角色_2067508971266732034.json, 图片生成/文生图/一键生成年代感动画风格角色_2069234470397497346.json, 图片生成/文生图/动画角色3视图（flux版）_1924796362821726210.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_face_detailer_4

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/80年代动画风格角色_1920679986523471873.json、图片生成/文生图/一键生成年代感动画风格角色_2067508971266732034.json、图片生成/文生图/一键生成年代感动画风格角色_2069234470397497346.json、图片生成/文生图/动画角色3视图（flux版）_1924796362821726210.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
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
- `SetUnionControlNetType` —— 3/4 个有
- `DF_Get_image_size` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.6 | 0.6 - 0.8 | 4 | 87% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.6，观测区间 0.6 - 0.8，4 个样本，取值集中（一致性 87%）
