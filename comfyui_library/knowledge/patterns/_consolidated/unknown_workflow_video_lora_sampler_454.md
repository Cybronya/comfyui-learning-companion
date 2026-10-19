---
name: unknown_workflow_video_lora_sampler_454
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.643
common_nodes: [CLIPVisionLoader, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/视频对口型数字人_InfiniteTalk_V2V_2083750945984442370.json, 音频生成/音频生成/Infinitetalk视频添加语音视频对口型_1979388744887341058.json, 音频生成/音频生成/Wan2.1-InfiniteTalk--视频对口型_2042411569077821442.json, 音频生成/音频生成/infinitetalk对口型工作流_1995386268756402178.json, 音频生成/音频生成/视频对口型 音频驱动生视频   数字人 视频重绘 二次编辑_2063855129274707970.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_454

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/视频对口型数字人_InfiniteTalk_V2V_2083750945984442370.json、音频生成/音频生成/Infinitetalk视频添加语音视频对口型_1979388744887341058.json、音频生成/音频生成/Wan2.1-InfiniteTalk--视频对口型_2042411569077821442.json、音频生成/音频生成/infinitetalk对口型工作流_1995386268756402178.json、音频生成/音频生成/视频对口型 音频驱动生视频   数字人 视频重绘 二次编辑_2063855129274707970.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
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
- `AudioCrop` —— 4/5 个有
- `AudioSeparation` —— 4/5 个有
- `Display Int (rgthree)` —— 4/5 个有
- `DownloadAndLoadWav2VecModel` —— 4/5 个有
- `INTConstant` —— 4/5 个有
- `ImageConcatMulti` —— 4/5 个有
- `SimpleMath+` —— 4/5 个有
- `SoundFlow_GetLength` —— 4/5 个有
- `ToInt` —— 4/5 个有
- `WanVideoTorchCompileSettings` —— 4/5 个有
- `easy int` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `ImageBatchMulti` —— 2/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `ReverseImageBatch` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `Float` —— 1/5 个有
- `ImageResize+` —— 1/5 个有
- `ImpactInt` —— 1/5 个有
- `JWIntegerToString` —— 1/5 个有
- `Wav2VecModelLoader` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
