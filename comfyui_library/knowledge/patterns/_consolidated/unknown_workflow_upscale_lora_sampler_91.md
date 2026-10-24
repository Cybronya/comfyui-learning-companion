---
name: unknown_workflow_upscale_lora_sampler_91
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.859
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, GrowMask, Image Comparer (rgthree), ImageUpscaleWithModel, InvertMask, JoinImageWithAlpha, KSamplerAdvanced, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, Upscale Model Loader, VAEDecode, VAEEncode, VAELoader, YUAN_TXTConvertAny]
problems: []
missing: []
members: [图片生成/图生图/krea2 局部修复_2112729383961194497.json, 图片生成/图生图/图片去红_2070444856769605634.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_91

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/krea2 局部修复_2112729383961194497.json、图片生成/图生图/图片去红_2070444856769605634.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `GrowMask`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `InvertMask`
- `JoinImageWithAlpha`
- `KSamplerAdvanced`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `Upscale Model Loader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `YUAN_TXTConvertAny`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 1/2 个有
- `Int` —— 1/2 个有
- `LatentBlend` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `ReferenceLatent` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 50% |
| Prompt 约束强度(CFG) | 6 | - | 2 | 67% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler_ancestral | - | 2 | 50% |
| 重绘幅度 | sgm_uniform | - | 2 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 6，样本不足，未给区间，2 个样本
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，2 个样本，一致性 50%
- 重绘幅度 最常用 sgm_uniform，2 个样本，一致性 50%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
