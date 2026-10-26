---
name: unknown_workflow_video_lora_sampler_229
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.868333
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_LoadVideo, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/19digitaaivideosing_2046947336139579394.json, 数字人/数字人/AI Video Studio PR插件VIP专用数字人口播(视频)工作流_2094295481898856450.json, 数字人/数字人/Infinite Talk数字人视频生视频流双人版_2073262552674557954.json, 数字人/数字人/Infinite Talk超自然无限长度视频生视频数字人（单人）_1958011933066768385.json, 数字人/数字人/Infinitetalk--视频对口型-完美复刻动作，保持原视频动作一致_1992505491098062850.json, 数字人/数字人/Infinitetalk_视频对口型-完美复刻动作，保持原视频动作一致_1961018358189723649.json, 数字人/数字人/Infinitetalk_视频对口型-完美复刻动作，保持原视频动作一致_1972208046057385986.json, 数字人/数字人/Infinitetalk_视频对口型-完美复刻动作，保持原视频动作一致_2011358802314010626.json, 数字人/数字人/infinitetalk-音频+视频数字人_1960547223945773057.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_229

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/反推提示词/19digitaaivideosing_2046947336139579394.json、数字人/数字人/AI Video Studio PR插件VIP专用数字人口播(视频)工作流_2094295481898856450.json、数字人/数字人/Infinite Talk数字人视频生视频流双人版_2073262552674557954.json、数字人/数字人/Infinite Talk超自然无限长度视频生视频数字人（单人）_1958011933066768385.json、数字人/数字人/Infinitetalk--视频对口型-完美复刻动作，保持原视频动作一致_1992505491098062850.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_LoadVideo`
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
- `GetImageRangeFromBatch` —— 8/9 个有
- `ImageResizeKJv2` —— 8/9 个有
- `VHS_VideoCombine` —— 8/9 个有
- `WanVideoEncode` —— 8/9 个有
- `GetImageSizeAndCount` —— 6/9 个有
- `easy int` —— 6/9 个有
- `GetNode` —— 5/9 个有
- `SetNode` —— 5/9 个有
- `SaveAudio` —— 4/9 个有
- `INTConstant` —— 3/9 个有
- `WanVideoTorchCompileSettings` —— 3/9 个有
- `Anything Everywhere` —— 2/9 个有
- `CR Prompt Text` —— 2/9 个有
- `JWInteger` —— 2/9 个有
- `AudioCombine` —— 1/9 个有
- `CreateVideo` —— 1/9 个有
- `GetImageSize` —— 1/9 个有
- `ImageBatchMulti` —— 1/9 个有
- `ImageConcatMulti` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `ReverseImageBatch` —— 1/9 个有
- `SaveVideo` —— 1/9 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/9 个有
- `WanVideoUni3C_embeds` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
