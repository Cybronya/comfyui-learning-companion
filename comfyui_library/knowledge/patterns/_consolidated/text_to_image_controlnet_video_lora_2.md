---
name: text_to_image_controlnet_video_lora_2
type: Text To Image
frequency: 3
level: strong
coverage: 0.622333
common_nodes: [Bjornulf_FreeVRAM, Bjornulf_ShowInt, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DownloadAndLoadGIMMVFIModel, DrawViTPose, EmptyLatentImage, Evaluate Integers, Fast Groups Muter (rgthree), FlashVSRNode, GIMMVFI_interpolate, GetNode, INTConstant, ImageConcanate, ImageFromBatch, ImageResizeKJv2, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, OnnxDetectionModelLoader, PoseAndFaceDetection, Primitive integer [Crystools], SetNode, UNETLoader, UnloadAllModels, VAEDecode, VAELoader, VHS_LoadVideo, VHS_LoadVideoPath, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy cleanGpuUsed, easy clearCacheAll, easy showAnything, easy sleep, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/48帧插帧高质量_WANAnimate长视频动作迁移更顺滑_2100198593348067330.json, 视频生成/图生视频/48帧插帧高质量_WANAnimate长视频动作迁移更顺滑_2101870653749161986.json, 视频生成/图生视频/48帧视频插帧_补帧 WANAnimate长视频动作迁移模仿_2113840995543633922.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_video_lora_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/48帧插帧高质量_WANAnimate长视频动作迁移更顺滑_2100198593348067330.json、视频生成/图生视频/48帧插帧高质量_WANAnimate长视频动作迁移更顺滑_2101870653749161986.json、视频生成/图生视频/48帧视频插帧_补帧 WANAnimate长视频动作迁移模仿_2113840995543633922.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 3 个 workflow 都包含：
- `Bjornulf_FreeVRAM`
- `Bjornulf_ShowInt`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DownloadAndLoadGIMMVFIModel`
- `DrawViTPose`
- `EmptyLatentImage`
- `Evaluate Integers`
- `Fast Groups Muter (rgthree)`
- `FlashVSRNode`
- `GIMMVFI_interpolate`
- `GetNode`
- `INTConstant`
- `ImageConcanate`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `Primitive integer [Crystools]`
- `SetNode`
- `UNETLoader`
- `UnloadAllModels`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_LoadVideoPath`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy showAnything`
- `easy sleep`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/3 个有
- `EmptyImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
