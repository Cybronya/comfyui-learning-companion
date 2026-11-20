---
name: unknown_workflow_video_lora_sampler_125
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.821313
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/infinite talk 数字人-音频驱动图片_2017646230746173442.json, 视频生成/图生视频/infinite tetalk音频+图生视频MTV_1959143275817021441.json, 视频生成/图生视频/infinitetalk数字人视频任意人物图片生成唱歌视频动作加强无限循环n分钟内不爆显存_1994005595265105922.json, 视频生成/图生视频/infintetalk合成唱歌视频_1990334829420007425.json, 视频生成/图生视频/【CQ808】单人静帧图对口型工作流_2011801795986722818.json, 视频生成/图生视频/图片人物对口型正式版_2002936132511907841.json, 视频生成/图生视频/图生视频 对口型数字人+最强音色克隆带语气情感+音频生成+数字人+声音克隆+情绪参考_2062720243771990018.json, 视频生成/图生视频/对口型数字人 最强音色克隆带语气情感 音频生成 数字人 声音克隆  情绪参考   Infinite+_2061287897743052801.json, 视频生成/图生视频/对口型数字人+最强音色克隆带语气情感+音频生成+数字人+声音克隆+情绪参考_2061971483555098625.json, 视频生成/图生视频/对口型数字人Infinite+talk对口型动态加强高版V3_1981308646988611586.json, 视频生成/图生视频/数字人 对口型最强音色克隆带语气情感 Infinite_2061625584001835010.json, 视频生成/图生视频/数字人 对口型最强音色克隆带语气情感 Infinite_2062437444791918594.json, 视频生成/图生视频/数字人 对口型最强音色克隆带语气情感 Infinite_2062801094731980801.json, 视频生成/图生视频/数字人 对口型最强音色克隆带语气情感 Infinite_2064624284164771842.json, 视频生成/图生视频/数字人 对口型最强音色克隆带语气情感 Infinite_2064954636120973313.json, 视频生成/图生视频/最强的数字人_2079549546333560833.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_125

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/infinite talk 数字人-音频驱动图片_2017646230746173442.json、视频生成/图生视频/infinite tetalk音频+图生视频MTV_1959143275817021441.json、视频生成/图生视频/infinitetalk数字人视频任意人物图片生成唱歌视频动作加强无限循环n分钟内不爆显存_1994005595265105922.json、视频生成/图生视频/infintetalk合成唱歌视频_1990334829420007425.json、视频生成/图生视频/【CQ808】单人静帧图对口型工作流_2011801795986722818.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 16 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
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
- `AudioCrop` —— 15/16 个有
- `GetImageSizeAndCount` —— 15/16 个有
- `PreviewAny` —— 15/16 个有
- `CR Prompt Text` —— 14/16 个有
- `JWFloat` —— 14/16 个有
- `JWInteger` —— 14/16 个有
- `AudioToFPS` —— 12/16 个有
- `LayerUtility: PurgeVRAM V2` —— 12/16 个有
- `easy showAnything` —— 12/16 个有
- `SetNode` —— 4/16 个有
- `GetNode` —— 3/16 个有
- `SaveAudio` —— 2/16 个有
- `Apply Whisper` —— 1/16 个有
- `Fast Groups Bypasser (rgthree)` —— 1/16 个有
- `Float` —— 1/16 个有
- `Int` —— 1/16 个有
- `LayerUtility: TextBox` —— 1/16 个有
- `OmniVoiceLongformTTS` —— 1/16 个有
- `OmniVoiceMultiSpeakerTTS` —— 1/16 个有
- `OmniVoiceVoiceDesignTTS` —— 1/16 个有
- `OmniVoiceWhisperLoader` —— 1/16 个有
- `PrimitiveStringMultiline` —— 1/16 个有
- `SeedVCRun` —— 1/16 个有
- `VHS_LoadVideo` —— 1/16 个有
- `easy int` —— 1/16 个有
- `workflow>2` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
