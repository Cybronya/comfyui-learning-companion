---
name: unknown_workflow_video_lora_sampler_278
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.47525
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, DirectorAudioFrameCalc, DirectorAudioScriptLoader, DirectorCasting, DirectorFinalRender, DirectorOrderGate, DirectorSceneIterator, DirectorStreamSaver, DirectorVideoPromptLoader, DirectorVisualStoryboardLoader, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetNode, INTConstant, JoinStringMulti, KSamplerAdvanced, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PainterI2VAdvanced, PathchSageAttentionKJ, PreviewAudio, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SetNode, ShowText|pysssss, TDQwen3TTSBatchGenerateSpeaker, TDQwen3TTSDefineSpeaker, TDQwen3TTSModelLoader, TDQwen3TTSMultiDialog, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2027602453616660482.json, 视频生成/图生视频/2026683306535817218.json, 视频生成/图生视频/2036343808945823745.json, 视频生成/图生视频/2021176958817673218.json, 视频生成/文生视频/半手动版 _ 动态漫自定义角色 _ 音色 _ 分镜 _ 台词 _ 视频_2065336611218481154.json, 视频生成/文生视频/半手动版本 _ 动态AI漫剧自定义角色 _ 音色 _ 分镜 _ 台词 _ 视频一键生成_2062869621941817346.json, 视频生成/文生视频/半手动版本动态AI漫剧自定义角色+音色+分镜+台词+视频一键生成_2065351903407591425.json, 视频生成/文生视频/空白工作流_2083489604925214722.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_278

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2027602453616660482.json、视频生成/图生视频/2026683306535817218.json、视频生成/图生视频/2036343808945823745.json、视频生成/图生视频/2021176958817673218.json、视频生成/文生视频/半手动版 _ 动态漫自定义角色 _ 音色 _ 分镜 _ 台词 _ 视频_2065336611218481154.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：48%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `DirectorAudioFrameCalc`
- `DirectorAudioScriptLoader`
- `DirectorCasting`
- `DirectorFinalRender`
- `DirectorOrderGate`
- `DirectorSceneIterator`
- `DirectorStreamSaver`
- `DirectorVideoPromptLoader`
- `DirectorVisualStoryboardLoader`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetNode`
- `INTConstant`
- `JoinStringMulti`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PainterI2VAdvanced`
- `PathchSageAttentionKJ`
- `PreviewAudio`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SetNode`
- `ShowText|pysssss`
- `TDQwen3TTSBatchGenerateSpeaker`
- `TDQwen3TTSDefineSpeaker`
- `TDQwen3TTSModelLoader`
- `TDQwen3TTSMultiDialog`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `RHHiddenNodes` —— 2/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 8 | 100% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler | - | 8 | 100% |
| 重绘幅度 | normal | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，8 个样本，一致性 100%
- 重绘幅度 最常用 normal，8 个样本，一致性 100%
