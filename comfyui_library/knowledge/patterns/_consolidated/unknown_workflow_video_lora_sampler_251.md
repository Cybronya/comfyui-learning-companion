---
name: unknown_workflow_video_lora_sampler_251
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.644333
common_nodes: [ComfyMathExpression, GetImageRangeFromBatch, INTConstant, ImageBatchExtendWithOverlap, LoadAudio, LoadImage, LongCatAvatarWhisperEmbeds, ReplaceVideoLatentFrames, TrimAudioDuration, VHS_VideoCombine, WanVideoDecode, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoTextEncodeCached, WanVideoVAELoader, WhisperModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/LongCat 1.5数字人动态加强稳定版V1_2058873230517166082.json, 视频生成/图生视频/LongCat 1.5数字人多图高动态稳定版V3_2058901183300980738.json, 视频生成/图生视频/LongCat 1.5数字人循环工作流_2059800193100505090.json, 视频生成/图生视频/LongCat 1.5数字人循环工作流_2073322311234711553.json, 视频生成/图生视频/LongCat 1.5数字人长视频工作流生产力版_2073710624823144449.json, 视频生成/图生视频/LongCat Avatar 1.5：8步极速生成、音频驱动超长数字人_2065330795597877250.json, 视频生成/图生视频/longcat avartart 1.5-extend-auto_2061455238598586369.json, 视频生成/图生视频/longcat avartart 1.5-extend_2061623496706449410.json, 视频生成/图生视频/很棒的LongCat 1.5数字人动态加强稳定-单次10s音频版_2060335881759838210.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_251

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/LongCat 1.5数字人动态加强稳定版V1_2058873230517166082.json、视频生成/图生视频/LongCat 1.5数字人多图高动态稳定版V3_2058901183300980738.json、视频生成/图生视频/LongCat 1.5数字人循环工作流_2059800193100505090.json、视频生成/图生视频/LongCat 1.5数字人循环工作流_2073322311234711553.json、视频生成/图生视频/LongCat 1.5数字人长视频工作流生产力版_2073710624823144449.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 9 个 workflow 都包含：
- `ComfyMathExpression`
- `GetImageRangeFromBatch`
- `INTConstant`
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
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `WhisperModelLoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 8/9 个有
- `ComfyNumberConvert` —— 6/9 个有
- `Float` —— 6/9 个有
- `FloatConstant` —— 6/9 个有
- `GetImageSizeAndCount` —— 6/9 个有
- `GetNode` —— 6/9 个有
- `PreviewAny` —— 6/9 个有
- `SetNode` —— 6/9 个有
- `WanVideoBlockSwap` —— 6/9 个有
- `easy forLoopEnd` —— 5/9 个有
- `easy forLoopStart` —— 5/9 个有
- `PreviewAudio` —— 4/9 个有
- `CR Prompt Text` —— 3/9 个有
- `GetImageSize` —— 3/9 个有
- `ProcessString` —— 3/9 个有
- `RH_LLMAPI_Pro_Node` —— 3/9 个有
- `WanAnimatePlus BlockSwap` —— 3/9 个有
- `easy indexAnything` —— 3/9 个有
- `easy promptList` —— 3/9 个有
- `easy showAnything` —— 3/9 个有
- `CR Prompt List` —— 2/9 个有
- `CR Text Replace` —— 2/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `ShowAnything|Mie` —— 1/9 个有
- `WujiCleaner` —— 1/9 个有
- `孤海注释` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
