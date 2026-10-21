---
name: unknown_workflow_video_lora_sampler_578
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.934333
common_nodes: [CLIPVisionLoader, CR Prompt Text, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, SoundFlow_GetLength, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/高动态口播数字人 InfiniteTalk+IndexTTS2 （Lightx2v+Rcm）_2090261460101459969.json, 视频生成/图生视频/1970484627771170817.json, 音频生成/音频生成/AA--声音克隆数字人-InfiniteTalk对口型图生视频（情感控制）_2030212385763495938.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_578

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/高动态口播数字人 InfiniteTalk+IndexTTS2 （Lightx2v+Rcm）_2090261460101459969.json、视频生成/图生视频/1970484627771170817.json、音频生成/音频生成/AA--声音克隆数字人-InfiniteTalk对口型图生视频（情感控制）_2030212385763495938.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `SoundFlow_GetLength`
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
- `AudioCrop` —— 2/3 个有
- `AudioSeparation` —— 2/3 个有
- `Bjornulf_ShowInt` —— 2/3 个有
- `IndexTTS2Run` —— 2/3 个有
- `SaveAudio` —— 2/3 个有
- `ToInt` —— 2/3 个有
- `easy int` —— 2/3 个有
- `1hew_AudioDuration` —— 1/3 个有
- `Bjornulf_ShowFloat` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Float to Int` —— 1/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `ImpactSwitch` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `PrimitiveString` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
