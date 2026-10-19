---
name: unknown_workflow_video_lora_sampler_310
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.426714
common_nodes: [CLIPVisionLoader, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageBatchExtendWithOverlap, ImageResizeKJv2, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MultiTalkWav2VecEmbeds, PreviewAny, ReplaceVideoLatentFrames, SetNode, TrimAudioDuration, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2004069109543411713.json, 视频生成/图生视频/2005920919849758721.json, 视频生成/图生视频/2004216271933767681.json, 视频生成/图生视频/2004028313129656322.json, 视频生成/图生视频/2003503610359103489.json, 视频生成/图生视频/2003272885085118465.json, 视频生成/图生视频/2003002229281964033.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_310

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2004069109543411713.json、视频生成/图生视频/2005920919849758721.json、视频生成/图生视频/2004216271933767681.json、视频生成/图生视频/2004028313129656322.json、视频生成/图生视频/2003503610359103489.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：43%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `ReplaceVideoLatentFrames`
- `SetNode`
- `TrimAudioDuration`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `FloatConstant` —— 6/7 个有
- `INTConstant` —— 6/7 个有
- `Wav2VecModelLoader` —— 6/7 个有
- `DownloadAndLoadWav2VecModel` —— 5/7 个有
- `WanVideoTorchCompileSettings` —— 5/7 个有
- `Int` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `Float` —— 1/7 个有
- `IndexTTS2Run` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `MemoryCleaner` —— 1/7 个有
- `MultiLinePromptIndex` —— 1/7 个有
- `PrimitiveFloat` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `SaveAudioMP3` —— 1/7 个有
- `easy forLoopEnd` —— 1/7 个有
- `easy forLoopStart` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
