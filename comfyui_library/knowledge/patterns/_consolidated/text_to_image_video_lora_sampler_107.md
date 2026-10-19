---
name: text_to_image_video_lora_sampler_107
type: Text To Image
frequency: 7
level: strong
coverage: 0.738714
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, EmptyLatentImage, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJv2, Int, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, OnnxDetectionModelLoader, PreviewImage, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSteadyDancerEmbeds, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoScheduler, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/SteadDancer动作迁移2.0_支持动漫人物一致性加强10秒以上_2109098445825990657.json, 视频生成/图生视频/SteadyDancer一键生成小猫小狗人物跳舞视频多人跳舞骨骼迁移不限时长_2106157070495080450.json, 视频生成/图生视频/SteadyDancer动作迁移不限时长 单人跳舞表情复刻视频生成_2104767103415963649.json, 视频生成/图生视频/SteadyDancer动作迁移不限时长版｜表情复刻单人跳舞，舞姿神还原_2107334075940958210.json, 视频生成/图生视频/SteadyDancer单人跳舞动作迁移｜不限时长版表情复刻，视频生视频_2104525759527350274.json, 视频生成/图生视频/SteadyDancer骨骼迁移不限时长｜单人跳舞动物跳舞动作生成_2096710822365057025.json, 视频生成/图生视频/SteadyDancer骨骼迁移跳舞视频｜小猫小狗多人不限时长_2105832688631508994.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_107

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/SteadDancer动作迁移2.0_支持动漫人物一致性加强10秒以上_2109098445825990657.json、视频生成/图生视频/SteadyDancer一键生成小猫小狗人物跳舞视频多人跳舞骨骼迁移不限时长_2106157070495080450.json、视频生成/图生视频/SteadyDancer动作迁移不限时长 单人跳舞表情复刻视频生成_2104767103415963649.json、视频生成/图生视频/SteadyDancer动作迁移不限时长版｜表情复刻单人跳舞，舞姿神还原_2107334075940958210.json、视频生成/图生视频/SteadyDancer单人跳舞动作迁移｜不限时长版表情复刻，视频生视频_2104525759527350274.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `EmptyLatentImage`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `Int`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `OnnxDetectionModelLoader`
- `PreviewImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerFromSettings`
- `WanVideoSamplerSettings`
- `WanVideoScheduler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PoseDetectionOneToAllAnimation` —— 6/7 个有
- `TextInput_` —— 6/7 个有
- `孤海注释` —— 6/7 个有
- `SaveImage` —— 2/7 个有
- `DF_Int_to_Float` —— 1/7 个有
- `DrawViTPose` —— 1/7 个有
- `EmptyImage` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `PoseAndFaceDetection` —— 1/7 个有
- `RH_Sora2_I2V` —— 1/7 个有
- `Text` —— 1/7 个有
- `WanVideoBlockSwap` —— 1/7 个有
- `WanVideoSetBlockSwap` —— 1/7 个有
- `WanVideoTorchCompileSettings` —— 1/7 个有
- `easy setNode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
