---
name: unknown_workflow_video_sampler_vae_46
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.893889
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/API-数字人-InfiniteTalk-单人对口型工作流_2059537663195172866.json, 数字人/数字人/I2V-InfiniteTalk双人数字人_2002787606607872002.json, 数字人/数字人/InfiniteTalk 图片生成单人唱歌视频（不限生成时长、批次提示词）_1958583900547268610.json, 数字人/数字人/InfiniteTalk-多人无限时长数字人生成工作流_1957766648377831426.json, 数字人/数字人/InfiniteTalk对口型工作流 V1.0_2052269912881676289.json, 数字人/数字人/InfiniteTalk数字人图生语音视频_1964942874242633729.json, 数字人/数字人/双人多人对口型数字人（漫剧、短剧、电商）_2040688295524438018.json, 视频生成/图生视频/I2V-InfiniteTalk双人数字人_1985223003455823873.json, 视频生成/图生视频/InfiniteTalk & LatentSync 对口型工作流 V1.0_2028880263652052993.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_46

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（数字人/数字人/API-数字人-InfiniteTalk-单人对口型工作流_2059537663195172866.json、数字人/数字人/I2V-InfiniteTalk双人数字人_2002787606607872002.json、数字人/数字人/InfiniteTalk 图片生成单人唱歌视频（不限生成时长、批次提示词）_1958583900547268610.json、数字人/数字人/InfiniteTalk-多人无限时长数字人生成工作流_1957766648377831426.json、数字人/数字人/InfiniteTalk对口型工作流 V1.0_2052269912881676289.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 8/9 个有
- `WanVideoTorchCompileSettings` —— 7/9 个有
- `ImageResizeKJv2` —— 6/9 个有
- `easy showAnything` —— 6/9 个有
- `PreviewImage` —— 5/9 个有
- `WanVideoLoraSelectMulti` —— 5/9 个有
- `Audio Duration (mtb)` —— 4/9 个有
- `PreviewAudio` —— 4/9 个有
- `SimpleMath+` —— 4/9 个有
- `VHS_LoadVideo` —— 4/9 个有
- `WanVideoLoraSelect` —— 4/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/9 个有
- `ToInt` —— 3/9 个有
- `Getter` —— 2/9 个有
- `Int` —— 2/9 个有
- `LayerUtility: PurgeVRAM V2` —— 2/9 个有
- `MathExpression|pysssss` —— 2/9 个有
- `PrimitiveFloat` —— 2/9 个有
- `QZ_ResolutionPreset` —— 2/9 个有
- `RH_GetAudioDuration` —— 2/9 个有
- `Setter` —— 2/9 个有
- `AudioCombine` —— 1/9 个有
- `INTConstant` —— 1/9 个有
- `ImageFromBatch+` —— 1/9 个有
- `LatentSyncNode` —— 1/9 个有
- `VHS_VideoInfoLoaded` —— 1/9 个有
- `VideoLengthAdjuster` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
