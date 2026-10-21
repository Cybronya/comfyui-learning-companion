---
name: unknown_workflow_video_lora_sampler_272
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.680125
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageResizeKJv2, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1958336218591334402.json, 视频生成/图生视频/2021869907490639874.json, 视频生成/图生视频/2003771753522470913.json, 视频生成/图生视频/2010335855776374785.json, 视频生成/图生视频/1969815681778786306.json, 音频生成/音频生成/InfiniteTalkV2V 视频对口型数字人说话唱歌_2005896738135306242.json, 音频生成/音频生成/视频对口型 自用_2019776475708268545.json, 音频生成/音频生成/视频对口型（指定角色）_2012598659203997698.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_272

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/1958336218591334402.json、视频生成/图生视频/2021869907490639874.json、视频生成/图生视频/2003771753522470913.json、视频生成/图生视频/2010335855776374785.json、视频生成/图生视频/1969815681778786306.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 8 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `SetNode`
- `VHS_LoadVideo`
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
- `Audio Duration (mtb)` —— 6/8 个有
- `ImageFromBatch+` —— 6/8 个有
- `JjkText` —— 6/8 个有
- `LayerUtility: PurgeVRAM` —— 6/8 个有
- `PrimitiveInt` —— 6/8 个有
- `PrimitiveString` —— 6/8 个有
- `SimpleMath+` —— 6/8 个有
- `CR Prompt Text` —— 2/8 个有
- `ImageConcanate` —— 2/8 个有
- `ImpactSwitch` —— 2/8 个有
- `JWInteger` —— 2/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `PDIMAGE_LongerSize` —— 2/8 个有
- `AILab_MaskPreview` —— 1/8 个有
- `ImageFromBatch` —— 1/8 个有
- `MaskListToMaskBatch` —— 1/8 个有
- `RH_Translator` —— 1/8 个有
- `Text` —— 1/8 个有
- `VHS_VideoInfo` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `easy sam3ModelLoader` —— 1/8 个有
- `easy sam3VideoSegmentation` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
