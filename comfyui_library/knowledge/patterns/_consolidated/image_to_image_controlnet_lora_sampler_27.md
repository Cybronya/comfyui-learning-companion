---
name: image_to_image_controlnet_lora_sampler_27
type: Image To Image
frequency: 2
level: weak
coverage: 0.8405
common_nodes: [AIO_Preprocessor, ControlNetApplyAdvanced, ControlNetLoader, FastCanvas, FastCanvasTool, HYPIRImageRestoration, Image Comparer (rgthree), ImageCompositeMasked, KSampler, LayerUtility: ColorImage V2, LayerUtility: ColorPicker, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy hiresFix, easy imageCropFromMask, easy imageDetailTransfer, easy imageRemBg]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/【阡陌】Kontext +controlnet 精准融图工作流_1966364236257669121.json, 平台全量/【阡陌】qwen image +controlnet 精准融图工作流_1966355249067929602.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler_27

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/【阡陌】Kontext +controlnet 精准融图工作流_1966364236257669121.json、平台全量/【阡陌】qwen image +controlnet 精准融图工作流_1966355249067929602.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `FastCanvas`
- `FastCanvasTool`
- `HYPIRImageRestoration`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `KSampler`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ColorPicker`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy hiresFix`
- `easy imageCropFromMask`
- `easy imageDetailTransfer`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 1/2 个有
- `CLIPLoader` —— 1/2 个有
- `CLIPTextEncode` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `DeepTranslatorTextNode` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `EasyCache` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `ReferenceLatent` —— 1/2 个有
- `TextEncodeQwenImageEditEnhanced` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
