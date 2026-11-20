---
name: text_to_image_video_lora_sampler_47
type: Text To Image
frequency: 15
level: weak
coverage: 0.632933
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DrawViTPose, EmptyLatentImage, ImageBatch, ImageFromBatch, ImageResizeKJv2, KSampler, LoraLoaderModelOnly, OnnxDetectionModelLoader, PoseAndFaceDetection, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/动作迁移动作一致性加强版｜表情手部抖动全需要plus_2112938055853240322.json, 图片生成/图生图/动作高仿一键迁移｜高显存角色一致性风格迁移生成_2091825884121616386.json, 图片生成/图生图/高仿级动作迁移复刻神器｜动作细节高度还原｜高显存配置直出_2113101434249105410.json, 视频生成/图生视频/1_1复刻高精细动作模仿｜动作迁移角色一致性图生视频_2091661066261590018.json, 视频生成/图生视频/1_1高精细动作模仿复刻｜plus增强动作迁移｜视频风格转换输出_2113107225316257793.json, 视频生成/图生视频/4段变装灵活分段动作迁移 服装替换人脸替换视频换脸神器_2110585129834991617.json, 视频生成/图生视频/Animate动作迁移极速版｜自动尺寸一键复刻跳舞视频_2105129829493465090.json, 视频生成/图生视频/Animate极速动作迁移｜复刻跳舞自动适配视频尺寸_2105224763630243842.json, 视频生成/图生视频/WanAnimate动作迁移高动态首选 视频人物动作复刻图生视频方案_2094348299632467969.json, 视频生成/图生视频/WanAnimate升级版 动作迁移全程画面不变色_2096743688486612993.json, 视频生成/图生视频/WanAnimate高动态首选 大幅度动作迁移也能稳稳复刻_2095079205926170625.json, 视频生成/图生视频/WanAnimate高动态首选 大幅度动作迁移也能稳稳复刻_2106522225347223554.json, 视频生成/图生视频/Zimage 生图生视频 角色替换-视频换人 人物跳舞(标清版)支持33秒_2083733748604030977.json, 视频生成/图生视频/Zimage洗图 +图生视频动作模仿 动作迁移 人物替换   真实自然 人物跳舞 支持33秒 +_2072921867442278402.json, 视频生成/图生视频/啊癫  26年最新 无需垫图 人物跳舞动作迁移 人物跳舞 （高清版） 支持33秒  需48G显存运行_2038614574705938433.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_47

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/动作迁移动作一致性加强版｜表情手部抖动全需要plus_2112938055853240322.json、图片生成/图生图/动作高仿一键迁移｜高显存角色一致性风格迁移生成_2091825884121616386.json、图片生成/图生图/高仿级动作迁移复刻神器｜动作细节高度还原｜高显存配置直出_2113101434249105410.json、视频生成/图生视频/1_1复刻高精细动作模仿｜动作迁移角色一致性图生视频_2091661066261590018.json、视频生成/图生视频/1_1高精细动作模仿复刻｜plus增强动作迁移｜视频风格转换输出_2113107225316257793.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：63%

## 共有节点

全部 15 个 workflow 都包含：
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
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BatchCount+` —— 14/15 个有
- `GetNode` —— 14/15 个有
- `RHHiddenNodes` —— 14/15 个有
- `RepeatImageBatch` —— 14/15 个有
- `SetNode` —— 14/15 个有
- `VHS_VideoInfo` —— 14/15 个有
- `WanVideoContextOptions` —— 14/15 个有
- `easy mathInt` —— 14/15 个有
- `WanVideoBlockSwap` —— 13/15 个有
- `WanVideoSetBlockSwap` —— 13/15 个有
- `easy float` —— 13/15 个有
- `JjkText` —— 12/15 个有
- `LoadImage` —— 12/15 个有
- `MemoryCleaner` —— 12/15 个有
- `PreviewImage` —— 12/15 个有
- `VRAMReserver` —— 12/15 个有
- `solarL_SaveImagesToZip` —— 12/15 个有
- `孤海注释` —— 11/15 个有
- `easy showAnything` —— 9/15 个有
- `LazySwitch1way` —— 8/15 个有
- `easy boolean` —— 8/15 个有
- `easy cleanGpuUsed` —— 8/15 个有
- `easy int` —— 8/15 个有
- `Int` —— 7/15 个有
- `WanVideoLoraSelect` —— 7/15 个有
- `DownloadAndLoadNLFModel` —— 6/15 个有
- `NLFPredict` —— 6/15 个有
- `PoseDetectionVitPoseToDWPose` —— 6/15 个有
- `RenderNLFPoses` —— 6/15 个有
- `SDPoseOODLoader` —— 6/15 个有
- `SDPoseOODProcessor` —— 6/15 个有
- `YOLOModelLoader` —— 6/15 个有
- `easy anythingIndexSwitch` —— 6/15 个有
- `CR Text` —— 5/15 个有
- `ImageScaleToTotalPixels` —— 5/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/15 个有
- `SimpleMath+` —— 4/15 个有
- `FastFilmGrain` —— 3/15 个有
- `INTConstant` —— 3/15 个有
- `Image Comparer (rgthree)` —— 3/15 个有
- `LayerColor: BrightnessContrastV2` —— 3/15 个有
- `LayerUtility: PurgeVRAM` —— 3/15 个有
- `Pick From Batch (mtb)` —— 3/15 个有
- `Qwen3_VQA` —— 3/15 个有
- `SeedVR2LoadDiTModel` —— 3/15 个有
- `SeedVR2LoadVAEModel` —— 3/15 个有
- `SeedVR2VideoUpscaler` —— 3/15 个有
- `LayerUtility: ColorImage V2` —— 2/15 个有
- `LazySwitch2way` —— 2/15 个有
- `Primitive integer [Crystools]` —— 2/15 个有
- `SaveImage` —— 2/15 个有
- `easy compare` —— 2/15 个有
- `easy imageSize` —— 2/15 个有
- `Fast Groups Bypasser (rgthree)` —— 1/15 个有
- `Float` —— 1/15 个有
- `GetImageSizeAndCount` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1080 | 15 | 0% |
| 高度 | 80 | 80 - 1920 | 15 | 0% |
| 采样步数 | 4 | 4 - 8 | 15 | 67% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 15 | 63% |
| 采样算法 | er_sde | - | 15 | 80% |
| 调度器 | beta | - | 15 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1080，15 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，15 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 8，15 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，15 个样本
- 采样算法 最常用 er_sde，15 个样本，一致性 80%
- 调度器 最常用 beta，15 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
