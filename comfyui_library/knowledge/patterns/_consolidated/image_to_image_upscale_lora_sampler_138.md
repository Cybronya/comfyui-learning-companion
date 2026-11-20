---
name: image_to_image_upscale_lora_sampler_138
type: Image To Image
frequency: 2
level: weak
coverage: 0.8835
common_nodes: [ACEPlusLoraConditioning, ACEPlusLoraProcessor, Any Switch (rgthree), CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DeepTranslatorTextNode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageScaleBy, ImageToMask, ImageUpscaleWithModel, JWStringConcat, KSampler, KSamplerAdvanced, LayerUtility: ColorImage V2, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: PurgeVRAM, LayerUtility: TextBox, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageInsetCrop, easy imageScaleDownToSize, easy imageSize, easy seed]
problems: []
missing: []
members: [平台全量/CHAOS 指令控图 智能改色换装 编辑物品  ICEdit提示词控制 工作流_1918671740984299521.json, 平台全量/Flux+ICEdit 一句话输入指令编辑改图图像一致性_1920634674056462338.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_138

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/CHAOS 指令控图 智能改色换装 编辑物品  ICEdit提示词控制 工作流_1918671740984299521.json、平台全量/Flux+ICEdit 一句话输入指令编辑改图图像一致性_1920634674056462338.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `ACEPlusLoraConditioning`
- `ACEPlusLoraProcessor`
- `Any Switch (rgthree)`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DeepTranslatorTextNode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageToMask`
- `ImageUpscaleWithModel`
- `JWStringConcat`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: TextBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageInsetCrop`
- `easy imageScaleDownToSize`
- `easy imageSize`
- `easy seed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 50% |
| Prompt 约束强度(CFG) | 28 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | beta | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 28，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 beta，2 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 28，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
