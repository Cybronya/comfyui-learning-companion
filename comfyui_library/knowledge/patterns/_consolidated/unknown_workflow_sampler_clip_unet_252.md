---
name: unknown_workflow_sampler_clip_unet_252
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9175
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, INTConstant, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, PreviewAny, PreviewImage, RH_CinematicVideoGenerator, RH_Translator, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveVideo, Text Multiline, TextCombinerSix, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2034904305618132994.json, 视频生成/文生视频/提示词扩写+真人角色绕审核超能视频2.0测试版工作流_2034202086610575362.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_252

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2034904305618132994.json、视频生成/文生视频/提示词扩写+真人角色绕审核超能视频2.0测试版工作流_2034202086610575362.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `INTConstant`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `PreviewAny`
- `PreviewImage`
- `RH_CinematicVideoGenerator`
- `RH_Translator`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `Text Multiline`
- `TextCombinerSix`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadVideo` —— 1/2 个有
- `MuyeTextEditOutput` —— 1/2 个有
- `RH_SeedanceVideoRefToVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
