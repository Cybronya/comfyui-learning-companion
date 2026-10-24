---
name: text_to_image_controlnet_lora_sampler_17
type: Text To Image
frequency: 3
level: strong
coverage: 0.612
common_nodes: [BatchCount+, BlockifyMask, CLIPLoader, CLIPTextEncode, CM_BoolUnaryOperation, CachePreviewBridge, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, DF_Float, DF_Integer, DWPreprocessor, DrawMaskOnImage, EmptyLatentImage, GH_CropRestore, GH_MaskCropV2, GetNode, GrowMaskWithBlur, GuHaiMaskDetect, GuHai_FaceAlignment, GuhaiBatchProgress_孤海批处理进度条, GulfSeaImageMergeMask, ImageColorMatch+, ImageMaskPreview_Guhai, ImageResize+, ImpactSEGSToMaskBatch, JjkText, KSampler, LayerMask: MaskGrow, LayerUtility: BooleanOperator, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskFix+, MaskToSEGS, PlaySound|pysssss, PreviewImage, QwenEditConfigPreparer, RMBG, RemoveBackgroundWithMask, SaveImage, SegsToCombinedMask, SetNode, SetUnionControlNetType, SimpleMath+, TextEncodeQwenImageEditPlusCustom_lrzjason, ToBinaryMask, UNETLoader, VAEDecode, VAELoader, easy forLoopEnd, easy forLoopStart, easy humanSegmentation, easy ifElse, solarL_SaveImagesToZip, 图像缩放范围孤海, 孤海-遮罩混合运算, 孤海Seg次序过滤, 孤海注释, 孤海遮罩分析, 数学运算_孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/多人换脸换头｜Qwen2511超强一致性图生图_2092933402344382465.json, 图片生成/图生图/百变换脸换头工具 多人超强一致性图像编辑_2098291362478247937.json, 图片生成/文生图/Krea2 Turbo极速文生图｜全节点注释含反推提示词_2093108370483011585.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler_17

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/多人换脸换头｜Qwen2511超强一致性图生图_2092933402344382465.json、图片生成/图生图/百变换脸换头工具 多人超强一致性图像编辑_2098291362478247937.json、图片生成/文生图/Krea2 Turbo极速文生图｜全节点注释含反推提示词_2093108370483011585.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 3 个 workflow 都包含：
- `BatchCount+`
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CM_BoolUnaryOperation`
- `CachePreviewBridge`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DF_Float`
- `DF_Integer`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `EmptyLatentImage`
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
- `ImpactSEGSToMaskBatch`
- `JjkText`
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
- `solarL_SaveImagesToZip`
- `图像缩放范围孤海`
- `孤海-遮罩混合运算`
- `孤海Seg次序过滤`
- `孤海注释`
- `孤海遮罩分析`
- `数学运算_孤海`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 2/3 个有
- `Fast Groups Muter (rgthree)` —— 2/3 个有
- `ImpactInt` —— 2/3 个有
- `ImpactSwitch` —— 2/3 个有
- `PrimitiveBoolean` —— 2/3 个有
- `SeedVR2LoadDiTModel` —— 2/3 个有
- `SeedVR2LoadVAEModel` —— 2/3 个有
- `SeedVR2VideoUpscaler` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `孤海-浮点滑条` —— 2/3 个有
- `GoohaiUniversalSlider` —— 1/3 个有
- `LG_Color_Match_V2` —— 1/3 个有
- `LatentUpscaleBy` —— 1/3 个有
- `ReferenceLatent` —— 1/3 个有
- `SAM3Segment` —— 1/3 个有
- `SZ_KleinTiledKSampler` —— 1/3 个有
- `VAEDecodeTiled` —— 1/3 个有
- `VAEEncode` —— 1/3 个有
- `easy anythingIndexSwitch` —— 1/3 个有
- `图像缩放V2_孤海` —— 1/3 个有
- `布尔孤海` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 2 | 2 - 2 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 2，观测区间 2 - 2，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
