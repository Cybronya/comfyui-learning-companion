---
name: text_to_image_video_lora_sampler_30
type: Text To Image
frequency: 20
level: weak
coverage: 0.9174
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DrawViTPose, EmptyLatentImage, GetImageRangeFromBatch, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, OnnxDetectionModelLoader, PathchSageAttentionKJ, PoseAndFaceDetection, SimpleMath+, SimpleMathDual+, TorchCompileModelWanVideoV2, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanAnimateToVideo, easy batchAnything, easy boolean, easy compare, easy convertAnything, easy ifElse, easy int, easy lengthAnything, easy positive, easy promptReplace, easy whileLoopEnd, easy whileLoopStart, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/动作迁移升级版来袭｜表情舞蹈动作复刻不限时长图生视频_2103669913457090562.json, 图片生成/图生图/动作迁移升级版表情舞蹈模仿动作复刻，不限时长图生视频方案_2104050288033353729.json, 图片生成/图生图/王炸动作迁移工作流｜参考视频动作一键复刻_2098713275579060225.json, 平台全量/动作迁移升级版｜表情舞蹈模仿动作复刻 不限时长图生视频_2099874594667720706.json, 视频生成/图生视频/Comfy官版WanAnimate 动作迁移支持运镜采样无缝循环_2096736812248166401.json, 视频生成/图生视频/Comfy官版WanAnimate 动作迁移支持运镜采样无缝循环_2098645150116438017.json, 视频生成/图生视频/Wan2.2结合Animate动作迁移 视频人物运动复刻修复黑屏_2098627308616773633.json, 视频生成/图生视频/动作迁移升级版加表情动作不限时长，舞蹈模仿各种动作复刻图生视频_2103929374503424002.json, 视频生成/图生视频/动作迁移升级版加表情动作不限时长，舞蹈模仿各种动作复刻图生视频方案_2103608874556289026.json, 视频生成/图生视频/动作迁移升级版舞蹈模仿 表情复刻不限时长图生视频处理工具_2112998111990865922.json, 视频生成/图生视频/动作迁移升级版｜表情舞蹈模仿动作复刻 不限时长图生视频_2097562494444335106.json, 视频生成/图生视频/动作迁移精细版_面部表情加精细姿势，视频生视频可选高清_2111206681580494849.json, 视频生成/图生视频/动作迁移精细版上线｜面部表情精细姿势超抖X高清可选_2111079225896820737.json, 视频生成/图生视频/动作迁移精细版二发布｜超抖X表情姿势可选高清输出_2111092213093588993.json, 视频生成/图生视频/动作迁移精细版｜面部表情精细姿势超抖高清可选_2094885882292686849.json, 视频生成/图生视频/精细动作迁移可选高清，面部表情视频生视频方案_2111262550280200193.json, 视频生成/图生视频/老Y视频换衣_2053103096611524610.json, 视频生成/图生视频/视频复刻升级版｜表情动作全保留图生视频同款跟拍_2101567713368952833.json, 视频生成/图生视频/视频换装视频换衣_2040663476045094914.json, 视频生成/图生视频/面部表情+精细姿势超抖X｜动作迁移精细版可选高清_2095084093120798722.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_30

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/动作迁移升级版来袭｜表情舞蹈动作复刻不限时长图生视频_2103669913457090562.json、图片生成/图生图/动作迁移升级版表情舞蹈模仿动作复刻，不限时长图生视频方案_2104050288033353729.json、图片生成/图生图/王炸动作迁移工作流｜参考视频动作一键复刻_2098713275579060225.json、平台全量/动作迁移升级版｜表情舞蹈模仿动作复刻 不限时长图生视频_2099874594667720706.json、视频生成/图生视频/Comfy官版WanAnimate 动作迁移支持运镜采样无缝循环_2096736812248166401.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 20 个 workflow 都包含：
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
- `GetImageSize` —— 18/20 个有
- `ImageResizeKJv2` —— 18/20 个有
- `JjkText` —— 18/20 个有
- `MathExpression|pysssss` —— 18/20 个有
- `SaveVideoRGBA` —— 18/20 个有
- `solarL_SaveImagesToZip` —— 18/20 个有
- `孤海注释` —— 18/20 个有
- `Int` —— 16/20 个有
- `RHHiddenNodes` —— 16/20 个有
- `BlockifyMask` —— 14/20 个有
- `DownloadAndLoadSAM2Model` —— 14/20 个有
- `DrawMaskOnImage` —— 14/20 个有
- `Fast Groups Muter (rgthree)` —— 14/20 个有
- `FlashVSRNode` —— 14/20 个有
- `GrowMask` —— 14/20 个有
- `LayerUtility: ImageBlend` —— 14/20 个有
- `PointsEditor` —— 14/20 个有
- `Sam2Segmentation` —— 14/20 个有
- `Seed` —— 14/20 个有
- `ImageConcatMulti` —— 12/20 个有
- `SaveImage` —— 7/20 个有
- `AILab_QwenVL` —— 2/20 个有
- `CFGNorm` —— 2/20 个有
- `ConditioningZeroOut` —— 2/20 个有
- `CropWithPadInfo` —— 2/20 个有
- `FirstFrameSelector` —— 2/20 个有
- `FluxGuidance` —— 2/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/20 个有
- `MemoryCleaner` —— 2/20 个有
- `PreviewBridge` —— 2/20 个有
- `PreviewImage` —— 2/20 个有
- `QwenEditConfigPreparer` —— 2/20 个有
- `QwenEditOutputExtractor` —— 2/20 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 2/20 个有
- `UnetLoaderGGUF` —— 2/20 个有
- `easy float` —— 2/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 832 | 20 | 0% |
| 高度 | 80 | 80 - 1536 | 20 | 0% |
| 采样步数 | 4 | 4 - 4 | 20 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 20 | 75% |
| 采样算法 | er_sde | - | 20 | 90% |
| 调度器 | beta | - | 20 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 29/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 832，20 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1536，20 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，20 个样本
- 采样算法 最常用 er_sde，20 个样本，一致性 90%
- 调度器 最常用 beta，20 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（29/20 个样本）：Steps较低可能导致细节不足
