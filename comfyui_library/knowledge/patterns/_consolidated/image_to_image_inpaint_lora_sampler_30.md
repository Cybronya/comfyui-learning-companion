---
name: image_to_image_inpaint_lora_sampler_30
type: Image To Image
frequency: 2
level: weak
coverage: 0.921
common_nodes: [CLIPTextEncodeFlux, CLIPVisionEncode, CLIPVisionLoader, CR Text, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, EmptyLatentImage, Florence2ModelLoader, Florence2Run, ImageConcanate, ImageCrop+, ImageResize+, ImageScale, ImageToMask, InpaintModelConditioning, Int, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModel, LayerUtility: ColorImage V2, LayerUtility: ColorPicker, LayerUtility: CropByMask V2, LayerUtility: ImageRemoveAlpha, LayerUtility: PurgeVRAM, LayerUtility: RestoreCropBox, LayerUtility: TextJoin, LoadImage, LoraLoader, LoraLoaderModelOnly, MaskToImage, ModelSamplingFlux, ReduxAdvanced, ResizeMask, SaveImage, ShowText|pysssss, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: []
missing: []
members: [平台全量/【多角度重绘】FLUX电商模特服装更换三视图产品迁移_1912788891722575873.json, 平台全量/人物三视图2.0版本_1895001416610217985.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_lora_sampler_30

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/【多角度重绘】FLUX电商模特服装更换三视图产品迁移_1912788891722575873.json、平台全量/人物三视图2.0版本_1895001416610217985.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Florence2ModelLoader`
- `Florence2Run`
- `ImageConcanate`
- `ImageCrop+`
- `ImageResize+`
- `ImageScale`
- `ImageToMask`
- `InpaintModelConditioning`
- `Int`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModel`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ColorPicker`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: RestoreCropBox`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `ModelSamplingFlux`
- `ReduxAdvanced`
- `ResizeMask`
- `SaveImage`
- `ShowText|pysssss`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| 采样步数 | 24 | - | 2 | 83% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0.6 | - | 2 | 33% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 24，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.6，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
