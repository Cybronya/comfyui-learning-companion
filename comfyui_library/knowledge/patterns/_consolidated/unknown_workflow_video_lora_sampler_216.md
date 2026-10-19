---
name: unknown_workflow_video_lora_sampler_216
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.832667
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, CR Prompt Text, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2045026952746115073.json, 视频生成/图生视频/1958590761962991617.json, 视频生成/图生视频/2039872167524966402.json, 视频生成/图生视频/1982787027227803649.json, 视频生成/图生视频/1976659195296727041.json, 视频生成/图生视频/1980462262907527170.json, 视频生成/图生视频/1958946563538235394.json, 视频生成/图生视频/1961034240169283585.json, 视频生成/图生视频/1980685750213722114.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_216

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2045026952746115073.json、视频生成/图生视频/1958590761962991617.json、视频生成/图生视频/2039872167524966402.json、视频生成/图生视频/1982787027227803649.json、视频生成/图生视频/1976659195296727041.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：83%

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
- `PreviewAny` —— 8/9 个有
- `WanVideoBlockSwap` —— 8/9 个有
- `GetAudioDurationFromAudio` —— 3/9 个有
- `SimpleMath+` —— 2/9 个有
- `Audio To Text (mtb)` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `JjkText` —— 1/9 个有
- `Load Whisper (mtb)` —— 1/9 个有
- `LongCatVoiceCloneTTS` —— 1/9 个有
- `MathExpression|pysssss` —— 1/9 个有
- `NormalizeAudioLoudness` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有
- `SaveAudio` —— 1/9 个有
- `SaveAudioMP3` —— 1/9 个有
- `ToInt` —— 1/9 个有
- `WanVideoTorchCompileSettings` —— 1/9 个有
- `easy convertAnything` —— 1/9 个有
- `easy imageConcat` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
