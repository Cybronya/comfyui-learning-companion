---
name: unknown_workflow_controlnet_lora_sampler_4
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.689625
common_nodes: [Any Switch (rgthree), BlockifyMask, CLIPLoader, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, DWPreprocessor, DrawMaskOnImage, FaceMaskFromPoseKeypoints, GH_MaskGrowthBlur, Get Image Size, GrowMask, GuHaiMaskDetect, Image Comparer (rgthree), ImageAndMaskPreview, ImpactInt, ImpactMinMax, KSampler, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LayerMask: SegformerB2ClothesUltra, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, PreviewImage, PrimitiveBoolean, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, RemoveBackgroundWithMask, SaveImage, SetNode, SetUnionControlNetType, SimpleMath+, TextEncodeQwenImageEditPlusCustom_lrzjason, ToBinaryMask, UNETLoader, VAEDecode, VAELoader, easy ifElse, easy imageRemBg, 图像缩放V2_孤海, 孤海-遮罩混合运算, 孤海遮罩分析]
problems: []
missing: []
members: [图片生成/图生图/人像一键换装_2086997967059378177.json, 图片生成/图生图/人像换装 电商模特换装 服饰展示_2084447125894688770.json, 图片生成/图生图/人物换装qwen_2087748015124729858.json, 图片生成/图生图/换脸，自动遮罩换任意_1995435504558649345.json, 图片生成/图生图/老孙AI 人物换装 _ 换脸 _ 神还原 _ 支持多人_2109135835512791041.json, 图片生成/图生图/衣冠焕彩（人物换装 _ 换脸 _ 神还原 _ 支持多人 _ 证件照 _ 结婚登记照换装）_2083022723395182593.json, 图片生成/图生图/衣冠焕彩，换装、换脸_2083533077573365761.json, 图片生成/文生图/人物换装 _ 神还原 _ 支持多人 _ 证件照 换装_2056601215491993602.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_4

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/人像一键换装_2086997967059378177.json、图片生成/图生图/人像换装 电商模特换装 服饰展示_2084447125894688770.json、图片生成/图生图/人物换装qwen_2087748015124729858.json、图片生成/图生图/换脸，自动遮罩换任意_1995435504558649345.json、图片生成/图生图/老孙AI 人物换装 _ 换脸 _ 神还原 _ 支持多人_2109135835512791041.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 8 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BlockifyMask`
- `CLIPLoader`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `FaceMaskFromPoseKeypoints`
- `GH_MaskGrowthBlur`
- `Get Image Size`
- `GrowMask`
- `GuHaiMaskDetect`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImpactInt`
- `ImpactMinMax`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: SegformerB2ClothesUltra`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `PreviewImage`
- `PrimitiveBoolean`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditConfigPreparer`
- `RemoveBackgroundWithMask`
- `SaveImage`
- `SetNode`
- `SetUnionControlNetType`
- `SimpleMath+`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `ToBinaryMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy ifElse`
- `easy imageRemBg`
- `图像缩放V2_孤海`
- `孤海-遮罩混合运算`
- `孤海遮罩分析`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 7/8 个有
- `CLIPTextEncode` —— 6/8 个有
- `ConcatTextOfUtils` —— 6/8 个有
- `Fast Groups Bypasser (rgthree)` —— 6/8 个有
- `LG_Color_Match_V2` —— 6/8 个有
- `LatentUpscaleBy` —— 6/8 个有
- `ReferenceLatent` —— 6/8 个有
- `SZ_KleinTiledKSampler` —— 6/8 个有
- `VAEDecodeTiled` —— 6/8 个有
- `VAEEncodeTiled` —— 6/8 个有
- `忽略多组孤海` —— 6/8 个有
- `AIO_Preprocessor` —— 2/8 个有
- `Anything Everywhere3` —— 2/8 个有
- `BasicScheduler` —— 2/8 个有
- `CLIPTextEncodeFlux` —— 2/8 个有
- `DetailDaemonSamplerNode` —— 2/8 个有
- `DualCLIPLoader` —— 2/8 个有
- `Fast Groups Muter (rgthree)` —— 2/8 个有
- `Image Levels Adjustment` —— 2/8 个有
- `KSamplerSelect` —— 2/8 个有
- `LayerFilter: FilmV2` —— 2/8 个有
- `ModelSamplingFlux` —— 2/8 个有
- `String Literal` —— 2/8 个有
- `UltimateSDUpscaleCustomSample` —— 2/8 个有
- `UpscaleModelLoader` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `easy isMaskEmpty` —— 2/8 个有
- `AutoCropFaces` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `MaskPreview` —— 1/8 个有
- `MaskPreview+` —— 1/8 个有
- `Text` —— 1/8 个有
- `孤海注释` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | 4 - 10 | 8 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 50% |
| 调度器 | beta | - | 8 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| ControlNet 权重 | 2 | 2 - 2 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 7，观测区间 4 - 10，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 50%
- 调度器 最常用 beta，8 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 2，观测区间 2 - 2，8 个样本，取值集中（一致性 100%）
