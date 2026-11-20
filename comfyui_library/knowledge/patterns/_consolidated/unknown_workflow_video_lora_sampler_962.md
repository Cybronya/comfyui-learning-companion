---
name: unknown_workflow_video_lora_sampler_962
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAudio, RH_Nano_Banana_Image2Image, RH_Translator, SoundFlow_GetLength, String Literal, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/全能图片V1+MegaTTS3+InfiniteTalk数字人带货_1963202407591292929.json, 视频生成/文生视频/全能图片V1+IndexTTS-2.0+InfiniteTalk数字人带货_1968265294475079681.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_962

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/全能图片V1+MegaTTS3+InfiniteTalk数字人带货_1963202407591292929.json、视频生成/文生视频/全能图片V1+IndexTTS-2.0+InfiniteTalk数字人带货_1968265294475079681.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAudio`
- `RH_Nano_Banana_Image2Image`
- `RH_Translator`
- `SoundFlow_GetLength`
- `String Literal`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `IndexTTS2Run` —— 1/2 个有
- `JWStringMultiline` —— 1/2 个有
- `MegaTTS3Run` —— 1/2 个有
- `SaveAudioMP3` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
