---
name: unknown_workflow_video_lora_sampler_156
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.626727
common_nodes: [CLIPVisionLoader, DrawViTPose, GetImageRangeFromBatch, ImageResizeKJv2, OnnxDetectionModelLoader, PoseAndFaceDetection, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSteadyDancerEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/真人视频转动漫风格_1996554877067214849.json, 视频生成/图生视频/SteadDancer动作迁移_1996568841872351234.json, 视频生成/图生视频/SteadDancer大模型：一键生成动物小猫小狗人物跳舞视频多人多动物同时跳舞多人舞蹈模仿_2011517668532162561.json, 视频生成/图生视频/SteadDancer真人视频转3D可爱风格_2064169491482894338.json, 视频生成/图生视频/动物跳舞_1997949647484256258.json, 视频生成/图生视频/图生视频 _ 专业舞蹈_ 自动姿态矫正 _ SteadyDancer_1996237432284651521.json, 视频生成/图生视频/真人视频真人转动漫风格 真人转动画视频3.0_2068694345024360450.json, 视频生成/图生视频/真人视频转3D可爱风格=SteadDancer=B站艾橘溪_1996110517959868418.json, 视频生成/图生视频/真人视频转3D可爱风格=SteadDancer，超丝滑顺畅！值得推荐_2037499475232559105.json, 视频生成/图生视频/真人视频转3D可爱风格=SteadDancer，超丝滑顺畅！值得推荐_2049292828706086913.json, 视频生成/图生视频/真人视频转动漫风格=SteadDancer_1996562415049383938.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_156

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/真人视频转动漫风格_1996554877067214849.json、视频生成/图生视频/SteadDancer动作迁移_1996568841872351234.json、视频生成/图生视频/SteadDancer大模型：一键生成动物小猫小狗人物跳舞视频多人多动物同时跳舞多人舞蹈模仿_2011517668532162561.json、视频生成/图生视频/SteadDancer真人视频转3D可爱风格_2064169491482894338.json、视频生成/图生视频/动物跳舞_1997949647484256258.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoBlockSwap`
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
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 10/11 个有
- `GetNode` —— 10/11 个有
- `JWInteger` —— 10/11 个有
- `SetNode` —— 10/11 个有
- `LayerUtility: PurgeVRAM` —— 9/11 个有
- `PrimitiveInt` —— 9/11 个有
- `SimpleMath+` —— 9/11 个有
- `ttN float` —— 9/11 个有
- `CheckpointLoaderSimple` —— 8/11 个有
- `EmptyLatentImage` —— 8/11 个有
- `KSampler` —— 8/11 个有
- `TextEncodeQwenImageEditPlus` —— 8/11 个有
- `VAEDecode` —— 8/11 个有
- `WanVideoTorchCompileSettings` —— 8/11 个有
- `ImageFromBatch+` —— 7/11 个有
- `JjkText` —— 7/11 个有
- `LoraLoaderModelOnly` —— 7/11 个有
- `SaveImage` —— 7/11 个有
- `ImageConcatMulti` —— 6/11 个有
- `LoadImage` —— 4/11 个有
- `Text` —— 4/11 个有
- `Text Concatenate` —— 4/11 个有
- `Text Multiline` —— 4/11 个有
- `easy anythingIndexSwitch` —— 4/11 个有
- `DF_Int_to_Float` —— 1/11 个有
- `INTConstant` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `TT_img_enc` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 720 - 768 | 8 | 98% |
| 高度 | 1280 | 768 - 1280 | 8 | 86% |
| 采样步数 | 8 | 8 - 8 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 720 - 768，8 个样本，取值集中（一致性 98%）
- 高度 中位数 1280，观测区间 768 - 1280，8 个样本，取值集中（一致性 86%）
- 采样步数 中位数 8，观测区间 8 - 8，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/11 个样本）：Steps较低可能导致细节不足
