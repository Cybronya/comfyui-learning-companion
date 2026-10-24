---
name: unknown_workflow_video_sampler_vae_42
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9629
common_nodes: [AudioCrop, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/InfiniteTalk-wan-双人-index tts_1958085210749415426.json, 视频生成/图生视频/InfiniteTalk-图片唱歌 单人数字人工作流_2086309319305424897.json, 视频生成/图生视频/InfiniteTalk单人数字人工作流_1957827307850530818.json, 视频生成/图生视频/InfiniteTalk单人数字人工作流_1957977430084481025.json, 视频生成/图生视频/InfiniteTalk图片多人对口型工作流_2070503715320193025.json, 视频生成/图生视频/InfiniteTalk对口型_1958082253886803970.json, 视频生成/图生视频/InfiniteTalk数字人双人对口型_1998964761461186561.json, 视频生成/图生视频/Multitalk多人对话(爱屋复制版)_1940924821561884673.json, 视频生成/图生视频/infinite+wan2.1多人对口型_1960541577531842561.json, 视频生成/图生视频/multitalk-wan-双人-index tts_1941378778566389761.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_42

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/InfiniteTalk-wan-双人-index tts_1958085210749415426.json、视频生成/图生视频/InfiniteTalk-图片唱歌 单人数字人工作流_2086309319305424897.json、视频生成/图生视频/InfiniteTalk单人数字人工作流_1957827307850530818.json、视频生成/图生视频/InfiniteTalk单人数字人工作流_1957977430084481025.json、视频生成/图生视频/InfiniteTalk图片多人对口型工作流_2070503715320193025.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 10 个 workflow 都包含：
- `AudioCrop`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioSeparation` —— 9/10 个有
- `CLIPVisionLoader` —— 9/10 个有
- `WanVideoClipVisionEncode` —— 9/10 个有
- `WanVideoTorchCompileSettings` —— 9/10 个有
- `WanVideoLoraSelect` —— 8/10 个有
- `ImageResizeKJv2` —— 6/10 个有
- `SeparateMasks` —— 6/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/10 个有
- `PreviewAudio` —— 5/10 个有
- `INTConstant` —— 3/10 个有
- `MathExpression|pysssss` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `LayerMask: MaskPreview` —— 2/10 个有
- `MaskPreview` —— 2/10 个有
- `StringToInt` —— 2/10 个有
- `WanVideoLoraSelectMulti` —— 2/10 个有
- `ImageScaleToMegapixels` —— 1/10 个有
- `IndexTTSRun` —— 1/10 个有
- `LayerUtility: PurgeVRAM V2` —— 1/10 个有
- `String Literal` —— 1/10 个有
- `UpscaleModelLoader` —— 1/10 个有
- `VHS_LoadVideo` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有
- `easy int` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
