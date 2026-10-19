---
name: text_to_image_video_lora_sampler_42
type: Text To Image
frequency: 15
level: weak
coverage: 0.913533
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DrawViTPose, EmptyLatentImage, GetImageRangeFromBatch, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, OnnxDetectionModelLoader, PathchSageAttentionKJ, PoseAndFaceDetection, SimpleMath+, SimpleMathDual+, TorchCompileModelWanVideoV2, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanAnimateToVideo, easy batchAnything, easy boolean, easy compare, easy convertAnything, easy ifElse, easy int, easy lengthAnything, easy positive, easy promptReplace, easy whileLoopEnd, easy whileLoopStart, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Comfy官版WanAnimate 动作迁移支持运镜采样无缝循环_2096736812248166401.json, 视频生成/图生视频/Comfy官版WanAnimate 动作迁移支持运镜采样无缝循环_2098645150116438017.json, 视频生成/图生视频/Wan2.2结合Animate动作迁移 视频人物运动复刻修复黑屏_2098627308616773633.json, 视频生成/图生视频/动作迁移升级版加表情动作不限时长，舞蹈模仿各种动作复刻图生视频_2103929374503424002.json, 视频生成/图生视频/动作迁移升级版加表情动作不限时长，舞蹈模仿各种动作复刻图生视频方案_2103608874556289026.json, 视频生成/图生视频/动作迁移升级版｜表情舞蹈模仿动作复刻 不限时长图生视频_2097562494444335106.json, 视频生成/图生视频/动作迁移精细版_面部表情加精细姿势，视频生视频可选高清_2111206681580494849.json, 视频生成/图生视频/动作迁移精细版上线｜面部表情精细姿势超抖X高清可选_2111079225896820737.json, 视频生成/图生视频/动作迁移精细版二发布｜超抖X表情姿势可选高清输出_2111092213093588993.json, 视频生成/图生视频/动作迁移精细版｜面部表情精细姿势超抖高清可选_2094885882292686849.json, 视频生成/图生视频/精细动作迁移可选高清，面部表情视频生视频方案_2111262550280200193.json, 视频生成/图生视频/2053103096611524610.json, 视频生成/图生视频/视频复刻升级版｜表情动作全保留图生视频同款跟拍_2101567713368952833.json, 视频生成/图生视频/2040663476045094914.json, 视频生成/图生视频/面部表情+精细姿势超抖X｜动作迁移精细版可选高清_2095084093120798722.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_42

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/Comfy官版WanAnimate 动作迁移支持运镜采样无缝循环_2096736812248166401.json、视频生成/图生视频/Comfy官版WanAnimate 动作迁移支持运镜采样无缝循环_2098645150116438017.json、视频生成/图生视频/Wan2.2结合Animate动作迁移 视频人物运动复刻修复黑屏_2098627308616773633.json、视频生成/图生视频/动作迁移升级版加表情动作不限时长，舞蹈模仿各种动作复刻图生视频_2103929374503424002.json、视频生成/图生视频/动作迁移升级版加表情动作不限时长，舞蹈模仿各种动作复刻图生视频方案_2103608874556289026.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 15 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DrawViTPose`
- `EmptyLatentImage`
- `GetImageRangeFromBatch`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `OnnxDetectionModelLoader`
- `PathchSageAttentionKJ`
- `PoseAndFaceDetection`
- `SimpleMath+`
- `SimpleMathDual+`
- `TorchCompileModelWanVideoV2`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanAnimateToVideo`
- `easy batchAnything`
- `easy boolean`
- `easy compare`
- `easy convertAnything`
- `easy ifElse`
- `easy int`
- `easy lengthAnything`
- `easy positive`
- `easy promptReplace`
- `easy whileLoopEnd`
- `easy whileLoopStart`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 14/15 个有
- `GetImageSize` —— 13/15 个有
- `JjkText` —— 13/15 个有
- `MathExpression|pysssss` —— 13/15 个有
- `SaveVideoRGBA` —— 13/15 个有
- `solarL_SaveImagesToZip` —— 13/15 个有
- `孤海注释` —— 13/15 个有
- `Int` —— 12/15 个有
- `RHHiddenNodes` —— 11/15 个有
- `FlashVSRNode` —— 10/15 个有
- `BlockifyMask` —— 9/15 个有
- `DownloadAndLoadSAM2Model` —— 9/15 个有
- `DrawMaskOnImage` —— 9/15 个有
- `Fast Groups Muter (rgthree)` —— 9/15 个有
- `GrowMask` —— 9/15 个有
- `LayerUtility: ImageBlend` —— 9/15 个有
- `PointsEditor` —— 9/15 个有
- `Sam2Segmentation` —— 9/15 个有
- `Seed` —— 9/15 个有
- `ImageConcatMulti` —— 7/15 个有
- `SaveImage` —— 5/15 个有
- `AILab_QwenVL` —— 2/15 个有
- `CFGNorm` —— 2/15 个有
- `ConditioningZeroOut` —— 2/15 个有
- `CropWithPadInfo` —— 2/15 个有
- `FirstFrameSelector` —— 2/15 个有
- `FluxGuidance` —— 2/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/15 个有
- `MemoryCleaner` —— 2/15 个有
- `PreviewBridge` —— 2/15 个有
- `PreviewImage` —— 2/15 个有
- `QwenEditConfigPreparer` —— 2/15 个有
- `QwenEditOutputExtractor` —— 2/15 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 2/15 个有
- `UnetLoaderGGUF` —— 2/15 个有
- `easy float` —— 2/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 15 | 71% |
| 采样算法 | er_sde | - | 15 | 87% |
| 调度器 | beta | - | 15 | 87% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 832 | 15 | 0% |
| 高度 | 80 | 80 - 1536 | 15 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，15 个样本
- 采样算法 最常用 er_sde，15 个样本，一致性 87%
- 调度器 最常用 beta，15 个样本，一致性 87%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 832，15 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1536，15 个样本，取值分散，一致性仅 0%
- 高发问题（21/15 个样本）：Steps较低可能导致细节不足
