---
name: unknown_workflow_video_lora_sampler_210
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.845111
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, CR Prompt Text, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2045026952746115073.json, 视频生成/图生视频/1958590761962991617.json, 视频生成/图生视频/2039872167524966402.json, 视频生成/图生视频/1982787027227803649.json, 视频生成/图生视频/1976659195296727041.json, 视频生成/图生视频/1980462262907527170.json, 视频生成/图生视频/1958946563538235394.json, 视频生成/图生视频/2056334538120454145.json, 视频生成/图生视频/2039220767790997506.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_210

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2045026952746115073.json、视频生成/图生视频/1958590761962991617.json、视频生成/图生视频/2039872167524966402.json、视频生成/图生视频/1982787027227803649.json、视频生成/图生视频/1976659195296727041.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 9 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoBlockSwap` —— 8/9 个有
- `MathExpression|pysssss` —— 3/9 个有
- `AudioToFPS` —— 2/9 个有
- `Bjornulf_ShowInt` —— 2/9 个有
- `GetAudioDurationFromAudio` —— 2/9 个有
- `JWFloat` —— 2/9 个有
- `Audio To Text (mtb)` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `Load Whisper (mtb)` —— 1/9 个有
- `LongCatVoiceCloneTTS` —— 1/9 个有
- `NormalizeAudioLoudness` —— 1/9 个有
- `SaveAudio` —— 1/9 个有
- `SaveAudioMP3` —— 1/9 个有
- `SimpleMath+` —— 1/9 个有
- `ToInt` —— 1/9 个有
- `WanVideoTorchCompileSettings` —— 1/9 个有
- `easy imageConcat` —— 1/9 个有
- `孤海注释` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
