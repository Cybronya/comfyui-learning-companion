---
name: unknown_workflow_video_lora_sampler_289
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.811375
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/更好用的InfiniteTalk对口型说话_唱歌数字人-稳定动态+强引导+色彩还原_2060438227680583681.json, 数字人/数字人/电商数字人infinitetalk_1988491410166996993.json, 数字人/数字人/老炮infinitetalk_1959555573828235265.json, 视频生成/图生视频/Infinite Talk 双人数字人_1970484627771170817.json, 视频生成/图生视频/InfiniteTalk数字人图生视频-自动对口型（支持唱歌_说话） 浮云12.11 次用_1998779897466249217.json, 视频生成/图生视频/infinitetalk-数字人口播对口型V1_2054541988237717506.json, 视频生成/图生视频/高清数字人-稳定加强V2.0版(对口型、口播、唱歌）最强AI数字人高清InfiniteTalk单人口_2075038609807339522.json, 音频生成/音频生成/AA--声音克隆数字人-InfiniteTalk对口型图生视频（情感控制）_2030212385763495938.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_289

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/更好用的InfiniteTalk对口型说话_唱歌数字人-稳定动态+强引导+色彩还原_2060438227680583681.json、数字人/数字人/电商数字人infinitetalk_1988491410166996993.json、数字人/数字人/老炮infinitetalk_1959555573828235265.json、视频生成/图生视频/Infinite Talk 双人数字人_1970484627771170817.json、视频生成/图生视频/InfiniteTalk数字人图生视频-自动对口型（支持唱歌_说话） 浮云12.11 次用_1998779897466249217.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
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
- `AudioCrop` —— 6/8 个有
- `AudioSeparation` —— 6/8 个有
- `CR Prompt Text` —— 4/8 个有
- `CR Text` —— 4/8 个有
- `SoundFlow_GetLength` —— 4/8 个有
- `WanVideoTorchCompileSettings` —— 4/8 个有
- `Float to Int` —— 3/8 个有
- `Int` —— 3/8 个有
- `ToInt` —— 3/8 个有
- `easy showAnything` —— 3/8 个有
- `GetNode` —— 2/8 个有
- `ImpactInt` —— 2/8 个有
- `JWIntegerToString` —— 2/8 个有
- `RH_GetAudioDuration` —— 2/8 个有
- `SetNode` —— 2/8 个有
- `easy int` —— 2/8 个有
- `1hew_AudioDuration` —— 1/8 个有
- `Bjornulf_ShowInt` —— 1/8 个有
- `CM_IntToFloat` —— 1/8 个有
- `IndexTTS2Run` —— 1/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `SaveAudio` —— 1/8 个有
- `easy float` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
