---
name: unknown_workflow_video_lora_vae_4
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.868
common_nodes: [ComfyNumberConvert, FloatConstant, ImageResizeKJv2, LoadAudio, LoadImage, LongCatAvatarWhisperEmbeds, TrimAudioDuration, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoVAELoader, WhisperModelLoader]
problems: []
missing: []
members: [图片生成/图生图/longcatAvatar1.5单段版_2061722462232080386.json, 数字人/数字人/LongCat-Video-Avatar 1.5单人_2058837211642163202.json, 数字人/数字人/LongCat-Video-Avatar 1.5数字人_2058887899709534210.json, 视频生成/图生视频/LongcatAvatar1.5长视频专用，脱口秀、歌手、主播_2061799694145245185.json, 视频生成/图生视频/long cat1.5数字人对口型工作流_2060239521802969090.json, 视频生成/图生视频/longcatAvatar1.5 图片数字人v1_2106246745930944513.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_vae_4

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/longcatAvatar1.5单段版_2061722462232080386.json、数字人/数字人/LongCat-Video-Avatar 1.5单人_2058837211642163202.json、数字人/数字人/LongCat-Video-Avatar 1.5数字人_2058887899709534210.json、视频生成/图生视频/LongcatAvatar1.5长视频专用，脱口秀、歌手、主播_2061799694145245185.json、视频生成/图生视频/long cat1.5数字人对口型工作流_2060239521802969090.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `ComfyNumberConvert`
- `FloatConstant`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LongCatAvatarWhisperEmbeds`
- `TrimAudioDuration`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WhisperModelLoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 4/6 个有
- `LoadWanVideoT5TextEncoder` —— 4/6 个有
- `WanVideoSamplerv2` —— 4/6 个有
- `WanVideoSchedulerv2` —— 4/6 个有
- `WanVideoTextEncode` —— 4/6 个有
- `ComfyMathExpression` —— 3/6 个有
- `WanVideoSetBlockSwap` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `Evaluate Floats` —— 2/6 个有
- `GetImageRangeFromBatch` —— 2/6 个有
- `GetImageSizeAndCount` —— 2/6 个有
- `ImageBatchExtendWithOverlap` —— 2/6 个有
- `ReplaceVideoLatentFrames` —— 2/6 个有
- `WanVideoSampler` —— 2/6 个有
- `WanVideoTextEncodeCached` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
