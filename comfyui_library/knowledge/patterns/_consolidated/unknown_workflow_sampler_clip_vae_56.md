---
name: unknown_workflow_sampler_clip_vae_56
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8625
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, KSamplerSelect, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux.2溶图_1995426699946995714.json, 图片生成/文生图/Flux2 文生图_图生图_图像修改_多图参考工作流_1993868752053796866.json, 图片生成/文生图/flux.2图像编辑测试（单图）_1995053515309506561.json, 图片生成/文生图/flux.2量化+SageAttention加速图像编辑（单图）_1994854140247465985.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_56

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Flux.2溶图_1995426699946995714.json、图片生成/文生图/Flux2 文生图_图生图_图像修改_多图参考工作流_1993868752053796866.json、图片生成/文生图/flux.2图像编辑测试（单图）_1995053515309506561.json、图片生成/文生图/flux.2量化+SageAttention加速图像编辑（单图）_1994854140247465985.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 3/4 个有
- `UnetLoaderGGUF` —— 3/4 个有
- `PreviewImage` —— 2/4 个有
- `RH_Translator` —— 2/4 个有
- `UNETLoader` —— 2/4 个有
- `Compositor3` —— 1/4 个有
- `CompositorConfig3` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `InspyrenetRembg` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `easy promptLine` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
