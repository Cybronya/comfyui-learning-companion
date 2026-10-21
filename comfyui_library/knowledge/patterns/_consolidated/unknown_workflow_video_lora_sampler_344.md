---
name: unknown_workflow_video_lora_sampler_344
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.883833
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, CR Prompt Text, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1951530771968372737.json, 视频生成/图生视频/1960601741647634434.json, 视频生成/图生视频/2011699798700728322.json, 视频生成/图生视频/2015621252844621826.json, 视频生成/图生视频/2015621240408510465.json, 视频生成/图生视频/2009596955852279810.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_344

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1951530771968372737.json、视频生成/图生视频/1960601741647634434.json、视频生成/图生视频/2011699798700728322.json、视频生成/图生视频/2015621252844621826.json、视频生成/图生视频/2015621240408510465.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 5/6 个有
- `PreviewAudio` —— 5/6 个有
- `WanVideoImageToVideoMultiTalk` —— 5/6 个有
- `Int` —— 4/6 个有
- `IndexTTS2Run` —— 3/6 个有
- `JWInteger` —— 3/6 个有
- `PreviewAny` —— 3/6 个有
- `TwoWaySwitch` —— 3/6 个有
- `ZML_TextInput` —— 3/6 个有
- `MaskPreview+` —— 2/6 个有
- `SeparateMasks` —— 2/6 个有
- `WanVideoTorchCompileSettings` —— 2/6 个有
- `CR Integer To String` —— 1/6 个有
- `CreateCFGScheduleFloatList` —— 1/6 个有
- `EmptyAudio` —— 1/6 个有
- `INTConstant` —— 1/6 个有
- `JWFloat` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `SaveLatent` —— 1/6 个有
- `WanVideoImageToVideoEncode` —— 1/6 个有
- `WanVideoSetBlockSwap` —— 1/6 个有
- `WanVideoSetLoRAs` —— 1/6 个有
- `easy seed` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
