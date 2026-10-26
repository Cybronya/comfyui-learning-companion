---
name: unknown_workflow_video_lora_sampler_1005
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8445
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Text, ComfyMathExpression, Fast Groups Bypasser (rgthree), ImageConcatMulti, ImageResizeKJv2, KSamplerSelect, LayerUtility: PurgeVRAM V2, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3AVDecodeT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PT_H3ConcatAVLatent, PixaromaLabel, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, ShowText|pysssss, Switch any [Crystools], UNETLoader, VAEEncode, VAELoader, VHS_VideoCombine, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3  Fl2va 双时钟采样 Turbo LORA 工作流_2089383100567605249.json, 视频生成/文生视频/MiniMax H3 双时钟采样 Turbo LORA 双采集多模态工作流_2087545682738630657.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1005

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3  Fl2va 双时钟采样 Turbo LORA 工作流_2089383100567605249.json、视频生成/文生视频/MiniMax H3 双时钟采样 Turbo LORA 双采集多模态工作流_2087545682738630657.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Text`
- `ComfyMathExpression`
- `Fast Groups Bypasser (rgthree)`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PT_H3ConcatAVLatent`
- `PixaromaLabel`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `ShowText|pysssss`
- `Switch any [Crystools]`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `AudioConcat` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `LoadVideoUI` —— 1/2 个有
- `MiniMaxH3ImageToVideo` —— 1/2 个有
- `MiniMaxH3ReferenceToVideo` —— 1/2 个有
- `Primitive boolean [Crystools]` —— 1/2 个有
- `TrimAudioDuration` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `VAEEncodeAudio` —— 1/2 个有
- `easy boolean` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
