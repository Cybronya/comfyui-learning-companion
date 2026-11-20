---
name: unknown_workflow_upscale_sampler_clip_30
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.967
common_nodes: [CLIPLoader, CLIPTextEncode, FlowMatchEulerDiscreteScheduler (Custom), JWInteger, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, ModelSamplingAuraFlow, PrimitiveStringMultiline, SamplerCustom, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader, easy getNode, easy setNode]
problems: []
missing: []
members: [图片生成/图生图/Z-Image官方采样器图生图高清2K版_2010571531469983746.json, 图片生成/文生图/Z-Image官方采样器文生图高清2K版_1995855860368912385.json, 图片生成/文生图/zimage base 直出2K版_2016352620927000578.json, 图片生成/文生图/zimage base 直出2K版_2016502072132243458.json, 图片生成/文生图/zimage base版本官方采样器文生图_2016350634324271105.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_30

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Z-Image官方采样器图生图高清2K版_2010571531469983746.json、图片生成/文生图/Z-Image官方采样器文生图高清2K版_1995855860368912385.json、图片生成/文生图/zimage base 直出2K版_2016352620927000578.json、图片生成/文生图/zimage base 直出2K版_2016502072132243458.json、图片生成/文生图/zimage base版本官方采样器文生图_2016350634324271105.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `FlowMatchEulerDiscreteScheduler (Custom)`
- `JWInteger`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `ModelSamplingAuraFlow`
- `PrimitiveStringMultiline`
- `SamplerCustom`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy getNode`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 4/5 个有
- `Int` —— 4/5 个有
- `RHHiddenNodes` —— 4/5 个有
- `KSampler` —— 2/5 个有
- `LoadImage` —— 2/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `PreviewTextNode` —— 1/5 个有
- `RH_Captioner_Pro` —— 1/5 个有
- `VAEEncode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 100% |
| 采样算法 | res_multistep | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
