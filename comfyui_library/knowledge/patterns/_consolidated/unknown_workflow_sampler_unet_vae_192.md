---
name: unknown_workflow_sampler_unet_vae_192
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9086
common_nodes: [BasicGuider, BasicScheduler, DualCLIPLoader, EmptySD3LatentImage, FluxKontextImageScale, KSamplerSelect, LoadImage, ModelSamplingFlux, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux Kontext双图编辑开源版本_1938334902939222018.json, 图片生成/图生图/Flux Kontext图像编辑开源版本_1938325848867143681.json, 图片生成/图生图/Flux_Context_图片编辑_1938538258194169857.json, 图片生成/图生图/KONTEXT多图融合工作流_1945122220479848449.json, 图片生成/图生图/Kontext中文版提示词多图模式（开源版）_1938411083663343618.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_192

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux Kontext双图编辑开源版本_1938334902939222018.json、图片生成/图生图/Flux Kontext图像编辑开源版本_1938325848867143681.json、图片生成/图生图/Flux_Context_图片编辑_1938538258194169857.json、图片生成/图生图/KONTEXT多图融合工作流_1945122220479848449.json、图片生成/图生图/Kontext中文版提示词多图模式（开源版）_1938411083663343618.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxKontextImageScale`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 4/5 个有
- `FluxGuidance` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `ImageConcanate` —— 3/5 个有
- `Int` —— 3/5 个有
- `RH_Translator` —— 3/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `CLIPTextEncodeFlux` —— 1/5 个有
- `Compositor3` —— 1/5 个有
- `CompositorConfig3` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `ImageScale` —— 1/5 个有
- `ImageScaleBy` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `SeedVR2` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `easy imageRemBg` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
