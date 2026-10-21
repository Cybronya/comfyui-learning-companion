---
name: unknown_workflow_video_lora_sampler_310
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.467714
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, PT_H3ConcatAVLatent, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3 二采优化版+Gemma4_2089334608109334530.json, 视频生成/图生视频/Minimax H3 二采首尾帧 + 参考音_2092200990517850113.json, 视频生成/图生视频/Minimax H3 参考生视频+高动态-自用版+可生成20s+视频_2107384460193918978.json, 视频生成/图生视频/Minimax H3 图_参考生视频+高动态_2095019320052117505.json, 视频生成/图生视频/Minimax H3 图生视频（二采）+1参考音【批量管理系统API用】_2093589690120228865.json, 视频生成/图生视频/Minimax H3 图生视频（无参考音）【批量管理系统api用】_2093586371775647745.json, 视频生成/图生视频/Minimax H3 提示词优化&视频画质优化_2087010732222279682.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_310

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Minimax H3 二采优化版+Gemma4_2089334608109334530.json、视频生成/图生视频/Minimax H3 二采首尾帧 + 参考音_2092200990517850113.json、视频生成/图生视频/Minimax H3 参考生视频+高动态-自用版+可生成20s+视频_2107384460193918978.json、视频生成/图生视频/Minimax H3 图_参考生视频+高动态_2095019320052117505.json、视频生成/图生视频/Minimax H3 图生视频（二采）+1参考音【批量管理系统API用】_2093589690120228865.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：47%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `PT_H3ConcatAVLatent`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVSeparateAVLatent` —— 6/7 个有
- `LayerUtility: PurgeVRAM V2` —— 6/7 个有
- `LoadAudio` —— 6/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/7 个有
- `Fast Groups Bypasser (rgthree)` —— 5/7 个有
- `H3SigmaRefiner` —— 5/7 个有
- `MiniMaxLowVRAMAttention` —— 5/7 个有
- `MinimaxH3LatentUpscaler3D` —— 5/7 个有
- `ResolutionSelector` —— 5/7 个有
- `SplitSigmas` —— 4/7 个有
- `easy showAnything` —— 4/7 个有
- `Any Switch (rgthree)` —— 2/7 个有
- `Any To String (mtb)` —— 2/7 个有
- `BatchImagesNode` —— 2/7 个有
- `FrameInterpolate` —— 2/7 个有
- `FrameInterpolationModelLoader` —— 2/7 个有
- `JoinStringMulti` —— 2/7 个有
- `LayerColor: Brightness & Contrast` —— 2/7 个有
- `StringConcatenate` —— 2/7 个有
- `BlockSparseAttention` —— 1/7 个有
- `H3LatentUpscaleByJingchen573` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `MiniMaxChunkFeedForward` —— 1/7 个有
- `ModelAttentionBackend` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `SolAttnPatch` —— 1/7 个有
- `TextGenerate` —— 1/7 个有
- `VAEEncode` —— 1/7 个有
- `VAEEncodeAudio` —— 1/7 个有
- `llama_cpp_instruct_adv` —— 1/7 个有
- `llama_cpp_model_loader` —— 1/7 个有
- `llama_cpp_parameters` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
