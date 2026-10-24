---
name: unknown_workflow_lora_sampler_clip_204
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.983333
common_nodes: [CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, EmptySD3LatentImage, Flux2Scheduler, GetImageSize, ImageSharpen, KSamplerAdvanced, KSamplerSelect, LoraLoaderModelOnly, ModelSamplingAuraFlow, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-image双采+klein放大_2016526059369406465.json, 图片生成/文生图/Z双采+klein，V2_2044012106806206466.json, 图片生成/文生图/Z双采+klein，V3_2051888010416934913.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_204

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image双采+klein放大_2016526059369406465.json、图片生成/文生图/Z双采+klein，V2_2044012106806206466.json、图片生成/文生图/Z双采+klein，V3_2051888010416934913.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：98%

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
- `ImageSharpen`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `MuyeTextEditOutput` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `BasicGuider` —— 1/3 个有
- `FluxGuidance` —— 1/3 个有
- `FluxKontextImageScale` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 12 | 12 - 15 | 3 | 89% |
| 采样算法 | 4 | 1 - 4 | 3 | 53% |
| 调度器 | res_2s | - | 3 | 67% |
| 重绘幅度 | bong_tangent | - | 3 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 12，观测区间 12 - 15，3 个样本，取值集中（一致性 89%）
- 采样算法 中位数 4，观测区间 1 - 4，3 个样本
- 调度器 最常用 res_2s，3 个样本，一致性 67%
- 重绘幅度 最常用 bong_tangent，3 个样本，一致性 67%
- 风险：Prompt 约束强度(CFG) 观测到 15，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
