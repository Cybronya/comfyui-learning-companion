---
name: unknown_workflow_video_lora_sampler_1173
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.709
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CompressImages, CreateVideo, GetVideoComponents, JjkText, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PreviewAny, PrimitiveStringMultiline, RIFE VFI, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, ShowAnything|Mie, Text, UNETLoader, UnloadAllModels, VAEDecode, VAELoader, VHS_LoadVideo, VHS_SelectFilename, VHS_VideoCombine, VHS_VideoInfoLoaded, VideoInfoSource, easy cleanGpuUsed, easy clearCacheAll, easy promptReplace, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/舞蹈_摇香舞_2.5D卡通版_2116375094497996802.json, 视频生成/文生视频/舞蹈 摇香舞 2.5D卡通版_2114712699501371394.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1173

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/舞蹈_摇香舞_2.5D卡通版_2116375094497996802.json、视频生成/文生视频/舞蹈 摇香舞 2.5D卡通版_2114712699501371394.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CompressImages`
- `CreateVideo`
- `GetVideoComponents`
- `JjkText`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `RIFE VFI`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `ShowAnything|Mie`
- `Text`
- `UNETLoader`
- `UnloadAllModels`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `VideoInfoSource`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy promptReplace`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Int` —— 1/2 个有
- `UnloadModel` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有
- `llama_cpp_model_loader` —— 1/2 个有
- `llama_cpp_parameters` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
