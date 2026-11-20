---
name: unknown_workflow_video_lora_sampler_566
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.609
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAudio, RH_GetAudioDuration, SoundFlow_TrimAudio, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/mulBL_stable_1999825490863063041.json, 图片生成/文生图/mul_only_720_1995744614046896130.json, 数字人/数字人/infinitetalk多段mv生成5段_1995307640144191489.json, 视频生成/图生视频/infinitetalk多段mv生成_1968146725170982914.json, 视频生成/图生视频/多镜头 InfiniteTalk 数字人_1994360577734610945.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_566

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/mulBL_stable_1999825490863063041.json、图片生成/文生图/mul_only_720_1995744614046896130.json、数字人/数字人/infinitetalk多段mv生成5段_1995307640144191489.json、视频生成/图生视频/infinitetalk多段mv生成_1968146725170982914.json、视频生成/图生视频/多镜头 InfiniteTalk 数字人_1994360577734610945.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAudio`
- `RH_GetAudioDuration`
- `SoundFlow_TrimAudio`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `WanVideoTorchCompileSettings` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `JoinStringMulti` —— 3/5 个有
- `MathExpression|pysssss` —— 3/5 个有
- `PreviewAny` —— 3/5 个有
- `RH_VideoMerge` —— 3/5 个有
- `SaveVideo` —— 3/5 个有
- `Text` —— 3/5 个有
- `VHS_SelectFilename` —— 3/5 个有
- `easy float` —— 3/5 个有
- `easy int` —— 3/5 个有
- `AudioSeparation` —— 2/5 个有
- `Display Int (rgthree)` —— 2/5 个有
- `ImageBatchMulti` —— 2/5 个有
- `ImageFromBatch` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `SimpleMath+` —— 2/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
