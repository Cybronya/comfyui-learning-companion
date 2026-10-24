---
name: unknown_workflow_lora_sampler_clip_227
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.885
common_nodes: [Anything Everywhere3, CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageConcanate, ImageCrop+, ImageToMask, KSampler, LayerUtility: ColorImage V2, LayerUtility: GetImageSize, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, RepeatLatentBatch, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux模型生成产品背景图_1914531621264130050.json, 图片生成/图生图/产品生成背景图FLUX版，文生图，光影融合，一键出图_1911967829166620674.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_227

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux模型生成产品背景图_1914531621264130050.json、图片生成/图生图/产品生成背景图FLUX版，文生图，光影融合，一键出图_1911967829166620674.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageConcanate`
- `ImageCrop+`
- `ImageToMask`
- `KSampler`
- `LayerUtility: ColorImage V2`
- `LayerUtility: GetImageSize`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RepeatLatentBatch`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `InpaintModelConditioning` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 35 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 35，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
