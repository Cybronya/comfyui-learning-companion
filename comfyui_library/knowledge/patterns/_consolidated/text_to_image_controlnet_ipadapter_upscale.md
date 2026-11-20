---
name: text_to_image_controlnet_ipadapter_upscale
type: Text To Image
frequency: 21
level: moderate
coverage: 0.714333
common_nodes: [BrushNet, BrushNetLoader, CLIPTextEncode, CLIPTextEncodeFlux, CLIPVisionLoader, CannyEdgePreprocessor, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DetailTransfer, DetailerForEachDebug, DualCLIPLoader, Efficient Loader, EmptyLatentImage, ICLightConditioning, IPAdapterAdvanced, IPAdapterUnifiedLoader, ImageScale, ImageScaleBy, ImageToMask, ImageUpscaleWithModel, ImpactDilateMask, InvertMask, KSampler, KSampler (Efficient), LayerMask: MaskGrow, LayerMask: SegmentAnythingUltra V2, LayerUtility: ExtendCanvas, LayerUtility: ImageBlend, LoadAndApplyICLightUnet, LoadImage, MaskToImage, MaskToSEGS, SaveImage, TextInput_, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageScaleDownToSize, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人像摄影工作流（SDXL+Brushnet+Ipadapter+Flux优化+Iclight打光)_1993219776535265281.json, 图片生成/图生图/创意人物写真工作流（换背景+重新打光）_2073707407326400513.json, 图片生成/图生图/图片人物重塑换背景+重新打光_2096072273827549185.json, 图片生成/图生图/图片人物重塑（换背景+重新打光）_2067071233581215746.json, 图片生成/图生图/图片人物重塑（换背景+重新打光）_2069237329864249345.json, 图片生成/图生图/图生图 PRO_2030958376661815298.json, 图片生成/图生图/超强人像摄影工作流（人像换背景）_1974665057567158273.json, 图片生成/文生图/奇幻北京创意写真，换背景工作流_2020680676072230914.json, 平台全量/人像摄影工作流（SDXL+Brushnet+Ipadapter+Flux优化+Iclight打光)_1957322367137673218.json, 平台全量/创意人物写真 换背景+重新打光工作流_2066844156068196354.json, 平台全量/创意人物写真工作流换背景+重新打光_2095789137893871617.json, 平台全量/创意人物写真工作流换背景+重新打光_2096140261855416322.json, 平台全量/创意人物写真工作流（换背景+重新打光）_2066791574348062721.json, 平台全量/图片人物重塑换背景+重新打光_2095780595849850882.json, 平台全量/奇幻背景创意人物写真工作流_1985674745289027585.json, 平台全量/奇幻背景创意人物写真工作流_2008120013621825538.json, 平台全量/工作流项目篇11-人像摄影工作流—蒙版做的好，效果越好Flux优化+Iclight打光_1976611340049620993.json, 视频生成/图生视频/PRO图生图工具｜文生图图生视频多模态处理_2094305135324389378.json, 视频生成/图生视频/PRO级图生图｜超强风格模拟背景创意光影画质优化_2090828347478728705.json, 视频生成/图生视频/创意人物写真工作流（换背景+重新打光）_2067057454910885889.json, 视频生成/图生视频/超强风格模拟图生图 PRO 光影画质优化创意背景文生图_2094168668145012738.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_ipadapter_upscale

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/人像摄影工作流（SDXL+Brushnet+Ipadapter+Flux优化+Iclight打光)_1993219776535265281.json、图片生成/图生图/创意人物写真工作流（换背景+重新打光）_2073707407326400513.json、图片生成/图生图/图片人物重塑换背景+重新打光_2096072273827549185.json、图片生成/图生图/图片人物重塑（换背景+重新打光）_2067071233581215746.json、图片生成/图生图/图片人物重塑（换背景+重新打光）_2069237329864249345.json…）

- **类型**：Text To Image
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 21 个 workflow 都包含：
- `BrushNet`
- `BrushNetLoader`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `CLIPVisionLoader`
- `CannyEdgePreprocessor`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DetailTransfer`
- `DetailerForEachDebug`
- `DualCLIPLoader`
- `Efficient Loader`
- `EmptyLatentImage`
- `ICLightConditioning`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `ImageScale`
- `ImageScaleBy`
- `ImageToMask`
- `ImageUpscaleWithModel`
- `ImpactDilateMask`
- `InvertMask`
- `KSampler`
- `KSampler (Efficient)`
- `LayerMask: MaskGrow`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ExtendCanvas`
- `LayerUtility: ImageBlend`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `MaskToImage`
- `MaskToSEGS`
- `SaveImage`
- `TextInput_`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageScaleDownToSize`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 17/21 个有
- `PreviewImage` —— 17/21 个有
- `PreviewMask_` —— 17/21 个有
- `CLIPLoader` —— 15/21 个有
- `LoraLoaderModelOnly` —— 15/21 个有
- `GrowMask` —— 14/21 个有
- `DF_Text_Box` —— 13/21 个有
- `LoraLoader` —— 13/21 个有
- `JWImageResizeByLongerSide` —— 12/21 个有
- `Joy_caption_two` —— 12/21 个有
- `Joy_caption_two_load` —— 12/21 个有
- `LatentUpscaleBy` —— 12/21 个有
- `QwenImageIntegratedKSampler` —— 12/21 个有
- `ShowText|pysssss` —— 12/21 个有
- `JjkText` —— 3/21 个有
- `solarL_SaveImagesToZip` —— 3/21 个有
- `孤海注释` —— 3/21 个有
- `Color (hexadecimal)` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.3 | 0.3 - 0.3 | 21 | 100% |
| 宽度 | 512 | 80 - 1024 | 21 | 59% |
| 高度 | 512 | 80 - 1536 | 21 | 45% |
| 采样步数 | 图生图 image-to-image | - | 21 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 21 | 27% |
| 采样算法 | 0 | 0 - 0 | 12 | 100% |
| 调度器 | 0 | 0 - 0 | 12 | 100% |
| 重绘幅度 | 999 | 0.2 - 999 | 21 | 14% |
| LoRA 模型强度 | 0.8 | 0.8 - 0.8 | 13 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.3，观测区间 0.3 - 0.3，21 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 80 - 1024，21 个样本
- 高度 中位数 512，观测区间 80 - 1536，21 个样本，取值分散，一致性仅 45%
- 采样步数 最常用 图生图 image-to-image，21 个样本，一致性 57%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，21 个样本，取值分散，一致性仅 27%
- 采样算法 中位数 0，观测区间 0 - 0，12 个样本，取值集中（一致性 100%）
- 调度器 中位数 0，观测区间 0 - 0，12 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 999，观测区间 0.2 - 999，21 个样本，取值分散，一致性仅 14%
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 0.8，13 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 风险：重绘幅度 观测到 999，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
