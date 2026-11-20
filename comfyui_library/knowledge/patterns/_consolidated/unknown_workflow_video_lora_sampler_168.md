---
name: unknown_workflow_video_lora_sampler_168
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.896538
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, ImageResizeKJv2, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/19digitaaivideosing_2046947336139579394.json, 平台全量/工作流视频篇10-视频生数字人-唱歌-口播-MV_2014251557331668993.json, 平台全量/视频对口型(加速版)720p_2010551895256993793.json, 数字人/数字人/1.2_InfiniteTalk视频+音频对口型（效果最好）_1994683257532915714.json, 数字人/数字人/AI Video Studio PR插件VIP专用数字人口播(视频)工作流_2094295481898856450.json, 数字人/数字人/InfiniteTalk数字人视频生视频2_1978763649466699777.json, 数字人/数字人/InfiniteTalk数字人视频生视频_1958502190061142018.json, 数字人/数字人/InfiniteTalk数字人视频生视频_1982814946415259649.json, 数字人/数字人/InfiniteTalk数字人视频生视频_2001131954474975234.json, 数字人/数字人/WH-AI-Studio视频生视频数字人-视频对口型（带情感音频生成）_2022275473673297921.json, 数字人/数字人/infinitetalk图像对口型_1971910981158891521.json, 数字人/数字人/数字人视频生视频_2004472334562066434.json, 数字人/数字人/数字人视频生视频_2041675802936352769.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_168

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/反推提示词/19digitaaivideosing_2046947336139579394.json、平台全量/工作流视频篇10-视频生数字人-唱歌-口播-MV_2014251557331668993.json、平台全量/视频对口型(加速版)720p_2010551895256993793.json、数字人/数字人/1.2_InfiniteTalk视频+音频对口型（效果最好）_1994683257532915714.json、数字人/数字人/AI Video Studio PR插件VIP专用数字人口播(视频)工作流_2094295481898856450.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
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
- `VHS_LoadVideo` —— 12/13 个有
- `VHS_VideoCombine` —— 12/13 个有
- `WanVideoEncode` —— 12/13 个有
- `WanVideoTorchCompileSettings` —— 11/13 个有
- `Audio Duration (mtb)` —— 9/13 个有
- `CR Text` —— 9/13 个有
- `GetImageSizeAndCount` —— 9/13 个有
- `ImageFromBatch+` —— 9/13 个有
- `PrimitiveInt` —— 9/13 个有
- `SimpleMath+` —— 9/13 个有
- `easy showAnything` —— 8/13 个有
- `Anything Everywhere` —— 3/13 个有
- `INTConstant` —— 3/13 个有
- `LoadImage` —— 3/13 个有
- `easy int` —— 3/13 个有
- `CreateVideo` —— 1/13 个有
- `GetImageSize` —— 1/13 个有
- `IndexTTS2Run` —— 1/13 个有
- `Int` —— 1/13 个有
- `PreviewAudio` —— 1/13 个有
- `PreviewImage` —— 1/13 个有
- `PrimitiveFloat` —— 1/13 个有
- `SaveVideo` —— 1/13 个有
- `TwoWaySwitch` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
