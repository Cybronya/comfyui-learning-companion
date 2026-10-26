---
name: unknown_workflow_video_lora_sampler_650
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.889
common_nodes: [ComfyNumberConvert, Int, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, LongCatAvatarWhisperEmbeds, SimpleMath+, Text, TrimAudioDuration, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoVAELoader, WhisperModelLoader]
problems: []
missing: []
members: [数字人/数字人/LongCat1.5--数字人对口型_2059893332653985793.json, 视频生成/图生视频/LongCat1.5--数字人对口型_2059078929838854146.json, 视频生成/图生视频/LongCat1.5--数字人对口型_2059921141237641218.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_650

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/LongCat1.5--数字人对口型_2059893332653985793.json、视频生成/图生视频/LongCat1.5--数字人对口型_2059078929838854146.json、视频生成/图生视频/LongCat1.5--数字人对口型_2059921141237641218.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `ComfyNumberConvert`
- `Int`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LongCatAvatarWhisperEmbeds`
- `SimpleMath+`
- `Text`
- `TrimAudioDuration`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `WhisperModelLoader`

**可变部分**（部分 workflow 才有）：
- `Float` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `Audio Duration (mtb)` —— 1/3 个有
- `CreateVideo` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `SaveVideo` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
