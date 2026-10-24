---
name: unknown_workflow_controlnet_sampler_clip_12
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.85275
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, ConditioningZeroOut, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LoadImage, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UnetLoaderGGUF, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【遇见AI】FLUX模型InstantX版Controlnet-Union_2041084960131518465.json, 图片生成/图生图/【遇见AI】FLUX模型JasperAI版Controlnet-Upscaler_2041086763887759361.json, 图片生成/图生图/【遇见AI】FLUX模型Shakker版Controlnet-Union-Pro_2041084048944140290.json, 图片生成/图生图/【遇见AI】FLUX模型alimama版Controlnet-Inpainting_2041074588796325889.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_12

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/【遇见AI】FLUX模型InstantX版Controlnet-Union_2041084960131518465.json、图片生成/图生图/【遇见AI】FLUX模型JasperAI版Controlnet-Upscaler_2041086763887759361.json、图片生成/图生图/【遇见AI】FLUX模型Shakker版Controlnet-Union-Pro_2041084048944140290.json、图片生成/图生图/【遇见AI】FLUX模型alimama版Controlnet-Inpainting_2041074588796325889.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ControlNetApplySD3` —— 3/4 个有
- `SetUnionControlNetType` —— 2/4 个有
- `CannyEdgePreprocessor` —— 1/4 个有
- `ControlNetInpaintingAliMamaApply` —— 1/4 个有
- `OpenposePreprocessor` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1536 | 4 | 81% |
| ControlNet 权重 | 1 | 0.8 - 1 | 3 | 90% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1536，4 个样本，取值集中（一致性 81%）
- ControlNet 权重 中位数 1，观测区间 0.8 - 1，3 个样本，取值集中（一致性 90%）
