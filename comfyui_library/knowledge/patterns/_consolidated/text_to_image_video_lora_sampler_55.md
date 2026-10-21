---
name: text_to_image_video_lora_sampler_55
type: Text To Image
frequency: 12
level: weak
coverage: 0.620583
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DrawViTPose, EmptyLatentImage, ImageBatch, ImageFromBatch, ImageResizeKJv2, KSampler, LoraLoaderModelOnly, OnnxDetectionModelLoader, PoseAndFaceDetection, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1_1复刻高精细动作模仿｜动作迁移角色一致性图生视频_2091661066261590018.json, 视频生成/图生视频/4段变装灵活分段动作迁移 服装替换人脸替换视频换脸神器_2110585129834991617.json, 视频生成/图生视频/WanAnimate动作迁移高动态首选 视频人物动作复刻图生视频方案_2094348299632467969.json, 视频生成/图生视频/WanAnimate升级版 动作迁移全程画面不变色_2096743688486612993.json, 视频生成/图生视频/WanAnimate高动态首选 大幅度动作迁移也能稳稳复刻_2095079205926170625.json, 视频生成/图生视频/WanAnimate高动态首选 大幅度动作迁移也能稳稳复刻_2106522225347223554.json, 视频生成/图生视频/Zimage 生图生视频 角色替换-视频换人 人物跳舞(标清版)支持33秒_2083733748604030977.json, 视频生成/图生视频/2072921867442278402.json, 视频生成/图生视频/动作迁移可抖X版｜爆款视频动作轻松搬运复用_2098714470225899522.json, 视频生成/图生视频/动作迁移支持抖音平台 图生视频人物动态精准跟随_2098474317028880385.json, 视频生成/图生视频/动作高仿一键迁移｜高显存风格迁移图生视频生成_2091807774530424833.json, 视频生成/图生视频/2038614574705938433.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_55

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/1_1复刻高精细动作模仿｜动作迁移角色一致性图生视频_2091661066261590018.json、视频生成/图生视频/4段变装灵活分段动作迁移 服装替换人脸替换视频换脸神器_2110585129834991617.json、视频生成/图生视频/WanAnimate动作迁移高动态首选 视频人物动作复刻图生视频方案_2094348299632467969.json、视频生成/图生视频/WanAnimate升级版 动作迁移全程画面不变色_2096743688486612993.json、视频生成/图生视频/WanAnimate高动态首选 大幅度动作迁移也能稳稳复刻_2095079205926170625.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：62%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DrawViTPose`
- `EmptyLatentImage`
- `ImageBatch`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `KSampler`
- `LoraLoaderModelOnly`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BatchCount+` —— 11/12 个有
- `GetNode` —— 11/12 个有
- `PreviewImage` —— 11/12 个有
- `RHHiddenNodes` —— 11/12 个有
- `RepeatImageBatch` —— 11/12 个有
- `SetNode` —— 11/12 个有
- `VHS_VideoInfo` —— 11/12 个有
- `VRAMReserver` —— 11/12 个有
- `WanVideoContextOptions` —— 11/12 个有
- `easy mathInt` —— 11/12 个有
- `easy float` —— 10/12 个有
- `JjkText` —— 9/12 个有
- `LoadImage` —— 9/12 个有
- `MemoryCleaner` —— 9/12 个有
- `solarL_SaveImagesToZip` —— 9/12 个有
- `easy showAnything` —— 8/12 个有
- `孤海注释` —— 8/12 个有
- `DownloadAndLoadNLFModel` —— 6/12 个有
- `Int` —— 6/12 个有
- `LazySwitch1way` —— 6/12 个有
- `NLFPredict` —— 6/12 个有
- `PoseDetectionVitPoseToDWPose` —— 6/12 个有
- `RenderNLFPoses` —— 6/12 个有
- `SDPoseOODLoader` —— 6/12 个有
- `SDPoseOODProcessor` —— 6/12 个有
- `WanVideoLoraSelect` —— 6/12 个有
- `YOLOModelLoader` —— 6/12 个有
- `easy anythingIndexSwitch` —— 6/12 个有
- `easy boolean` —— 6/12 个有
- `easy int` —— 6/12 个有
- `easy cleanGpuUsed` —— 5/12 个有
- `CR Text` —— 3/12 个有
- `FastFilmGrain` —— 3/12 个有
- `INTConstant` —— 3/12 个有
- `Image Comparer (rgthree)` —— 3/12 个有
- `ImageScaleToTotalPixels` —— 3/12 个有
- `LayerColor: BrightnessContrastV2` —— 3/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/12 个有
- `LayerUtility: PurgeVRAM` —— 3/12 个有
- `Pick From Batch (mtb)` —— 3/12 个有
- `Qwen3_VQA` —— 3/12 个有
- `SaveImage` —— 3/12 个有
- `SeedVR2LoadDiTModel` —— 3/12 个有
- `SeedVR2LoadVAEModel` —— 3/12 个有
- `SeedVR2VideoUpscaler` —— 3/12 个有
- `SimpleMath+` —— 2/12 个有
- `Fast Groups Bypasser (rgthree)` —— 1/12 个有
- `Float` —— 1/12 个有
- `GetImageSizeAndCount` —— 1/12 个有
- `Primitive integer [Crystools]` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 12 | 65% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 12 | 58% |
| 采样算法 | er_sde | - | 12 | 75% |
| 调度器 | beta | - | 12 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 1080 | 12 | 0% |
| 高度 | 80 | 80 - 1920 | 12 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，12 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，12 个样本
- 采样算法 最常用 er_sde，12 个样本，一致性 75%
- 调度器 最常用 beta，12 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1080，12 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，12 个样本，取值分散，一致性仅 0%
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
