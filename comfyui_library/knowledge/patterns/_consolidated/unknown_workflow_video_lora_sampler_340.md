---
name: unknown_workflow_video_lora_sampler_340
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.948571
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, INTConstant, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAudio, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/Wan2.2+Multitalk数字人工作流_1952579748809641986.json, 数字人/数字人/空白工作流_1942131715920052225.json, 视频生成/图生视频/(KJ版)Wan2.2+multitalk 单人说话_1951530771968372737.json, 视频生成/图生视频/Digital Avatars for E-commerce InfiniteTalk +数字人带货_2095704577696948225.json, 视频生成/图生视频/InfiniteTalk+IndexTTS+Kontext数字人带货_1958084173951094786.json, 视频生成/图生视频/MultiTalk+IndexTTS+Kontext数字人带货_1937830211084029954.json, 音频生成/音频生成/InfiniteTalk+数字人口播带货_1973224776535814145.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_340

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/Wan2.2+Multitalk数字人工作流_1952579748809641986.json、数字人/数字人/空白工作流_1942131715920052225.json、视频生成/图生视频/(KJ版)Wan2.2+multitalk 单人说话_1951530771968372737.json、视频生成/图生视频/Digital Avatars for E-commerce InfiniteTalk +数字人带货_2095704577696948225.json、视频生成/图生视频/InfiniteTalk+IndexTTS+Kontext数字人带货_1958084173951094786.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `INTConstant`
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
- `ImageResizeKJv2` —— 6/7 个有
- `IndexTTSRun` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/7 个有
- `LayerUtility: PurgeVRAM V2` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `String Literal` —— 5/7 个有
- `ImageConcanate` —— 4/7 个有
- `RH_ComfyFluxKontext` —— 4/7 个有
- `RH_Translator` —— 4/7 个有
- `SaveImage` —— 4/7 个有
- `WanVideoImageToVideoEncode` —— 4/7 个有
- `WanVideoImageToVideoMultiTalk` —— 3/7 个有
- `CR Integer To String` —— 2/7 个有
- `CR Prompt Text` —— 2/7 个有
- `CreateCFGScheduleFloatList` —— 2/7 个有
- `GetImageSizeAndCount` —— 2/7 个有
- `MathExpression|pysssss` —— 2/7 个有
- `WanVideoSetBlockSwap` —— 2/7 个有
- `WanVideoSetLoRAs` —— 2/7 个有
- `easy seed` —— 2/7 个有
- `Int` —— 1/7 个有
- `JWInteger` —— 1/7 个有
- `SaveLatent` —— 1/7 个有
- `ttN int` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
