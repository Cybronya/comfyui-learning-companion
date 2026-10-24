---
name: text_to_image_controlnet_upscale_latent_upscale_6
type: Text To Image
frequency: 2
level: weak
coverage: 0.889
common_nodes: [ApplyPulidFlux, CLIPTextEncode, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, FaceAnalysisModels, FaceBoundingBox, FluxGuidance, GrowMaskWithBlur, Joy_caption_two, Joy_caption_two_load, KSampler, LatentUpscaleBy, LayerMask: PersonMaskUltra V2, LoadImage, LoraLoaderModelOnly, OpenposePreprocessor, PreviewImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, SaveImage, SetUnionControlNetType, ShowText|pysssss, Text Concatenate (JPS), TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, preview_mask]
problems: []
missing: []
members: [图片生成/图生图/风格转绘（hed+op）_1924254008326672385.json, 图片生成/文生图/风格转绘-F.1_1894391214139965442.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_latent_upscale_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/风格转绘（hed+op）_1924254008326672385.json、图片生成/文生图/风格转绘-F.1_1894391214139965442.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyPulidFlux`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `LatentUpscaleBy`
- `LayerMask: PersonMaskUltra V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `OpenposePreprocessor`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `SaveImage`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `Text Concatenate (JPS)`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `preview_mask`

**可变部分**（部分 workflow 才有）：
- `HEDPreprocessor` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| ControlNet 权重 | 0.525 | - | 2 | 57% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.8 | - | 2 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.525，样本不足，未给区间，2 个样本
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.8，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
