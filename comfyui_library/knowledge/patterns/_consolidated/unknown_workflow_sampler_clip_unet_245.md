---
name: unknown_workflow_sampler_clip_unet_245
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.947
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/最强开源 FLUX2系列合集_1993708586574479361.json, "视频生成/文生视频/谁与争锋 Flux2 Z-image,  多图编辑 挑战 Qwen Edit_1994227326332370945.json"]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_245

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/最强开源 FLUX2系列合集_1993708586574479361.json、视频生成/文生视频/谁与争锋 Flux2 Z-image,  多图编辑 挑战 Qwen Edit_1994227326332370945.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxGuidance`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ApplySageAttention` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `DeepTranslatorTextNode` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `ModelPatchTorchSettings` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
