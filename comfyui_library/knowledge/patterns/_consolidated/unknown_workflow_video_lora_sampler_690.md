---
name: unknown_workflow_video_lora_sampler_690
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.964667
common_nodes: [AudioCrop, AudioSeparation, CR Text, HuMoEmbeds, ImpactInt, JWIntegerToString, LoadAudio, LoadWanVideoT5TextEncoder, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, WhisperModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/1969293960176934913.json, 视频生成/图生视频/1968957972288323586.json, 音频生成/音频生成/👽HuMo音频直接生成视频👽_1969277777063145473.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_690

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1969293960176934913.json、视频生成/图生视频/1968957972288323586.json、音频生成/音频生成/👽HuMo音频直接生成视频👽_1969277777063145473.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CR Text`
- `HuMoEmbeds`
- `ImpactInt`
- `JWIntegerToString`
- `LoadAudio`
- `LoadWanVideoT5TextEncoder`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `WhisperModelLoader`

**可变部分**（部分 workflow 才有）：
- `CreateCFGScheduleFloatList` —— 2/3 个有
- `ImageBatchMulti` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `Note Plus (mtb)` —— 2/3 个有
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `easy imageRemBg` —— 2/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImageFromBatch` —— 1/3 个有
- `MultiTalkModelLoader` —— 1/3 个有
- `MultiTalkWav2VecEmbeds` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `WanVideoCombineEmbeds` —— 1/3 个有
- `WanVideoImageToVideoMultiTalk` —— 1/3 个有
- `Wav2VecModelLoader` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
