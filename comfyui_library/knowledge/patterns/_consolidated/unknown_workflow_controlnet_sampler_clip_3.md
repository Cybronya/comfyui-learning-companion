---
name: unknown_workflow_controlnet_sampler_clip_3
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.762333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EmptySD3LatentImage, KSamplerSelect, LoadImage, ModelSamplingFlux, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [MiDaS-DepthMapPreprocessor, Text Multiline, GetImageSize+]
members: [图片生成/文生图/1914137899061735426.json, 图片生成/文生图/1927179095069851650.json, 图片生成/文生图/1935896243191410690.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_3

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1914137899061735426.json、图片生成/文生图/1927179095069851650.json、图片生成/文生图/1935896243191410690.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `ImpactCombineConditionings` —— 2/3 个有
- `AnyLinePreprocessor` —— 1/3 个有
- `ApplyFirstBlockCachePatch` —— 1/3 个有
- `CannyEdgePreprocessor` —— 1/3 个有
- `DWPreprocessor` —— 1/3 个有
- `GetImageSize+` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `MiDaS-DepthMapPreprocessor` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `SetUnionControlNetType` —— 1/3 个有
- `Text Multiline` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | 0.6 - 0.8 | 3 | 88% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.7，观测区间 0.6 - 0.8，3 个样本，取值集中（一致性 88%）
- 这些节点还没有知识卡，系统对它们的理解有限：MiDaS-DepthMapPreprocessor、Text Multiline、GetImageSize+
