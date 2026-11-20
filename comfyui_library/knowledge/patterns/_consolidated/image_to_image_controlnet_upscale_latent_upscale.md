---
name: image_to_image_controlnet_upscale_latent_upscale
type: Image To Image
frequency: 11
level: moderate
coverage: 0.608364
common_nodes: [BatchCount+, BlockifyMask, CLIPLoader, CLIPTextEncode, CM_BoolUnaryOperation, CachePreviewBridge, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, DF_Float, DF_Integer, DWPreprocessor, DrawMaskOnImage, GH_CropRestore, GH_MaskCropV2, GetNode, GoohaiUniversalSlider, GrowMaskWithBlur, GuHaiMaskDetect, GuHai_FaceAlignment, GuhaiBatchProgress_孤海批处理进度条, GulfSeaImageMergeMask, ImageColorMatch+, ImageMaskPreview_Guhai, ImageResize+, ImpactSEGSToMaskBatch, KSampler, LG_Color_Match_V2, LatentUpscaleBy, LayerMask: MaskGrow, LayerUtility: BooleanOperator, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskFix+, MaskToSEGS, PlaySound|pysssss, PreviewImage, QwenEditConfigPreparer, RMBG, ReferenceLatent, RemoveBackgroundWithMask, SAM3Segment, SZ_KleinTiledKSampler, SaveImage, SegsToCombinedMask, SetNode, SetUnionControlNetType, SimpleMath+, TextEncodeQwenImageEditPlusCustom_lrzjason, ToBinaryMask, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy forLoopEnd, easy forLoopStart, easy humanSegmentation, easy ifElse, 图像缩放V2_孤海, 图像缩放范围孤海, 孤海-遮罩混合运算, 孤海Seg次序过滤, 孤海遮罩分析, 布尔孤海, 忽略多组孤海, 数学运算_孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 一键换脸、换头（超强一致性 支持多人）_2112706449871822849.json, 图片生成/图生图/Qwen+一键多人换脸、换头（搬运自“孤海AI”）_2078069788059987969.json, 图片生成/图生图/Qwen_一键换脸、换头超强一致性_支持多人_2085541373553504257.json, 图片生成/图生图/Qwen_一键换脸、换头超强一致性_支持多人_2085556537598234625.json, 图片生成/图生图/单人_多人换脸 全自动精准换脸 99.99% 相似度_2084094116975173633.json, 图片生成/图生图/支持多人换头超强一致性一键换脸Qwen_2085200549493952513.json, 图片生成/图生图/支持多人换头超强一致性一键换脸Qwen_2085207789718302721.json, 图片生成/图生图/百变换脸YSRH 1024_2097854870144512002.json, 图片生成/图生图/百变换脸、换头，二人、三人、多人（超强一致性）_2084984711142797314.json, 图片生成/图生图/百变换造型，超强一致性，RH9J_2093355477798318082.json, 图片生成/图生图/老孙AI 一键换脸、换头（一致性超强 支持多人）_2085387730040737794.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_latent_upscale

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen 一键换脸、换头（超强一致性 支持多人）_2112706449871822849.json、图片生成/图生图/Qwen+一键多人换脸、换头（搬运自“孤海AI”）_2078069788059987969.json、图片生成/图生图/Qwen_一键换脸、换头超强一致性_支持多人_2085541373553504257.json、图片生成/图生图/Qwen_一键换脸、换头超强一致性_支持多人_2085556537598234625.json、图片生成/图生图/单人_多人换脸 全自动精准换脸 99.99% 相似度_2084094116975173633.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 11 个 workflow 都包含：
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
- `GH_CropRestore`
- `GH_MaskCropV2`
- `GetNode`
- `GoohaiUniversalSlider`
- `GrowMaskWithBlur`
- `GuHaiMaskDetect`
- `GuHai_FaceAlignment`
- `GuhaiBatchProgress_孤海批处理进度条`
- `GulfSeaImageMergeMask`
- `ImageColorMatch+`
- `ImageMaskPreview_Guhai`
- `ImageResize+`
- `ImpactSEGSToMaskBatch`
- `KSampler`
- `LG_Color_Match_V2`
- `LatentUpscaleBy`
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
- `ReferenceLatent`
- `RemoveBackgroundWithMask`
- `SAM3Segment`
- `SZ_KleinTiledKSampler`
- `SaveImage`
- `SegsToCombinedMask`
- `SetNode`
- `SetUnionControlNetType`
- `SimpleMath+`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `ToBinaryMask`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy humanSegmentation`
- `easy ifElse`
- `图像缩放V2_孤海`
- `图像缩放范围孤海`
- `孤海-遮罩混合运算`
- `孤海Seg次序过滤`
- `孤海遮罩分析`
- `布尔孤海`
- `忽略多组孤海`
- `数学运算_孤海`

**可变部分**（部分 workflow 才有）：
- `easy anythingIndexSwitch` —— 9/11 个有
- `ImpactSwitch` —— 2/11 个有
- `JjkText` —— 2/11 个有
- `solarL_SaveImagesToZip` —— 2/11 个有
- `Anything Everywhere3` —— 1/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `ToggleAnyNode` —— 1/11 个有
- `孤海注释` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 2 | 2 - 2 | 11 | 100% |
| 采样步数 | 4 | 4 - 10 | 11 | 62% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 11 | 18% |
| 采样算法 | sa_solver | - | 11 | 73% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 11 | 73% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 2，观测区间 2 - 2，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 10，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，11 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 sa_solver，11 个样本，一致性 73%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，11 个样本，一致性 73%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
