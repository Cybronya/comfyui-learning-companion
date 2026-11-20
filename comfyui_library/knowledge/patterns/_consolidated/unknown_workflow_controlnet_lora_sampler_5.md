---
name: unknown_workflow_controlnet_lora_sampler_5
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.558571
common_nodes: [Anything Everywhere3, BatchCount+, BlockifyMask, CLIPLoader, CM_BoolUnaryOperation, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, DF_Float, DF_Integer, DWPreprocessor, DrawMaskOnImage, GH_CropRestore, GH_MaskCropV2, GetNode, GrowMaskWithBlur, GuHaiMaskDetect, GuHai_FaceAlignment, GuhaiBatchProgress_孤海批处理进度条, GulfSeaImageMergeMask, ImageColorMatch+, ImageMaskPreview_Guhai, ImageResize+, ImpactInt, ImpactSEGSToMaskBatch, ImpactSwitch, KSampler, LayerMask: MaskGrow, LayerUtility: BooleanOperator, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskFix+, MaskToSEGS, PlaySound|pysssss, PreviewImage, PrimitiveBoolean, QwenEditConfigPreparer, RMBG, RemoveBackgroundWithMask, SaveImage, SegsToCombinedMask, SetNode, SetUnionControlNetType, SimpleMath+, TextEncodeQwenImageEditPlusCustom_lrzjason, ToBinaryMask, UNETLoader, VAEDecode, VAELoader, easy forLoopEnd, easy forLoopStart, easy humanSegmentation, easy ifElse, 图像缩放范围孤海, 孤海-浮点滑条, 孤海-遮罩混合运算, 孤海Seg次序过滤, 孤海遮罩分析, 数学运算_孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 一键换脸、换头（超强一致性 支持多人）_2054891041886613505.json, 图片生成/图生图/Qwen2511一键换脸换头超强一致性支持多人_2066162919523573762.json, 图片生成/图生图/Qwen2511一键换脸换头超强一致性支持多人_2066714844191092738.json, 图片生成/图生图/【精选系列】Qwen 一键换脸、换头（超强一致性 支持多人）_2058417792709386241.json, 图片生成/图生图/一键换脸、换头（超强一致性+支持多人）_2057735831397421057.json, 图片生成/图生图/一键换脸、换头（超强一致性+支持多人）_2062002510138793985.json, 图片生成/图生图/松间月 一键换脸、换头（加速版）_2006822928846950401.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_5

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen 一键换脸、换头（超强一致性 支持多人）_2054891041886613505.json、图片生成/图生图/Qwen2511一键换脸换头超强一致性支持多人_2066162919523573762.json、图片生成/图生图/Qwen2511一键换脸换头超强一致性支持多人_2066714844191092738.json、图片生成/图生图/【精选系列】Qwen 一键换脸、换头（超强一致性 支持多人）_2058417792709386241.json、图片生成/图生图/一键换脸、换头（超强一致性+支持多人）_2057735831397421057.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：56%

## 共有节点

全部 7 个 workflow 都包含：
- `Anything Everywhere3`
- `BatchCount+`
- `BlockifyMask`
- `CLIPLoader`
- `CM_BoolUnaryOperation`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DF_Float`
- `DF_Integer`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `GH_CropRestore`
- `GH_MaskCropV2`
- `GetNode`
- `GrowMaskWithBlur`
- `GuHaiMaskDetect`
- `GuHai_FaceAlignment`
- `GuhaiBatchProgress_孤海批处理进度条`
- `GulfSeaImageMergeMask`
- `ImageColorMatch+`
- `ImageMaskPreview_Guhai`
- `ImageResize+`
- `ImpactInt`
- `ImpactSEGSToMaskBatch`
- `ImpactSwitch`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerUtility: BooleanOperator`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskFix+`
- `MaskToSEGS`
- `PlaySound|pysssss`
- `PreviewImage`
- `PrimitiveBoolean`
- `QwenEditConfigPreparer`
- `RMBG`
- `RemoveBackgroundWithMask`
- `SaveImage`
- `SegsToCombinedMask`
- `SetNode`
- `SetUnionControlNetType`
- `SimpleMath+`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `ToBinaryMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy humanSegmentation`
- `easy ifElse`
- `图像缩放范围孤海`
- `孤海-浮点滑条`
- `孤海-遮罩混合运算`
- `孤海Seg次序过滤`
- `孤海遮罩分析`
- `数学运算_孤海`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 6/7 个有
- `SeedVR2LoadDiTModel` —— 6/7 个有
- `SeedVR2LoadVAEModel` —— 6/7 个有
- `SeedVR2VideoUpscaler` —— 6/7 个有
- `easy cleanGpuUsed` —— 6/7 个有
- `CachePreviewBridge` —— 5/7 个有
- `PreviewBridge` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 2 | 2 - 2 | 7 | 100% |
| 采样步数 | 10 | 4 - 10 | 7 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 2，观测区间 2 - 2，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 4 - 10，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
