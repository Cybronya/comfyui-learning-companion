---
name: unknown_workflow_video_lora_sampler_797
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5615
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, GetNode, INTConstant, ImageResizeKJv2, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoPassImagesFromSamples, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/720x1280_solo_singing_MV_无运镜_2059587273380941826.json, 数字人/数字人/InifiniteTalk 数字人一键生成_2009171549823180801.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_797

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/720x1280_solo_singing_MV_无运镜_2059587273380941826.json、数字人/数字人/InifiniteTalk 数字人一键生成_2009171549823180801.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoPassImagesFromSamples`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 1/2 个有
- `AudioCrop` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `GetAudioDurationFromAudio` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有
- `ShowAnything|Mie` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `TextInput_` —— 1/2 个有
- `WanVideoEasyCache` —— 1/2 个有
- `WanVideoEnhanceAVideo` —— 1/2 个有
- `WanVideoExperimentalArgs` —— 1/2 个有
- `WanVideoSLG` —— 1/2 个有
- `Wav2VecModelLoader` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
