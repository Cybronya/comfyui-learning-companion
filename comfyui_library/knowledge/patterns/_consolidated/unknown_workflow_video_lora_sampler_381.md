---
name: unknown_workflow_video_lora_sampler_381
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.44
common_nodes: [CLIPVisionLoader, FloatConstant, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageBatchExtendWithOverlap, ImageResizeKJv2, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MultiTalkWav2VecEmbeds, PreviewAny, ReplaceVideoLatentFrames, SetNode, TrimAudioDuration, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, Wav2VecModelLoader]
problems: []
missing: []
members: [图片生成/图生图/LongCatAvatar_龙猫数字人-文生图_2002914137871118338.json, 图片生成/文生图/内部测试0001_2006740333874384898.json, 数字人/数字人/LongCat Video Avatar 数字人图生视频_2004813148668522498.json, 数字人/数字人/LongCat-Video-Avatar-数字人-视频对口型_2005133378838036482.json, 数字人/数字人/LongCatAvatar 多段自动拼接 数字人_2004211639698292738.json, 视频生成/图生视频/LongCat-Video-Avatar大模型来了！上传1张照片+1段录音，轻松生成高质量数字人视频！_2004069109543411713.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_381

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/LongCatAvatar_龙猫数字人-文生图_2002914137871118338.json、图片生成/文生图/内部测试0001_2006740333874384898.json、数字人/数字人/LongCat Video Avatar 数字人图生视频_2004813148668522498.json、数字人/数字人/LongCat-Video-Avatar-数字人-视频对口型_2005133378838036482.json、数字人/数字人/LongCatAvatar 多段自动拼接 数字人_2004211639698292738.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：44%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPVisionLoader`
- `FloatConstant`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `Wav2VecModelLoader`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadWav2VecModel` —— 5/6 个有
- `INTConstant` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `IndexTTS2Run` —— 2/6 个有
- `JWInteger` —— 2/6 个有
- `MultiLinePromptIndex` —— 2/6 个有
- `SaveAudioMP3` —— 2/6 个有
- `AddLabel` —— 1/6 个有
- `AudioCrop` —— 1/6 个有
- `CR Prompt Text` —— 1/6 个有
- `CR Text` —— 1/6 个有
- `DF_Int_to_Float` —— 1/6 个有
- `Float` —— 1/6 个有
- `Int` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `PreviewAudio` —— 1/6 个有
- `PrimitiveFloat` —— 1/6 个有
- `RH_Nano_Banana2_Image2Image` —— 1/6 个有
- `SaveAudio` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有
- `ZML_ImageSelectorNode` —— 1/6 个有
- `easy downloadIndexTTSAndLoadModel` —— 1/6 个有
- `easy indexTTSGenerateSimple` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
