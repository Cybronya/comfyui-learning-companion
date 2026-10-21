---
name: unknown_workflow_video_lora_sampler_416
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.574
common_nodes: [FloatConstant, INTConstant, ImageResizeKJv2, LoadAudio, LoadImage, LongCatAvatarWhisperEmbeds, TrimAudioDuration, VHS_VideoCombine, WanVideoDecode, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoTextEncodeCached, WanVideoVAELoader, WhisperModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/2061799694145245185.json, 视频生成/图生视频/2060239521802969090.json, 视频生成/图生视频/2061455238598586369.json, 视频生成/图生视频/2061623496706449410.json, 视频生成/图生视频/2061466076168409089.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_416

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2061799694145245185.json、视频生成/图生视频/2060239521802969090.json、视频生成/图生视频/2061455238598586369.json、视频生成/图生视频/2061623496706449410.json、视频生成/图生视频/2061466076168409089.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 5 个 workflow 都包含：
- `FloatConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LongCatAvatarWhisperEmbeds`
- `TrimAudioDuration`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `WhisperModelLoader`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 4/5 个有
- `GetImageRangeFromBatch` —— 4/5 个有
- `GetNode` —— 4/5 个有
- `ImageBatchExtendWithOverlap` —— 4/5 个有
- `PreviewAny` —— 4/5 个有
- `ReplaceVideoLatentFrames` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `WanAnimatePlus BlockSwap` —— 3/5 个有
- `ComfyNumberConvert` —— 2/5 个有
- `GetImageSize` —— 2/5 个有
- `GetImageSizeAndCount` —— 2/5 个有
- `PreviewAudio` —— 2/5 个有
- `WanVideoBlockSwap` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `easy forLoopEnd` —— 1/5 个有
- `easy forLoopStart` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
