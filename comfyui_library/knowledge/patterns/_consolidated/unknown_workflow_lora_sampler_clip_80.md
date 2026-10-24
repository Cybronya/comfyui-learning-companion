---
name: unknown_workflow_lora_sampler_clip_80
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.931167
common_nodes: [CFGGuider, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/bg_2068900398752157698.json, 图片生成/图生图/flux2 klein 9B 4视图_2050825970894028801.json, 图片生成/图生图/klein_KV直出_2022222084566425602.json, 图片生成/图生图/换头换脸_真实自然-Flux2-Klein工作流_2017928641371443202.json, 图片生成/图生图/换头换脸_真实自然-Flux2-Klein工作流_2067849412315013121.json, 图片生成/图生图/赛博朋克画风_2029859105694814210.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_80

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/bg_2068900398752157698.json、图片生成/图生图/flux2 klein 9B 4视图_2050825970894028801.json、图片生成/图生图/klein_KV直出_2022222084566425602.json、图片生成/图生图/换头换脸_真实自然-Flux2-Klein工作流_2017928641371443202.json、图片生成/图生图/换头换脸_真实自然-Flux2-Klein工作流_2067849412315013121.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 5/6 个有
- `Image Comparer (rgthree)` —— 5/6 个有
- `CLIPLoader` —— 4/6 个有
- `ImageScaleToTotalPixels` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `UNETLoader` —— 4/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `SegmentV2` —— 3/6 个有
- `LoadDiffusionModelShared //Inspire` —— 2/6 个有
- `LoadTextEncoderShared //Inspire` —— 2/6 个有
- `easy imageColorMatch` —— 2/6 个有
- `GrowMaskWithBlur` —— 1/6 个有
- `InpaintModelConditioning` —— 1/6 个有
- `InvertMask` —— 1/6 个有
- `MaskPreview` —— 1/6 个有
- `MaskToImage` —— 1/6 个有
- `Text` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
