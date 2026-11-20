---
name: unknown_workflow_video_lora_sampler_1013
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.824
common_nodes: [AudioSeparation, CLIPVisionLoader, CR Text, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/Multi_InfiniteTalk （wan2.1测试-人物偏油）_1966047524211650562.json, 音频生成/音频生成/Multitalk单人唱歌数字人_1952348321673359361.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1013

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/Multi_InfiniteTalk （wan2.1测试-人物偏油）_1966047524211650562.json、音频生成/音频生成/Multitalk单人唱歌数字人_1952348321673359361.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Text`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Audio Cut (mtb)` —— 1/2 个有
- `AudioCrop` —— 1/2 个有
- `CM_FloatToNumber` —— 1/2 个有
- `CM_NumberToFloat` —— 1/2 个有
- `Float` —— 1/2 个有
- `Int` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SaveAudio` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `WanVideoBlockSwap` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
