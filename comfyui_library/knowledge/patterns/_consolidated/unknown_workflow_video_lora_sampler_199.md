---
name: unknown_workflow_video_lora_sampler_199
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.790417
common_nodes: [Audio Duration (mtb), AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PrimitiveFloat, SimpleMath+, TextInput_, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [数字人/数字人/MultiTalk数字人唱歌-16G可玩_1942781589854031873.json, 数字人/数字人/MultiTalk数字人唱歌-16G可玩（优化版本）_1942816414530998274.json, 数字人/数字人/aiMVClip应用版_1985609275160645633.json, 数字人/数字人/稳定质量Multitalk--最新最强数字人_1936158876121337857.json, 视频生成/图生视频/MultiTalk 单人脱口秀｜KJ加速版_1936701399797501953.json, 视频生成/图生视频/MultiTalk+AniWan单人KJ高质量加速稳定版V4（UNI3C运镜-脸部稳定版）_1948784661829492737.json, 视频生成/图生视频/MultiTalk+AniWan单人KJ（UNI3C运镜 手持） 浮云 测试版_1998945387329282050.json, 视频生成/图生视频/MultiTalk+AniWan单人KJ（UNI3C运镜 手持） 浮云_1998778583533412354.json, 视频生成/图生视频/MultiTalk+Aniwan单人KJ高质量加速稳定版V4（脸部一致性版）_1948782335715094529.json, 视频生成/图生视频/MultiTalk+UNI3C运镜_1986856996743876610.json, 视频生成/图生视频/MultiTalk+Wan2.2（高低噪）加速版数字人V1（人物不动版UNI3C运镜）_1955533790640836610.json, 视频生成/图生视频/MultiTalk单人+Wan2.2(低)+Sigma调度KJ加速V4（全身动态版UNI3C运镜）_1955521619805421569.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_199

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（数字人/数字人/MultiTalk数字人唱歌-16G可玩_1942781589854031873.json、数字人/数字人/MultiTalk数字人唱歌-16G可玩（优化版本）_1942816414530998274.json、数字人/数字人/aiMVClip应用版_1985609275160645633.json、数字人/数字人/稳定质量Multitalk--最新最强数字人_1936158876121337857.json、视频生成/图生视频/MultiTalk 单人脱口秀｜KJ加速版_1936701399797501953.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 12 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PrimitiveFloat`
- `SimpleMath+`
- `TextInput_`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/12 个有
- `JWIntegerToString` —— 10/12 个有
- `LayerUtility: PurgeVRAM` —— 10/12 个有
- `easy showAnything` —— 10/12 个有
- `JWInteger` —— 9/12 个有
- `PrimitiveInt` —— 9/12 个有
- `ImageResizeKJ` —— 6/12 个有
- `VHS_LoadVideo` —— 6/12 个有
- `WanVideoEncode` —— 6/12 个有
- `WanVideoUni3C_ControlnetLoader` —— 6/12 个有
- `WanVideoUni3C_embeds` —— 6/12 个有
- `CreateCFGScheduleFloatList` —— 3/12 个有
- `SaveAudio` —— 3/12 个有
- `WanVideoSLG` —— 3/12 个有
- `AddLabel` —— 2/12 个有
- `EmptyImage` —— 2/12 个有
- `GetImageSizeAndCount` —— 2/12 个有
- `ImageConcatMulti` —— 2/12 个有
- `WanVideoEnhanceAVideo` —— 2/12 个有
- `WanVideoExperimentalArgs` —— 2/12 个有
- `WanVideoSetBlockSwap` —— 2/12 个有
- `WanVideoSetLoRAs` —— 2/12 个有
- `ColorMatch` —— 1/12 个有
- `FloatToSigmas` —— 1/12 个有
- `INTConstant` —— 1/12 个有
- `ImageResizeKJv2` —— 1/12 个有
- `LayerUtility: PurgeVRAM V2` —— 1/12 个有
- `MathExpression|pysssss` —— 1/12 个有
- `StringToFloatList` —— 1/12 个有
- `WanVideoContextOptions` —— 1/12 个有
- `WanVideoEasyCache` —— 1/12 个有
- `WanVideoFreeInitArgs` —— 1/12 个有
- `WanVideoSetRadialAttention` —— 1/12 个有
- `WanVideoTorchCompileSettings` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
