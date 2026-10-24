---
name: unknown_workflow_sampler_clip_unet_415
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9025
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, LoadImage, ModelSamplingFlux, RH_Captioner, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux SRPO仿图_1969765351493935106.json, 图片生成/图生图/修复结构_1964879807592939522.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_415

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/flux SRPO仿图_1969765351493935106.json、图片生成/图生图/修复结构_1964879807592939522.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `RH_Captioner`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DF_Get_image_size` —— 1/2 个有
- `ImageScaleToMegapixels` —— 1/2 个有
- `JoyCaption` —— 1/2 个有
- `RepeatLatentBatch` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
