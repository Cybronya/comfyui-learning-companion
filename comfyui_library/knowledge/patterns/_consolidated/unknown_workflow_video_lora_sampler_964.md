---
name: unknown_workflow_video_lora_sampler_964
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.844
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, CR Prompt Text, CR Text, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, GetNode, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MaskPreview+, MathExpression|pysssss, MegaTTS3Run, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, PreviewAudio, SaveAudio, SaveAudioMP3, SeparateMasks, SetNode, VHS_VideoCombine, VoxCPM_TTS, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy downloadIndexTTSAndLoadModel, easy indexTTSAudioMerge, easy indexTTSGenerateSimple, easy int]
problems: []
missing: []
members: [视频生成/图生视频/加强版单人-双人[完美口型数字人]_1970560402209841153.json, 音频生成/音频生成/顶配视频版 单人-双人[完美口型数字人]_1970863789459546113.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_964

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/加强版单人-双人[完美口型数字人]_1970560402209841153.json、音频生成/音频生成/顶配视频版 单人-双人[完美口型数字人]_1970863789459546113.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `CR Text`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `GetNode`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskPreview+`
- `MathExpression|pysssss`
- `MegaTTS3Run`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `PreviewAudio`
- `SaveAudio`
- `SaveAudioMP3`
- `SeparateMasks`
- `SetNode`
- `VHS_VideoCombine`
- `VoxCPM_TTS`
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
- `easy downloadIndexTTSAndLoadModel`
- `easy indexTTSAudioMerge`
- `easy indexTTSGenerateSimple`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `IndexTTS2Run` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
