---
name: unknown_workflow_sampler_clip_vae_21
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.897455
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX2-dev文生图_1993862047901433857.json, 图片生成/文生图/FLUX2-dev文生图工作流_1993549884353609730.json, 图片生成/文生图/FLUX2-多参考一致性创意场景合成_2090769208387923969.json, 图片生成/文生图/Flux.2 单图编辑 用嘴改图官方工作流_1998219021541629954.json, 图片生成/文生图/Flux.2+LoRA文生图_1995120190486667265.json, 图片生成/文生图/Flux.2双图编辑_1993607256262508545.json, 图片生成/文生图/Flux.2文生哪吒_1994791173480964097.json, 图片生成/文生图/Flux2 官方文_图生视频_1993512866739322882.json, 图片生成/文生图/Flux2 文生图_1986239618842578945.json, 图片生成/文生图/Flux2-Turbo加速生图_2005931616717467650.json, 图片生成/文生图/flux.2量化+SageAttention加速图像编辑（单图）_1994854140247465985.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_21

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/FLUX2-dev文生图_1993862047901433857.json、图片生成/文生图/FLUX2-dev文生图工作流_1993549884353609730.json、图片生成/文生图/FLUX2-多参考一致性创意场景合成_2090769208387923969.json、图片生成/文生图/Flux.2 单图编辑 用嘴改图官方工作流_1998219021541629954.json、图片生成/文生图/Flux.2+LoRA文生图_1995120190486667265.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxGuidance`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 9/11 个有
- `LoadImage` —— 9/11 个有
- `ReferenceLatent` —— 9/11 个有
- `UNETLoader` —— 9/11 个有
- `VAEEncode` —— 9/11 个有
- `LoraLoaderModelOnly` —— 3/11 个有
- `RH_Translator` —— 3/11 个有
- `PreviewImage` —— 2/11 个有
- `UnetLoaderGGUF` —— 2/11 个有
- `CR SDXL Aspect Ratio` —— 1/11 个有
- `ImpactInt` —— 1/11 个有
- `ModelPatchTorchSettings` —— 1/11 个有
- `PathchSageAttentionKJ` —— 1/11 个有
- `PreviewAny` —— 1/11 个有
- `PrimitiveInt` —— 1/11 个有
- `TTResolutionSelector` —— 1/11 个有
- `easy promptLine` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
