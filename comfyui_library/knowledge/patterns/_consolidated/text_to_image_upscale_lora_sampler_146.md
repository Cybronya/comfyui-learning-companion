---
name: text_to_image_upscale_lora_sampler_146
type: Text To Image
frequency: 2
level: weak
coverage: 0.8945
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize, GrowMaskWithBlur, JjkText, KSampler, LayerColor: Exposure, LayerFilter: FilmV2, LayerMask: PersonMaskUltra V2, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, PrimitiveInt, RHHiddenNodes, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader, ZML_ImageSelectorNode, easy imageConcat, easy imageRemBg, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/FireRed千问Qwen一键换背景场景换装｜换头换脸可选朋友圈封神工作流_2087153883746488321.json, 平台全量/FluxKlein姿势复制姿态迁移｜换装换脸换背景商用旅拍大片_2089011404979396610.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_146

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/FireRed千问Qwen一键换背景场景换装｜换头换脸可选朋友圈封神工作流_2087153883746488321.json、平台全量/FluxKlein姿势复制姿态迁移｜换装换脸换背景商用旅拍大片_2089011404979396610.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize`
- `GrowMaskWithBlur`
- `JjkText`
- `KSampler`
- `LayerColor: Exposure`
- `LayerFilter: FilmV2`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `RHHiddenNodes`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `ZML_ImageSelectorNode`
- `easy imageConcat`
- `easy imageRemBg`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `Dapao_LlamaCaption` —— 1/2 个有
- `FlexLoraLoaderModelOnly` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageColorMatchAdobe+` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `PainterFluxImageEdit` —— 1/2 个有
- `QwenImageIntegratedKSampler` —— 1/2 个有
- `RandomPromptSelector` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `easy seed` —— 1/2 个有
- `easy showAnything` —— 1/2 个有
- `孤海外补画板按方向` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 80 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（5/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
