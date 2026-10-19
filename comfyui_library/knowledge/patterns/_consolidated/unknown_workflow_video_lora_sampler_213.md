---
name: unknown_workflow_video_lora_sampler_213
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.960889
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAudio, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: [LayerUtility: PurgeVRAM V2, MathExpression|pysssss, String Literal]
members: [视频生成/图生视频/1968265294475079681.json, 视频生成/图生视频/1957826997610446849.json, 视频生成/图生视频/Digital Avatars for E-commerce InfiniteTalk +数字人带货_2095704577696948225.json, 视频生成/图生视频/1971453748994359297.json, 视频生成/图生视频/1958084173951094786.json, 视频生成/图生视频/1937830211084029954.json, 视频生成/图生视频/1963202407591292929.json, 视频生成/文生视频/1968265294475079681.json, 音频生成/音频生成/InfiniteTalk+数字人口播带货_1973224776535814145.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_213

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1968265294475079681.json、视频生成/图生视频/1957826997610446849.json、视频生成/图生视频/Digital Avatars for E-commerce InfiniteTalk +数字人带货_2095704577696948225.json、视频生成/图生视频/1971453748994359297.json、视频生成/图生视频/1958084173951094786.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 9 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAudio`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoImageToVideoMultiTalk` —— 8/9 个有
- `LayerUtility: PurgeVRAM V2` —— 7/9 个有
- `RH_Translator` —— 7/9 个有
- `String Literal` —— 7/9 个有
- `INTConstant` —— 6/9 个有
- `ImageConcanate` —— 4/9 个有
- `IndexTTSRun` —— 4/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/9 个有
- `PreviewImage` —— 4/9 个有
- `RH_ComfyFluxKontext` —— 4/9 个有
- `SaveImage` —— 4/9 个有
- `MathExpression|pysssss` —— 3/9 个有
- `MelBandRoFormerModelLoader` —— 3/9 个有
- `MelBandRoFormerSampler` —— 3/9 个有
- `RH_Nano_Banana_Image2Image` —— 3/9 个有
- `SoundFlow_GetLength` —— 3/9 个有
- `IndexTTS2Run` —— 2/9 个有
- `JWStringMultiline` —— 2/9 个有
- `MaskPreview+` —— 2/9 个有
- `SeparateMasks` —— 2/9 个有
- `MegaTTS3Run` —— 1/9 个有
- `SaveAudioMP3` —— 1/9 个有
- `WanVideoImageToVideoEncode` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM V2、MathExpression|pysssss、String Literal
