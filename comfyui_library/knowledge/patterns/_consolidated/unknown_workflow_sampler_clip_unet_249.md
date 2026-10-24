---
name: unknown_workflow_sampler_clip_unet_249
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.862
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, ConditioningZeroOut, DualCLIPLoader, KSamplerSelect, LoadImage, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【遇见AI】FLUX Tools Fill 扩图_2041024111018778626.json, 图片生成/图生图/【遇见AI】FLUX Tools Fill 重绘_2041021438299213825.json, 图片生成/图生图/【遇见AI】FLUX Tools canny&depth_2041013420962619394.json, 图片生成/文生图/Flux+ControlNet_UnionPro2_v2_1927179095069851650.json, 图片生成/文生图/Flux+ControlNet_Union文生图_1914137899061735426.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_249

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/【遇见AI】FLUX Tools Fill 扩图_2041024111018778626.json、图片生成/图生图/【遇见AI】FLUX Tools Fill 重绘_2041021438299213825.json、图片生成/图生图/【遇见AI】FLUX Tools canny&depth_2041013420962619394.json、图片生成/文生图/Flux+ControlNet_UnionPro2_v2_1927179095069851650.json、图片生成/文生图/Flux+ControlNet_Union文生图_1914137899061735426.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/5 个有
- `AIO_Preprocessor` —— 2/5 个有
- `ControlNetApplyAdvanced` —— 2/5 个有
- `ControlNetLoader` —— 2/5 个有
- `EmptySD3LatentImage` —— 2/5 个有
- `ImpactCombineConditionings` —— 2/5 个有
- `InpaintModelConditioning` —— 2/5 个有
- `AnyLinePreprocessor` —— 1/5 个有
- `CannyEdgePreprocessor` —— 1/5 个有
- `DWPreprocessor` —— 1/5 个有
- `ImagePadForOutpaint` —— 1/5 个有
- `InstructPixToPixConditioning` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `MiDaS-DepthMapPreprocessor` —— 1/5 个有
- `Text Multiline` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.75 | - | 2 | 93% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.75，样本不足，未给区间，2 个样本，取值集中（一致性 93%）
