---
name: unknown_workflow_video_lora_sampler_613
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.858
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Text, ComfyMathExpression, Fast Groups Bypasser (rgthree), ImageConcatMulti, ImageResizeKJv2, KSamplerSelect, LayerUtility: PurgeVRAM V2, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3AVDecodeT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PT_H3ConcatAVLatent, PixaromaLabel, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, ShowText|pysssss, Switch any [Crystools], UNETLoader, VAEEncode, VAELoader, VHS_VideoCombine, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3  Fl2va 双时钟采样 Turbo LORA 工作流_2089383100567605249.json, 视频生成/文生视频/MiniMax H3  Fl2va 双时钟采样 Turbo LORA 工作流_2089383100567605249.json, 视频生成/文生视频/MiniMax H3 双时钟采样 Turbo LORA 双采集多模态工作流_2087545682738630657.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_613

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3  Fl2va 双时钟采样 Turbo LORA 工作流_2089383100567605249.json、视频生成/文生视频/MiniMax H3  Fl2va 双时钟采样 Turbo LORA 工作流_2089383100567605249.json、视频生成/文生视频/MiniMax H3 双时钟采样 Turbo LORA 双采集多模态工作流_2087545682738630657.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
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
- `MiniMaxH3ImageToVideo` —— 2/3 个有
- `Primitive boolean [Crystools]` —— 2/3 个有
- `AudioConcat` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `LoadVideoUI` —— 1/3 个有
- `MiniMaxH3ReferenceToVideo` —— 1/3 个有
- `TrimAudioDuration` —— 1/3 个有
- `VAEDecode` —— 1/3 个有
- `VAEEncodeAudio` —— 1/3 个有
- `easy boolean` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
