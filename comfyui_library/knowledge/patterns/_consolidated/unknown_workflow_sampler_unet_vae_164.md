---
name: unknown_workflow_sampler_unet_vae_164
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.921
common_nodes: [BasicScheduler, CLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Krea2 Multi-Image Reference Editing_2073788017583673345.json, 图片生成/文生图/Krea2文生图标准工作流_2091191129374019586.json, 图片生成/文生图/pipi-anima高级采样器工作流_2078243608947412994.json, 图片生成/文生图/z-image-turbo-union2.1控制_2011994282508423170.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_164

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Krea2 Multi-Image Reference Editing_2073788017583673345.json、图片生成/文生图/Krea2文生图标准工作流_2091191129374019586.json、图片生成/文生图/pipi-anima高级采样器工作流_2078243608947412994.json、图片生成/文生图/z-image-turbo-union2.1控制_2011994282508423170.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 3/4 个有
- `CLIPTextEncode` —— 3/4 个有
- `LoadImage` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `ResolutionSelector` —— 2/4 个有
- `AIO_Preprocessor` —— 1/4 个有
- `CFGGuider` —— 1/4 个有
- `FluxGuidance` —— 1/4 个有
- `Krea2EditRebalance` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `LazyCache` —— 1/4 个有
- `ModelPatchLoader` —— 1/4 个有
- `QwenImageDiffsynthControlnet` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 864 - 2048 | 4 | 62% |
| 高度 | 1232 | 1024 - 2048 | 4 | 70% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 864 - 2048，4 个样本
- 高度 中位数 1232，观测区间 1024 - 2048，4 个样本
