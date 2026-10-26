---
name: text_to_image_controlnet_upscale_lora_4
type: Text To Image
frequency: 4
level: strong
coverage: 0.98825
common_nodes: [ApplyInstantID, CFGNorm, CLIPLoader, CLIPTextEncode, CM_IntToFloat, CM_IntToNumber, CM_NumberToInt, CM_NumberUnaryOperation, CR Prompt Text, CR Upscale Image, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, FaceAnalysisModels, FaceBoundingBox, GetImageSize+, ImageComposite+, ImageScale, ImageScaleBy, InstantIDFaceAnalysis, InstantIDModelLoader, JWImageResizeByLongerSide, JWInteger, KSampler, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask, LayerUtility: LayerImageTransform, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SaveLatent, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, SetLatentNoiseMask, TT_img_enc, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageToBase64, easy saveText, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/(亚洲私模)Qwen Image文生图（自用）V3_1973034022802731010.json, 图片生成/文生图/(亚洲私模+姿势+反推)Qwen Image文生图V3（自用）_1973036375224266754.json, 图片生成/文生图/（自用）API版Qwen Image文生图V3（贞贞N版）_1958929887488847873.json, 图片生成/文生图/（自用）API版Qwen Image文生图V4（贞贞N版+姿势+反推）_1972571951636148225.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_lora_4

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/(亚洲私模)Qwen Image文生图（自用）V3_1973034022802731010.json、图片生成/文生图/(亚洲私模+姿势+反推)Qwen Image文生图V3（自用）_1973036375224266754.json、图片生成/文生图/（自用）API版Qwen Image文生图V3（贞贞N版）_1958929887488847873.json、图片生成/文生图/（自用）API版Qwen Image文生图V4（贞贞N版+姿势+反推）_1972571951636148225.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 4 个 workflow 都包含：
- `ApplyInstantID`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CM_IntToFloat`
- `CM_IntToNumber`
- `CM_NumberToInt`
- `CM_NumberUnaryOperation`
- `CR Prompt Text`
- `CR Upscale Image`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `GetImageSize+`
- `ImageComposite+`
- `ImageScale`
- `ImageScaleBy`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `JWImageResizeByLongerSide`
- `JWInteger`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropBoxResolve`
- `LayerUtility: CropByMask`
- `LayerUtility: LayerImageTransform`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SaveLatent`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `SetLatentNoiseMask`
- `TT_img_enc`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageToBase64`
- `easy saveText`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `ControlNetApplySD3` —— 2/4 个有
- `DWPreprocessor` —— 2/4 个有
- `Joy_caption_two_advanced` —— 2/4 个有
- `Joy_caption_two_load` —— 2/4 个有
- `Joy_extra_options` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `RHHiddenNodes` —— 2/4 个有
- `SetUnionControlNetType` —— 2/4 个有
- `ShellAgentPluginOutputText` —— 2/4 个有
- `Text Concatenate` —— 2/4 个有
- `easy showAnything` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | res_2m_ode | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| ControlNet 权重 | 0.45 | 0.1 - 0.8 | 4 | 22% |
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2m_ode，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.45，观测区间 0.1 - 0.8，4 个样本，取值分散，一致性仅 22%
- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
