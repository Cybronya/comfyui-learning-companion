---
name: image_to_image_controlnet_upscale_lora_10
type: Image To Image
frequency: 3
level: strong
coverage: 0.836
common_nodes: [AIO_Preprocessor, ApplyFBCacheOnModel, ApplyInstantIDAdvanced, BNK_CLIPTextEncodeAdvanced, CR Text, CR Text Input Switch (4 way), CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DWPreprocessor, GetNode, HyperLoRAApplyLoRA, HyperLoRAConfig, HyperLoRAFaceAttr, HyperLoRAGenerateIDLoRA, HyperLoRAIDCond, HyperLoRALoader, Image Comparer (rgthree), Image Crop Face, ImpactMakeImageBatch, ImpactSwitch, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerMask: PersonMaskUltra V2, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RH_Captioner, SUPIR_Upscale, SaveImage, SetNode, SetUnionControlNetType, Text Concatenate, VAEDecode, VAEEncode, easy int]
problems: []
missing: []
members: [图片生成/图生图/海马体证件照!大师级_2058714849777119234.json, 图片生成/图生图/海马体证件照_1975072042024308738.json, 图片生成/图生图/海马体证件照_2010557940763205634.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_lora_10

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/海马体证件照!大师级_2058714849777119234.json、图片生成/图生图/海马体证件照_1975072042024308738.json、图片生成/图生图/海马体证件照_2010557940763205634.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `ApplyFBCacheOnModel`
- `ApplyInstantIDAdvanced`
- `BNK_CLIPTextEncodeAdvanced`
- `CR Text`
- `CR Text Input Switch (4 way)`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DWPreprocessor`
- `GetNode`
- `HyperLoRAApplyLoRA`
- `HyperLoRAConfig`
- `HyperLoRAFaceAttr`
- `HyperLoRAGenerateIDLoRA`
- `HyperLoRAIDCond`
- `HyperLoRALoader`
- `Image Comparer (rgthree)`
- `Image Crop Face`
- `ImpactMakeImageBatch`
- `ImpactSwitch`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `RH_Captioner`
- `SUPIR_Upscale`
- `SaveImage`
- `SetNode`
- `SetUnionControlNetType`
- `Text Concatenate`
- `VAEDecode`
- `VAEEncode`
- `easy int`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.45 | 0.45 - 0.45 | 3 | 100% |
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 3 | 100% |
| 采样算法 | dpmpp_2m | - | 3 | 100% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.45，观测区间 0.45 - 0.45，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 100%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
