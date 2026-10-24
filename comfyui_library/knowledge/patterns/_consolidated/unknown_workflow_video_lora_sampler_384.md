---
name: unknown_workflow_video_lora_sampler_384
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7448
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, INTConstant, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, PreviewAudio, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/wan2.1-InfiniTetalk  音频+视频=数字人_1967763738742984706.json, 数字人/数字人/音频趋动 infinite talk wan2.1_2015430092859645953.json, 视频生成/图生视频/wan2.1-InfiniTetalk-音频+图像=数字人_1967501356460335105.json, 视频生成/图生视频/图片生成口播视频_InfiniteTalk_I2V_2010602329619304450.json, 视频生成/图生视频/视频改口型_InfiniteTalk_V2V_2010621857124323330.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_384

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/wan2.1-InfiniTetalk  音频+视频=数字人_1967763738742984706.json、数字人/数字人/音频趋动 infinite talk wan2.1_2015430092859645953.json、视频生成/图生视频/wan2.1-InfiniTetalk-音频+图像=数字人_1967501356460335105.json、视频生成/图生视频/图片生成口播视频_InfiniteTalk_I2V_2010602329619304450.json、视频生成/图生视频/视频改口型_InfiniteTalk_V2V_2010621857124323330.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 5 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `INTConstant`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `PreviewAudio`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 4/5 个有
- `WanVideoEncode` —— 4/5 个有
- `WanVideoTorchCompileSettings` —— 4/5 个有
- `GetNode` —— 3/5 个有
- `ImageConcatMulti` —— 3/5 个有
- `ImageResizeKJv2` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `VHS_LoadVideo` —— 3/5 个有
- `AudioCrop` —— 2/5 个有
- `AudioCropProcessUTK` —— 2/5 个有
- `Fast Bypasser (rgthree)` —— 2/5 个有
- `LayerUtility: PurgeVRAM V2` —— 2/5 个有
- `LayerUtility: TextBox` —— 2/5 个有
- `MelBandRoFormerModelLoader` —— 2/5 个有
- `MelBandRoFormerSampler` —— 2/5 个有
- `Wav2VecModelLoader` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `ColorMatch` —— 1/5 个有
- `ImageFromBatch` —— 1/5 个有
- `ImageScaleByAspectRatio_UTK` —— 1/5 个有
- `Int` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `Switch any [Crystools]` —— 1/5 个有
- `TrimAudioDuration` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
