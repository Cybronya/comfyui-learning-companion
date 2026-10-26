---
name: unknown_workflow_video_lora_sampler_996
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.953
common_nodes: [AudioCrop, AudioSeparation, CR Text, CreateCFGScheduleFloatList, HuMoEmbeds, ImpactInt, JWIntegerToString, LoadAudio, LoadWanVideoT5TextEncoder, Note Plus (mtb), SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, WhisperModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/👽HuMo电商展示产品+口播👽_1969293960176934913.json, 音频生成/音频生成/👽HuMo音频直接生成视频👽_1969277777063145473.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_996

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/👽HuMo电商展示产品+口播👽_1969293960176934913.json、音频生成/音频生成/👽HuMo音频直接生成视频👽_1969277777063145473.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CR Text`
- `CreateCFGScheduleFloatList`
- `HuMoEmbeds`
- `ImpactInt`
- `JWIntegerToString`
- `LoadAudio`
- `LoadWanVideoT5TextEncoder`
- `Note Plus (mtb)`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WhisperModelLoader`

**可变部分**（部分 workflow 才有）：
- `ImageBatchMulti` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
