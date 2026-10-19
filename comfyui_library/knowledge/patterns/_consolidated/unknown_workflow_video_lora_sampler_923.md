---
name: unknown_workflow_video_lora_sampler_923
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.618
common_nodes: [AudioCrop, AudioSeparation, DownloadAndLoadWav2VecModel, GetNode, INTConstant, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/1958462983561232386.json, 视频生成/文生视频/Infinitetalk表情迁移（文生视频）_2072999635486285824.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_923

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/1958462983561232386.json、视频生成/文生视频/Infinitetalk表情迁移（文生视频）_2072999635486285824.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：62%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `INTConstant`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
