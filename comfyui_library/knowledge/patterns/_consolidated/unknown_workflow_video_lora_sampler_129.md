---
name: unknown_workflow_video_lora_sampler_129
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.827308
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, CR Prompt Text, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, PreviewAny, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1988227930037903361.json, 视频生成/图生视频/2002936132511907841.json, 视频生成/图生视频/2062720243771990018.json, 视频生成/图生视频/2047405386377990145.json, 视频生成/图生视频/2061287897743052801.json, 视频生成/图生视频/2061971483555098625.json, 视频生成/图生视频/对口型数字人Infinite+talk对口型动态加强高版V3_1981308646988611586.json, 视频生成/图生视频/2061625584001835010.json, 视频生成/图生视频/2062437444791918594.json, 视频生成/图生视频/2062801094731980801.json, 视频生成/图生视频/2064624284164771842.json, 视频生成/图生视频/2064954636120973313.json, 视频生成/图生视频/2079549546333560833.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_129

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/1988227930037903361.json、视频生成/图生视频/2002936132511907841.json、视频生成/图生视频/2062720243771990018.json、视频生成/图生视频/2047405386377990145.json、视频生成/图生视频/2061287897743052801.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 13 个 workflow 都包含：
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
- `PreviewAny`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `MultiTalkWav2VecEmbeds` —— 12/13 个有
- `WanVideoModelLoader` —— 12/13 个有
- `AudioToFPS` —— 11/13 个有
- `JWFloat` —— 11/13 个有
- `LayerUtility: PurgeVRAM V2` —— 11/13 个有
- `easy showAnything` —— 11/13 个有
- `GetNode` —— 2/13 个有
- `SetNode` —— 2/13 个有
- `Apply Whisper` —— 1/13 个有
- `CLIPTextEncode` —— 1/13 个有
- `Fast Groups Bypasser (rgthree)` —— 1/13 个有
- `ImageBatch` —— 1/13 个有
- `ImageFromBatch` —— 1/13 个有
- `KSampler` —— 1/13 个有
- `OmniVoiceLongformTTS` —— 1/13 个有
- `OmniVoiceMultiSpeakerTTS` —— 1/13 个有
- `OmniVoiceVoiceDesignTTS` —— 1/13 个有
- `OmniVoiceWhisperLoader` —— 1/13 个有
- `RHHiddenNodes` —— 1/13 个有
- `SaveAudio` —— 1/13 个有
- `VAEDecode` —— 1/13 个有
- `WanInfiniteTalkToVideo` —— 1/13 个有
- `easy indexAnything` —— 1/13 个有
- `workflow>2` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | normal | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
