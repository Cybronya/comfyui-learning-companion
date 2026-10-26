---
name: unknown_workflow_video_lora_sampler_347
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.677143
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/视频改口型_InfiniteTalk_V2V_2054821175225790465.json, 数字人/数字人/音频趋动 infinite talk wan2.1_2015430092859645953.json, 数字人/数字人/顶配--nfinite Talk低高动态高清版V2_1987461960633659393.json, 视频生成/图生视频/[V2V新版]Infinite Talk动态运镜控制数字人V2_1958336218591334402.json, 视频生成/图生视频/图片生成口播视频_InfiniteTalk_I2V_2010602329619304450.json, 视频生成/图生视频/视频改口型_InfiniteTalk_V2V_2010621857124323330.json, 视频生成/图生视频/（单人版Nova）Infinite Talk高动态V2V高清版数字人V2_1969815681778786306.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_347

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/视频改口型_InfiniteTalk_V2V_2054821175225790465.json、数字人/数字人/音频趋动 infinite talk wan2.1_2015430092859645953.json、数字人/数字人/顶配--nfinite Talk低高动态高清版V2_1987461960633659393.json、视频生成/图生视频/[V2V新版]Infinite Talk动态运镜控制数字人V2_1958336218591334402.json、视频生成/图生视频/图片生成口播视频_InfiniteTalk_I2V_2010602329619304450.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 6/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `VHS_LoadVideo` —— 6/7 个有
- `INTConstant` —— 4/7 个有
- `PreviewAudio` —— 4/7 个有
- `AudioCrop` —— 3/7 个有
- `AudioCropProcessUTK` —— 3/7 个有
- `CR Prompt Text` —— 3/7 个有
- `ImageConcanate` —— 3/7 个有
- `ImpactSwitch` —— 3/7 个有
- `JWInteger` —— 3/7 个有
- `LayerUtility: TextBox` —— 3/7 个有
- `LoadImage` —— 3/7 个有
- `PDIMAGE_LongerSize` —— 3/7 个有
- `WanVideoTorchCompileSettings` —— 3/7 个有
- `ImageConcatMulti` —— 2/7 个有
- `ImageScaleByAspectRatio_UTK` —— 2/7 个有
- `LayerUtility: PurgeVRAM V2` —— 2/7 个有
- `VHS_VideoInfo` —— 2/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `ColorMatch` —— 1/7 个有
- `ImageFromBatch` —— 1/7 个有
- `TrimAudioDuration` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
