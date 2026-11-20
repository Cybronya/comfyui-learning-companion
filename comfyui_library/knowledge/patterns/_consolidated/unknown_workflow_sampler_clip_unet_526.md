---
name: unknown_workflow_sampler_clip_unet_526
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.95
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSamplerSelect, LoadImage, ModelPatchLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/z-image-turbo-union2.1控制_2011994282508423170.json, 平台全量/深度控制文生图｜Qwen-Image 2.1 ControlNet INT8_2119400738123243522.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_526

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/z-image-turbo-union2.1控制_2011994282508423170.json、平台全量/深度控制文生图｜Qwen-Image 2.1 ControlNet INT8_2119400738123243522.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoadImage`
- `ModelPatchLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LazyCache` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `QwenImage21Cache` —— 1/2 个有
- `QwenImageDiffsynthControlnet` —— 1/2 个有
- `ZImageFunControlnet` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1408 | - | 2 | 55% |
| 高度 | 1408 | - | 2 | 55% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1408，样本不足，未给区间，2 个样本
- 高度 中位数 1408，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
