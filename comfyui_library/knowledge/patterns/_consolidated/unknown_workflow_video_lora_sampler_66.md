---
name: unknown_workflow_video_lora_sampler_66
type: Unknown Workflow
frequency: 22
level: strong
coverage: 0.605864
common_nodes: [CLIPVisionLoader, DrawViTPose, GetImageRangeFromBatch, ImageResizeKJv2, JWInteger, OnnxDetectionModelLoader, PoseAndFaceDetection, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSteadyDancerEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/真人视频转动漫风格_1996554877067214849.json, 平台全量/SteadDancer真人视频转3D可爱风格_2052211983528800257.json, 平台全量/SteadDancer真人视频转3D可爱风格_2053721045252755458.json, 平台全量/SteadDancer真人视频转3D可爱风格_2054848884299575297.json, 平台全量/SteadDancer真人视频转3D可爱风格生成器_2052605547270160386.json, 平台全量/SteadDancer真人视频转3D可爱风格生成器_2053345944376233986.json, 平台全量/SteadDancer真人视频转3D可爱风格生成器_2075915693840748545.json, 平台全量/SteadDancer真人视频转动漫可爱风格-单人跳舞双人跳舞转动漫 可自定义风格_2056333105170051074.json, 平台全量/SteadDancer真人视频转动漫可爱风格_2056276568628092929.json, 平台全量/SteadDancer真人视频转动漫可爱风格_2057028068287541249.json, 平台全量/真人视频转动漫可爱风格（9中风格）_2060954431281262593.json, 平台全量/真人视频转动漫风格=SteadDancer_2083922678012006401.json, 平台全量/超好用🔥真人视频转动漫可爱风格-多种动漫风格按需自选_2056605890484203521.json, 视频生成/图生视频/SteadDancer大模型：一键生成动物小猫小狗人物跳舞视频多人多动物同时跳舞多人舞蹈模仿_2011517668532162561.json, 视频生成/图生视频/SteadDancer真人视频转3D可爱风格_2064169491482894338.json, 视频生成/图生视频/动物跳舞_1997949647484256258.json, 视频生成/图生视频/图生视频 _ 专业舞蹈_ 自动姿态矫正 _ SteadyDancer_1996237432284651521.json, 视频生成/图生视频/真人视频真人转动漫风格 真人转动画视频3.0_2068694345024360450.json, 视频生成/图生视频/真人视频转3D可爱风格=SteadDancer=B站艾橘溪_1996110517959868418.json, 视频生成/图生视频/真人视频转3D可爱风格=SteadDancer，超丝滑顺畅！值得推荐_2037499475232559105.json, 视频生成/图生视频/真人视频转3D可爱风格=SteadDancer，超丝滑顺畅！值得推荐_2049292828706086913.json, 视频生成/图生视频/真人视频转动漫风格=SteadDancer_1996562415049383938.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_66

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/图生图/真人视频转动漫风格_1996554877067214849.json、平台全量/SteadDancer真人视频转3D可爱风格_2052211983528800257.json、平台全量/SteadDancer真人视频转3D可爱风格_2053721045252755458.json、平台全量/SteadDancer真人视频转3D可爱风格_2054848884299575297.json、平台全量/SteadDancer真人视频转3D可爱风格生成器_2052605547270160386.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 22 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `JWInteger`
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
- `GetImageSizeAndCount` —— 21/22 个有
- `GetNode` —— 21/22 个有
- `LayerUtility: PurgeVRAM` —— 21/22 个有
- `PrimitiveInt` —— 21/22 个有
- `SetNode` —— 21/22 个有
- `SimpleMath+` —— 21/22 个有
- `ttN float` —— 21/22 个有
- `CheckpointLoaderSimple` —— 20/22 个有
- `EmptyLatentImage` —— 20/22 个有
- `KSampler` —— 20/22 个有
- `TextEncodeQwenImageEditPlus` —— 20/22 个有
- `VAEDecode` —— 20/22 个有
- `ImageFromBatch+` —— 19/22 个有
- `JjkText` —— 19/22 个有
- `LoraLoaderModelOnly` —— 19/22 个有
- `SaveImage` —— 19/22 个有
- `WanVideoTorchCompileSettings` —— 19/22 个有
- `ImageConcatMulti` —— 16/22 个有
- `Text` —— 15/22 个有
- `Text Concatenate` —— 15/22 个有
- `Text Multiline` —— 15/22 个有
- `easy anythingIndexSwitch` —— 15/22 个有
- `LoadImage` —— 3/22 个有
- `DF_Int_to_Float` —— 1/22 个有
- `PreviewImage` —— 1/22 个有
- `TT_img_enc` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 720 - 768 | 20 | 99% |
| 高度 | 1280 | 768 - 1280 | 20 | 91% |
| 采样步数 | 8 | 8 - 8 | 20 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 20 | 100% |
| 采样算法 | euler | - | 20 | 95% |
| 调度器 | simple | - | 20 | 95% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 720 - 768，20 个样本，取值集中（一致性 99%）
- 高度 中位数 1280，观测区间 768 - 1280，20 个样本，取值集中（一致性 91%）
- 采样步数 中位数 8，观测区间 8 - 8，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，20 个样本，一致性 95%
- 调度器 最常用 simple，20 个样本，一致性 95%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（20/22 个样本）：Steps较低可能导致细节不足
