---
name: image_to_image_inpaint_upscale_lora_16
type: Image To Image
frequency: 2
level: weak
coverage: 0.7825
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, SUPIR_Upscale, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/最新移除LORA_1927918579570589697.json, 平台全量/移除万物+手动蒙版+智能修复_1962436176076476418.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_upscale_lora_16

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/最新移除LORA_1927918579570589697.json、平台全量/移除万物+手动蒙版+智能修复_1962436176076476418.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `SUPIR_Upscale`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 1/2 个有
- `INPAINT_ExpandMask` —— 1/2 个有
- `LayerMask: MaskPreview` —— 1/2 个有
- `Mask Fill Holes` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SetNode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 19 | - | 2 | 42% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 0.625 | - | 2 | 40% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 19，样本不足，未给区间，2 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 0.625，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
