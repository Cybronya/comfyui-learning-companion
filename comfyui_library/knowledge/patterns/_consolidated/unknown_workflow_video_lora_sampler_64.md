---
name: unknown_workflow_video_lora_sampler_64
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.7895
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [数字人/数字人/MultiTalk数字人唱歌-16G可玩_1942781589854031873.json, 数字人/数字人/MultiTalk数字人唱歌-16G可玩（优化版本）_1942816414530998274.json, 数字人/数字人/aiMVClip应用版_1985609275160645633.json, 数字人/数字人/稳定质量Multitalk--最新最强数字人_1936158876121337857.json, 视频生成/图生视频/MultiTalk 单人脱口秀｜KJ加速版_1936701399797501953.json, 视频生成/图生视频/MultiTalk+AniWan单人KJ高质量加速稳定版V4（UNI3C运镜-脸部稳定版）_1948784661829492737.json, 视频生成/图生视频/MultiTalk+AniWan单人KJ（UNI3C运镜 手持） 浮云 测试版_1998945387329282050.json, 视频生成/图生视频/MultiTalk+AniWan单人KJ（UNI3C运镜 手持） 浮云_1998778583533412354.json, 视频生成/图生视频/MultiTalk+Aniwan单人KJ高质量加速稳定版V4（脸部一致性版）_1948782335715094529.json, 视频生成/图生视频/MultiTalk+UNI3C运镜_1986856996743876610.json, 视频生成/图生视频/MultiTalk_图生视频_1936815365949149186.json, 视频生成/图生视频/MultiTalk单人KJ高质量加速稳定版(无clipvision版)_1936345879362310145.json, 视频生成/图生视频/MultiTalk单人KJ高质量加速稳定版V2（大幅度增加时长）_1936304565509607426.json, 视频生成/图生视频/MultiTalk单人KJ高质量加速稳定版（UNI3C运镜版）_1936341490123837441.json, 视频生成/图生视频/MultiTalk数字人口播单人版_1940606353897402370.json, 视频生成/图生视频/MultiTalk最强数字人插件16G可玩，音频+图片=王炸数字人_1937864518498455553.json, 视频生成/图生视频/Multitalk+aniwan数字人，可说话演讲可唱歌_1940356622893953026.json, 视频生成/图生视频/Multitalk数字人（极速版）_1937674986381295618.json, 视频生成/图生视频/ani ③-Multitalk数字人_1945034637402099713.json, 音频生成/音频生成/Multitalk+aniwan数字人，可说话演讲可唱歌_1949746352932741121.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_64

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（数字人/数字人/MultiTalk数字人唱歌-16G可玩_1942781589854031873.json、数字人/数字人/MultiTalk数字人唱歌-16G可玩（优化版本）_1942816414530998274.json、数字人/数字人/aiMVClip应用版_1985609275160645633.json、数字人/数字人/稳定质量Multitalk--最新最强数字人_1936158876121337857.json、视频生成/图生视频/MultiTalk 单人脱口秀｜KJ加速版_1936701399797501953.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 20 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 19/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 19/20 个有
- `PrimitiveFloat` —— 19/20 个有
- `TextInput_` —— 19/20 个有
- `WanVideoClipVisionEncode` —— 19/20 个有
- `LayerUtility: PurgeVRAM` —— 18/20 个有
- `JWIntegerToString` —— 17/20 个有
- `easy showAnything` —— 17/20 个有
- `JWInteger` —— 16/20 个有
- `PrimitiveInt` —— 14/20 个有
- `VHS_LoadVideo` —— 7/20 个有
- `WanVideoEncode` —— 7/20 个有
- `WanVideoUni3C_ControlnetLoader` —— 7/20 个有
- `WanVideoUni3C_embeds` —— 7/20 个有
- `ImageResizeKJ` —— 6/20 个有
- `WanVideoEnhanceAVideo` —— 4/20 个有
- `WanVideoExperimentalArgs` —— 4/20 个有
- `WanVideoSLG` —— 4/20 个有
- `SaveAudio` —— 3/20 个有
- `WanVideoEasyCache` —— 3/20 个有
- `WanVideoFreeInitArgs` —— 3/20 个有
- `WanVideoSetRadialAttention` —— 3/20 个有
- `WanVideoContextOptions` —— 2/20 个有
- `CR Text` —— 1/20 个有
- `CreateCFGScheduleFloatList` —— 1/20 个有
- `Fast Groups Bypasser (rgthree)` —— 1/20 个有
- `ImageResizeKJv2` —— 1/20 个有
- `LayerUtility: PurgeVRAM V2` —— 1/20 个有
- `PreviewAudio` —— 1/20 个有
- `WanVideoTorchCompileSettings` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
