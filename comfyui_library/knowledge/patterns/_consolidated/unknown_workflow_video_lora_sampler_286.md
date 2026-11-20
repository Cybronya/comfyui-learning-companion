---
name: unknown_workflow_video_lora_sampler_286
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7917
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/MultiTalk_图生视频_1936815365949149186.json, 视频生成/图生视频/MultiTalk单人KJ高质量加速稳定版(无clipvision版)_1936345879362310145.json, 视频生成/图生视频/MultiTalk单人KJ高质量加速稳定版V2（大幅度增加时长）_1936304565509607426.json, 视频生成/图生视频/MultiTalk单人KJ高质量加速稳定版（UNI3C运镜版）_1936341490123837441.json, 视频生成/图生视频/MultiTalk数字人口播单人版_1940606353897402370.json, 视频生成/图生视频/MultiTalk最强数字人插件16G可玩，音频+图片=王炸数字人_1937864518498455553.json, 视频生成/图生视频/Multitalk+aniwan数字人，可说话演讲可唱歌_1940356622893953026.json, 视频生成/图生视频/Multitalk数字人（极速版）_1937674986381295618.json, 视频生成/图生视频/ani ③-Multitalk数字人_1945034637402099713.json, 音频生成/音频生成/Multitalk+aniwan数字人，可说话演讲可唱歌_1949746352932741121.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_286

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MultiTalk_图生视频_1936815365949149186.json、视频生成/图生视频/MultiTalk单人KJ高质量加速稳定版(无clipvision版)_1936345879362310145.json、视频生成/图生视频/MultiTalk单人KJ高质量加速稳定版V2（大幅度增加时长）_1936304565509607426.json、视频生成/图生视频/MultiTalk单人KJ高质量加速稳定版（UNI3C运镜版）_1936341490123837441.json、视频生成/图生视频/MultiTalk数字人口播单人版_1940606353897402370.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 10 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `Audio Duration (mtb)` —— 9/10 个有
- `JWInteger` —— 9/10 个有
- `JWIntegerToString` —— 9/10 个有
- `LayerUtility: PurgeVRAM` —— 9/10 个有
- `PrimitiveFloat` —— 9/10 个有
- `TextInput_` —— 9/10 个有
- `WanVideoClipVisionEncode` —— 9/10 个有
- `easy showAnything` —— 9/10 个有
- `PrimitiveInt` —— 7/10 个有
- `VHS_LoadVideo` —— 3/10 个有
- `WanVideoEncode` —— 3/10 个有
- `WanVideoUni3C_ControlnetLoader` —— 3/10 个有
- `WanVideoUni3C_embeds` —— 3/10 个有
- `ImageResizeKJ` —— 2/10 个有
- `WanVideoEasyCache` —— 2/10 个有
- `WanVideoEnhanceAVideo` —— 2/10 个有
- `WanVideoExperimentalArgs` —— 2/10 个有
- `WanVideoFreeInitArgs` —— 2/10 个有
- `WanVideoSLG` —— 2/10 个有
- `WanVideoSetRadialAttention` —— 2/10 个有
- `CR Text` —— 1/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `LayerUtility: PurgeVRAM V2` —— 1/10 个有
- `PreviewAudio` —— 1/10 个有
- `WanVideoContextOptions` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
