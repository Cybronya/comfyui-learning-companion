---
name: unknown_workflow_video_lora_vae_2
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.71725
common_nodes: [ComfyMathExpression, GetImageRangeFromBatch, ImageBatchExtendWithOverlap, LoadAudio, LoadImage, LongCatAvatarWhisperEmbeds, ReplaceVideoLatentFrames, TrimAudioDuration, VHS_VideoCombine, WanVideoDecode, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoTextEncodeCached, WanVideoVAELoader, WhisperModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/2058873230517166082.json, 视频生成/图生视频/2058901183300980738.json, 视频生成/图生视频/2059800193100505090.json, 视频生成/图生视频/2073322311234711553.json, 视频生成/图生视频/2073710624823144449.json, 视频生成/图生视频/2065330795597877250.json, 视频生成/图生视频/Longcat-Avatar1.5-超长时长数字人v1_2107328414905626625.json, 视频生成/图生视频/2060335881759838210.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_vae_2

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2058873230517166082.json、视频生成/图生视频/2058901183300980738.json、视频生成/图生视频/2059800193100505090.json、视频生成/图生视频/2073322311234711553.json、视频生成/图生视频/2073710624823144449.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 8 个 workflow 都包含：
- `ComfyMathExpression`
- `GetImageRangeFromBatch`
- `ImageBatchExtendWithOverlap`
- `LoadAudio`
- `LoadImage`
- `LongCatAvatarWhisperEmbeds`
- `ReplaceVideoLatentFrames`
- `TrimAudioDuration`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `WhisperModelLoader`

**可变部分**（部分 workflow 才有）：
- `ComfyNumberConvert` —— 7/8 个有
- `Float` —— 7/8 个有
- `GetImageSizeAndCount` —— 7/8 个有
- `INTConstant` —— 7/8 个有
- `ImageResizeKJv2` —— 7/8 个有
- `WanVideoSamplerv2` —— 7/8 个有
- `WanVideoSchedulerv2` —— 7/8 个有
- `WanVideoBlockSwap` —— 6/8 个有
- `easy forLoopEnd` —— 5/8 个有
- `easy forLoopStart` —— 5/8 个有
- `CR Prompt Text` —— 4/8 个有
- `FloatConstant` —— 4/8 个有
- `GetNode` —— 4/8 个有
- `PreviewAny` —— 4/8 个有
- `SetNode` —— 4/8 个有
- `easy indexAnything` —— 4/8 个有
- `easy promptList` —— 4/8 个有
- `ProcessString` —— 3/8 个有
- `RH_LLMAPI_Pro_Node` —— 3/8 个有
- `easy showAnything` —— 3/8 个有
- `CR Prompt List` —— 2/8 个有
- `CR Text Replace` —— 2/8 个有
- `PreviewAudio` —— 2/8 个有
- `WanAnimatePlus BlockSwap` —— 2/8 个有
- `GetImageSize` —— 1/8 个有
- `Int` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `ShowAnything|Mie` —— 1/8 个有
- `WanVideoSampler` —— 1/8 个有
- `WujiCleaner` —— 1/8 个有
- `孤海注释` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
