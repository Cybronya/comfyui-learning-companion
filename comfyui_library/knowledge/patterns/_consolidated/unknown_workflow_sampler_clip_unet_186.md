---
name: unknown_workflow_sampler_clip_unet_186
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.878333
common_nodes: [CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, EmptySD3LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Anima-702-护士长_2072661208766959618.json, 图片生成/文生图/Hyperrealistic_ Z-image + Flux klein_2017132941884788737.json, 图片生成/文生图/Z-image双采+klein放大_2016526059369406465.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_186

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Anima-702-护士长_2072661208766959618.json、图片生成/文生图/Hyperrealistic_ Z-image + Flux klein_2017132941884788737.json、图片生成/文生图/Z-image双采+klein放大_2016526059369406465.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptySD3LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `ImageSharpen` —— 2/3 个有
- `KSamplerAdvanced` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `BasicGuider` —— 1/3 个有
- `FLS_SamplerV4` —— 1/3 个有
- `FluxGuidance` —— 1/3 个有
- `FluxKontextImageScale` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `PlaySound|pysssss` —— 1/3 个有
- `RTXVideoSuperResolution` —— 1/3 个有
- `ResolutionSelector` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 13.5 | - | 2 | 89% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 13.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 15，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
