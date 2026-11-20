---
name: unknown_workflow_controlnet_lora_sampler_3
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.633
common_nodes: [CLIPLoader, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, Int, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerUtility: ColorImage V2, LayerUtility: ImageBlendAdvance, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskFastGrow, MaskFillHoles, MaskToImage, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, SaveImage, SetUnionControlNetType, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen-人物置换_1991684055253073921.json, 图片生成/图生图/Qwen-遮罩人物置换_1999028251177668609.json, 图片生成/图生图/一键换万物_1991819409924878337.json, 图片生成/图生图/一键换万物_1992684651221241858.json, 图片生成/图生图/一键换万物自动版（快捷）_1991839250284957697.json, 图片生成/图生图/图片人物迁移升级版_1992793687887335425.json, 图片生成/图生图/局部编辑+参考图+全节点注释_2056245946870231041.json, 图片生成/图生图/超级自然人物迁移拍照打卡_1991728596093972482.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_3

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen-人物置换_1991684055253073921.json、图片生成/图生图/Qwen-遮罩人物置换_1999028251177668609.json、图片生成/图生图/一键换万物_1991819409924878337.json、图片生成/图生图/一键换万物_1992684651221241858.json、图片生成/图生图/一键换万物自动版（快捷）_1991839250284957697.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `Int`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskFastGrow`
- `MaskFillHoles`
- `MaskToImage`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditConfigPreparer`
- `SaveImage`
- `SetUnionControlNetType`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConcatTextOfUtils` —— 7/8 个有
- `LayerUtility: ImageReel` —— 7/8 个有
- `LayerUtility: ImageReelComposit` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `AIO_Preprocessor` —— 6/8 个有
- `ImageCompositeMaskedWithSwitch` —— 6/8 个有
- `ImageScaleToTotalPixels` —— 6/8 个有
- `LayerMask: MaskGrow` —— 6/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `DrawViTPose` —— 2/8 个有
- `GetImageSize` —— 2/8 个有
- `GroundingDinoModelLoader_SDPose` —— 2/8 个有
- `LayerMask: MaskPreview` —— 2/8 个有
- `LayerMask: PersonMaskUltra V2` —— 2/8 个有
- `OnnxDetectionModelLoader` —— 2/8 个有
- `PoseAndFaceDetection` —— 2/8 个有
- `SDPoseOODLoader` —— 2/8 个有
- `SDPoseOODProcessor` —— 2/8 个有
- `YOLOModelLoader` —— 2/8 个有
- `easy clearCacheAll` —— 2/8 个有
- `DWPreprocessor` —— 1/8 个有
- `ImageCompositeMasked` —— 1/8 个有
- `ImageCompositeMaskedOneByOne` —— 1/8 个有
- `RHHiddenNodes` —— 1/8 个有
- `RH_Captioner` —— 1/8 个有
- `TTP_text_mix` —— 1/8 个有
- `TextInput_` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | beta57 | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| ControlNet 权重 | 2 | 1 - 2 | 8 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 beta57，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 2，观测区间 1 - 2，8 个样本
