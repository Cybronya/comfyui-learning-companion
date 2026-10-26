---
name: unknown_workflow_video_upscale_lora_27
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.99
common_nodes: [ColorMatch, GODMT_ListGetByIndex, GODMT_SplitString, GetImageRangeFromBatch, GetImageSize+, ImageUpscaleWithModel, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, RH_Captioner, RH_Prompter, SaveImage, Text Multiline, TextInput_, TextPreview, UpscaleModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy batchAnything, easy float, easy forLoopEnd, easy forLoopStart, easy promptConcat]
problems: []
missing: []
members: [数字人/数字人/MultiTalk_FusionX_无限图生数字人_1939304835680485377.json, 视频生成/图生视频/FusionX_Vace_无限图生视频_1939266325271461889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_27

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/MultiTalk_FusionX_无限图生数字人_1939304835680485377.json、视频生成/图生视频/FusionX_Vace_无限图生视频_1939266325271461889.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：99%

## 共有节点

全部 2 个 workflow 都包含：
- `ColorMatch`
- `GODMT_ListGetByIndex`
- `GODMT_SplitString`
- `GetImageRangeFromBatch`
- `GetImageSize+`
- `ImageUpscaleWithModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `RH_Captioner`
- `RH_Prompter`
- `SaveImage`
- `Text Multiline`
- `TextInput_`
- `TextPreview`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy batchAnything`
- `easy float`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 1/2 个有
- `AudioCrop` —— 1/2 个有
- `CLIPVisionLoader` —— 1/2 个有
- `ComparingTwoFrames_` —— 1/2 个有
- `DownloadAndLoadWav2VecModel` —— 1/2 个有
- `JWFloatMin` —— 1/2 个有
- `JWFloatToString` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `MultiTalkModelLoader` —— 1/2 个有
- `MultiTalkWav2VecEmbeds` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `WanVideoClipVisionEncode` —— 1/2 个有
- `WanVideoContextOptions` —— 1/2 个有
- `WanVideoImageToVideoEncode` —— 1/2 个有
- `WanVideoMagCache` —— 1/2 个有
- `WanVideoVACEEncode` —— 1/2 个有
- `WanVideoVACEStartToEndFrame` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
