---
name: unknown_workflow_video_lora_sampler_668
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.810667
common_nodes: [CLIPVisionLoader, CR Prompt Text, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, ToInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/高动态口播数字人 InfiniteTalk+IndexTTS2 （Lightx2v+Rcm）_2090261460101459969.json, 视频生成/图生视频/InfiniteTalk高动态_1985744717117890562.json, 音频生成/音频生成/(歌曲数字人)全流程精准口型高强动作V4_1989287142675369986.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_668

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/高动态口播数字人 InfiniteTalk+IndexTTS2 （Lightx2v+Rcm）_2090261460101459969.json、视频生成/图生视频/InfiniteTalk高动态_1985744717117890562.json、音频生成/音频生成/(歌曲数字人)全流程精准口型高强动作V4_1989287142675369986.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
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
- `SimpleMath+`
- `ToInt`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `JWFloat` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `RH_GetAudioDuration` —— 2/3 个有
- `SaveAudio` —— 2/3 个有
- `easy int` —— 2/3 个有
- `AudioCrop` —— 1/3 个有
- `AudioSeparation` —— 1/3 个有
- `Bjornulf_ShowFloat` —— 1/3 个有
- `Bjornulf_ShowInt` —— 1/3 个有
- `Comfly_api_set` —— 1/3 个有
- `Comfly_suno_custom` —— 1/3 个有
- `ImpactSwitch` —— 1/3 个有
- `IndexTTS2Run` —— 1/3 个有
- `Int` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `PrimitiveString` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `SoundFlow_GetLength` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
