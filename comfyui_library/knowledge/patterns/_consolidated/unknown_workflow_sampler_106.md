---
name: unknown_workflow_sampler_106
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7825
common_nodes: [CR Prompt Text, CreateVideo, FunCineForge_SM_KSampler, FunCineForge_SM_Model, FunCineForge_SM_Predata, FunCineForge_SM_Segments, GetVideoComponents, LoadAudio, PreviewAny, Qwen3ASRLoader, Qwen3ASRTranscribe, SaveAudio, SaveVideo, ShowAnything|Mie, VHS_LoadVideo, VHS_VideoInfoLoaded, Video Slice, easy anythingIndexSwitch, easy cleanGpuUsed]
problems: []
missing: []
members: [音频生成/音频生成/FunCineForge电影配音修正系统全自动版V3_2038491012061990913.json, 音频生成/音频生成/（自动时长版-音画同步25FPS）FunCineForge电影配音修正系统全自动版V3_2038520073069006850.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_106

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/FunCineForge电影配音修正系统全自动版V3_2038491012061990913.json、音频生成/音频生成/（自动时长版-音画同步25FPS）FunCineForge电影配音修正系统全自动版V3_2038520073069006850.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `CreateVideo`
- `FunCineForge_SM_KSampler`
- `FunCineForge_SM_Model`
- `FunCineForge_SM_Predata`
- `FunCineForge_SM_Segments`
- `GetVideoComponents`
- `LoadAudio`
- `PreviewAny`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `SaveAudio`
- `SaveVideo`
- `ShowAnything|Mie`
- `VHS_LoadVideo`
- `VHS_VideoInfoLoaded`
- `Video Slice`
- `easy anythingIndexSwitch`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Float` —— 1/2 个有
- `VHS_GetImageCount` —— 1/2 个有
- `Video Duration Calculator` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
