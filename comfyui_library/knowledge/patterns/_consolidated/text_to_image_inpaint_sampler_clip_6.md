---
name: text_to_image_inpaint_sampler_clip_6
type: Text To Image
frequency: 2
level: weak
coverage: 0.874
common_nodes: [AILab_QwenVL, BasicScheduler, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DetailDaemonSamplerNode, DifferentialDiffusion, DualCLIPLoader, EmptyLatentImage, FluxGuidance, Image Comparer (rgthree), ImageScaleBy, ImageUntile+, InpaintModelConditioning, KSampler, KSamplerSelect, LayerMask: MaskGrow, LayerUtility: ColorImage V2, LayerUtility: ImageBlendAdvance V3, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageShift, Mask Invert, MaskPreview, Masks Subtract, PreviewBridge, PreviewImage, RepeatImageBatch, SamplerCustom, SaveImage, Seed (rgthree), ShowText|pysssss, SplitSigmas, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy mathInt, easy positive, easy promptConcat, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/z-image-flux-fill-onereward-无缝拼接图-无缝贴图-材质贴图_2041532484155875329.json, 平台全量/自动一键生成 无缝平铺图案 Z-lmage +Qwen 反推提示词  无缝拼接图 无缝贴图 材质贴图_2042074647923007489.json]
source: knowledge_consolidation
---

# text_to_image_inpaint_sampler_clip_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/z-image-flux-fill-onereward-无缝拼接图-无缝贴图-材质贴图_2041532484155875329.json、平台全量/自动一键生成 无缝平铺图案 Z-lmage +Qwen 反推提示词  无缝拼接图 无缝贴图 材质贴图_2042074647923007489.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DetailDaemonSamplerNode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageUntile+`
- `InpaintModelConditioning`
- `KSampler`
- `KSamplerSelect`
- `LayerMask: MaskGrow`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlendAdvance V3`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageShift`
- `Mask Invert`
- `MaskPreview`
- `Masks Subtract`
- `PreviewBridge`
- `PreviewImage`
- `RepeatImageBatch`
- `SamplerCustom`
- `SaveImage`
- `Seed (rgthree)`
- `ShowText|pysssss`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy mathInt`
- `easy positive`
- `easy promptConcat`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | bong_tangent | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 bong_tangent，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
