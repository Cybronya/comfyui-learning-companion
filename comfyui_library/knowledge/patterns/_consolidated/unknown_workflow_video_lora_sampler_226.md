---
name: unknown_workflow_video_lora_sampler_226
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.677455
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageResizeKJv2, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/(二阶段)全能视频S视频修复重对口型稳定版V1_1973766509875040258.json, 平台全量/Infinitetalk-视频对口型_1958461367923666945.json, 平台全量/Infinitetalk_视频对口型_1957814447580573697.json, 平台全量/【InfiniteTalk】钟馗视频对口型工作流_1958428623009116161.json, 平台全量/视频改口型_InfiniteTalk_V2V_1959697748859760641.json, 数字人/数字人/视频改口型_InfiniteTalk_V2V_2054821175225790465.json, 数字人/数字人/顶配--nfinite Talk低高动态高清版V2_1987461960633659393.json, 视频生成/图生视频/[V2V新版]Infinite Talk动态运镜控制数字人V2_1958336218591334402.json, 视频生成/图生视频/图片生成口播视频_InfiniteTalk_I2V_2010602329619304450.json, 视频生成/图生视频/视频改口型_InfiniteTalk_V2V_2010621857124323330.json, 视频生成/图生视频/（单人版Nova）Infinite Talk高动态V2V高清版数字人V2_1969815681778786306.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_226

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（平台全量/(二阶段)全能视频S视频修复重对口型稳定版V1_1973766509875040258.json、平台全量/Infinitetalk-视频对口型_1958461367923666945.json、平台全量/Infinitetalk_视频对口型_1957814447580573697.json、平台全量/【InfiniteTalk】钟馗视频对口型工作流_1958428623009116161.json、平台全量/视频改口型_InfiniteTalk_V2V_1959697748859760641.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 11 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
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
- `LoadAudio` —— 10/11 个有
- `PreviewAny` —— 10/11 个有
- `VHS_LoadVideo` —— 10/11 个有
- `WanVideoTorchCompileSettings` —— 7/11 个有
- `AudioCrop` —— 6/11 个有
- `INTConstant` —— 6/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/11 个有
- `ImageConcatMulti` —— 5/11 个有
- `PreviewAudio` —— 5/11 个有
- `AudioCropProcessUTK` —— 4/11 个有
- `CR Prompt Text` —— 4/11 个有
- `ImageConcanate` —— 4/11 个有
- `JWInteger` —— 4/11 个有
- `LayerUtility: TextBox` —— 4/11 个有
- `PDIMAGE_LongerSize` —— 4/11 个有
- `ImageScaleByAspectRatio_UTK` —— 3/11 个有
- `ImpactSwitch` —— 3/11 个有
- `LoadImage` —— 3/11 个有
- `VHS_VideoInfo` —— 3/11 个有
- `LayerUtility: PurgeVRAM V2` —— 2/11 个有
- `easy cleanGpuUsed` —— 2/11 个有
- `Bjornulf_ShowInt` —— 1/11 个有
- `ImageFromBatch+` —— 1/11 个有
- `Label (rgthree)` —— 1/11 个有
- `RecordAudio` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
