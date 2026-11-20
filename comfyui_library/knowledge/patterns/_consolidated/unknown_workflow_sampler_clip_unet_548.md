---
name: unknown_workflow_sampler_clip_unet_548
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8915
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, LoadImage, LoadImageFromUrl, ModelSamplingFlux, Note Plus (mtb), RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/ReduxAdvanced元素复刻（mask + downsample）_1939593725955981313.json, 平台全量/VaeEncodeUpscale_VAE编码器重绘修复_1956976352350101506.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_548

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/ReduxAdvanced元素复刻（mask + downsample）_1939593725955981313.json、平台全量/VaeEncodeUpscale_VAE编码器重绘修复_1956976352350101506.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `LoadImageFromUrl`
- `ModelSamplingFlux`
- `Note Plus (mtb)`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `Get Image Size` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ReduxAdvanced` —— 1/2 个有
- `StyleModelLoader` —— 1/2 个有
- `VAEEncode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
