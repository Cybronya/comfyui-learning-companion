---
name: text_to_image_video_lora_sampler_111
type: Text To Image
frequency: 8
level: weak
coverage: 0.561875
common_nodes: [BatchCount+, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DownloadAndLoadNLFModel, DrawViTPose, EmptyLatentImage, GetNode, ImageBatch, ImageFromBatch, ImageResizeKJv2, KSampler, LazySwitch1way, LoraLoaderModelOnly, MemoryCleaner, NLFPredict, OnnxDetectionModelLoader, PoseAndFaceDetection, PoseDetectionVitPoseToDWPose, PreviewImage, RHHiddenNodes, RenderNLFPoses, RepeatImageBatch, SDPoseOODLoader, SDPoseOODProcessor, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, VRAMReserver, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, YOLOModelLoader, easy anythingIndexSwitch, easy boolean, easy float, easy int, easy mathInt]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/24G显存运行无需参考图 人物跳舞(标清版)支持33秒_2043951353009020930.json, 平台全量/啊癫  26年最新无需垫图 人物跳舞动作迁移 人物跳舞 （标清版） 支持33秒  仅需24G显存运行_2038786959178469378.json, 视频生成/图生视频/WanAnimate动作迁移高动态首选 视频人物动作复刻图生视频方案_2094348299632467969.json, 视频生成/图生视频/WanAnimate高动态首选 大幅度动作迁移也能稳稳复刻_2095079205926170625.json, 视频生成/图生视频/WanAnimate高动态首选 大幅度动作迁移也能稳稳复刻_2106522225347223554.json, 视频生成/图生视频/Zimage 生图生视频 角色替换-视频换人 人物跳舞(标清版)支持33秒_2083733748604030977.json, 视频生成/图生视频/Zimage洗图 +图生视频动作模仿 动作迁移 人物替换   真实自然 人物跳舞 支持33秒 +_2072921867442278402.json, 视频生成/图生视频/啊癫  26年最新 无需垫图 人物跳舞动作迁移 人物跳舞 （高清版） 支持33秒  需48G显存运行_2038614574705938433.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_111

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/24G显存运行无需参考图 人物跳舞(标清版)支持33秒_2043951353009020930.json、平台全量/啊癫  26年最新无需垫图 人物跳舞动作迁移 人物跳舞 （标清版） 支持33秒  仅需24G显存运行_2038786959178469378.json、视频生成/图生视频/WanAnimate动作迁移高动态首选 视频人物动作复刻图生视频方案_2094348299632467969.json、视频生成/图生视频/WanAnimate高动态首选 大幅度动作迁移也能稳稳复刻_2095079205926170625.json、视频生成/图生视频/WanAnimate高动态首选 大幅度动作迁移也能稳稳复刻_2106522225347223554.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 8 个 workflow 都包含：
- `BatchCount+`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DownloadAndLoadNLFModel`
- `DrawViTPose`
- `EmptyLatentImage`
- `GetNode`
- `ImageBatch`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `KSampler`
- `LazySwitch1way`
- `LoraLoaderModelOnly`
- `MemoryCleaner`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PoseDetectionVitPoseToDWPose`
- `PreviewImage`
- `RHHiddenNodes`
- `RenderNLFPoses`
- `RepeatImageBatch`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `VRAMReserver`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `YOLOModelLoader`
- `easy anythingIndexSwitch`
- `easy boolean`
- `easy float`
- `easy int`
- `easy mathInt`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 5/8 个有
- `FastFilmGrain` —— 5/8 个有
- `INTConstant` —— 5/8 个有
- `Image Comparer (rgthree)` —— 5/8 个有
- `ImageScaleToTotalPixels` —— 5/8 个有
- `LayerColor: BrightnessContrastV2` —— 5/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/8 个有
- `LayerUtility: PurgeVRAM` —— 5/8 个有
- `Pick From Batch (mtb)` —— 5/8 个有
- `Qwen3_VQA` —— 5/8 个有
- `SeedVR2LoadDiTModel` —— 5/8 个有
- `SeedVR2LoadVAEModel` —— 5/8 个有
- `SeedVR2VideoUpscaler` —— 5/8 个有
- `easy showAnything` —— 5/8 个有
- `LoadImage` —— 4/8 个有
- `JjkText` —— 3/8 个有
- `SaveImage` —— 3/8 个有
- `solarL_SaveImagesToZip` —— 3/8 个有
- `孤海注释` —— 3/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 80 - 1080 | 8 | 31% |
| 高度 | 1920 | 80 - 1920 | 8 | 28% |
| 采样步数 | 8 | 4 - 8 | 8 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 8 | 27% |
| 采样算法 | res_2s | - | 8 | 62% |
| 调度器 | bong_tangent | - | 8 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 80 - 1080，8 个样本，取值分散，一致性仅 31%
- 高度 中位数 1920，观测区间 80 - 1920，8 个样本，取值分散，一致性仅 28%
- 采样步数 中位数 8，观测区间 4 - 8，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，8 个样本，取值分散，一致性仅 27%
- 采样算法 最常用 res_2s，8 个样本，一致性 62%
- 调度器 最常用 bong_tangent，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
