---
name: text_to_image_video_lora_sampler_147
type: Text To Image
frequency: 4
level: strong
coverage: 0.7935
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DWPreprocessor, EmptyLatentImage, FaceMaskFromPoseKeypoints, GetNode, ImageCropByMaskAndResize, ImageResizeKJv2, JWInteger, JjkText, KSampler, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, PixelPerfectResolution, PrimitiveInt, SetNode, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/AI动作模仿唱歌跳舞对口型｜AnimateWan2.2图生视频生成_2097085659403087873.json, 视频生成/图生视频/Animate Wan2.2视频换脸换头视频生视频处理工具_2101775798649835522.json, 视频生成/图生视频/AnimateWan2.2动作模仿｜唱歌跳舞对口型一键生成_2095105299878338562.json, 视频生成/图生视频/AnimateWan2.2动作模仿｜唱歌跳舞对口型生成_2094924434271461377.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_147

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/AI动作模仿唱歌跳舞对口型｜AnimateWan2.2图生视频生成_2097085659403087873.json、视频生成/图生视频/Animate Wan2.2视频换脸换头视频生视频处理工具_2101775798649835522.json、视频生成/图生视频/AnimateWan2.2动作模仿｜唱歌跳舞对口型一键生成_2095105299878338562.json、视频生成/图生视频/AnimateWan2.2动作模仿｜唱歌跳舞对口型生成_2094924434271461377.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `EmptyLatentImage`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `JWInteger`
- `JjkText`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PixelPerfectResolution`
- `PrimitiveInt`
- `SetNode`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
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
- `easy cleanGpuUsed`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ImageFromBatch` —— 3/4 个有
- `Text` —— 3/4 个有
- `ttN float` —— 3/4 个有
- `SaveImage` —— 2/4 个有
- `Audio Duration (mtb)` —— 1/4 个有
- `BlockifyMask` —— 1/4 个有
- `CM_IntToFloat` —— 1/4 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/4 个有
- `DrawMaskOnImage` —— 1/4 个有
- `GIMMVFI_interpolate` —— 1/4 个有
- `GetImageRangeFromBatch` —— 1/4 个有
- `GetImageSizeAndCount` —— 1/4 个有
- `GrowMask` —— 1/4 个有
- `ImageFromBatch+` —— 1/4 个有
- `Int` —— 1/4 个有
- `TextOverlay` —— 1/4 个有
- `easy sam3ModelLoader` —— 1/4 个有
- `easy sam3VideoSegmentation` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
