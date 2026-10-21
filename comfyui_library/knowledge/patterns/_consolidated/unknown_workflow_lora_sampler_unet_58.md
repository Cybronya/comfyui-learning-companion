---
name: unknown_workflow_lora_sampler_unet_58
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.87
common_nodes: [AudioInfoNode, BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, INTConstant, ImageFromBatch+, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3SigmaShift, ModelAttentionBackend, PreviewAny, PreviewAudio, PrimitiveBoolean, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy batchAnything, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy ifElse, easy matchLine, easy mergeVideosFromPaths, easy minimaxH3ToVideo, easy multiTrackEditor, easy multiTrackInfoOutput, easy multiTrackTaskOutput, easy promptLine, easy saveVideo, easy seed, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMaxH3_EasyMedia_循环长视频_8步单采版_10ERros_2093011796692127746.json, 视频生成/图生视频/【合理动态】H3_EasyMedia_循环长视频_2096826034602729474.json, 视频生成/文生视频/MiniMaxH3_EasyMedia_循环长视频_2092586543155343362.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_58

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3_EasyMedia_循环长视频_8步单采版_10ERros_2093011796692127746.json、视频生成/图生视频/【合理动态】H3_EasyMedia_循环长视频_2096826034602729474.json、视频生成/文生视频/MiniMaxH3_EasyMedia_循环长视频_2092586543155343362.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioInfoNode`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `INTConstant`
- `ImageFromBatch+`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `PreviewAny`
- `PreviewAudio`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy batchAnything`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy ifElse`
- `easy matchLine`
- `easy mergeVideosFromPaths`
- `easy minimaxH3ToVideo`
- `easy multiTrackEditor`
- `easy multiTrackInfoOutput`
- `easy multiTrackTaskOutput`
- `easy promptLine`
- `easy saveVideo`
- `easy seed`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 2/3 个有
- `LTXVSeparateAVLatent` —— 2/3 个有
- `ManualSigmas` —— 2/3 个有
- `MinimaxH3LatentUpscaler3D` —— 2/3 个有
- `SplitSigmas` —— 2/3 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/3 个有
- `LoraLoaderBypassModelOnly` —— 1/3 个有
- `SolAttnMiniMax` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
