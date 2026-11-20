---
name: unknown_workflow_lora_sampler_unet_327
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.418
common_nodes: [Any To String (mtb), AudioCrop, BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, Fast Groups Bypasser (rgthree), GetNode, ImageResizeKJv2, JjkText, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, ModelPreviewOverrideKJ, PreviewAudio, PrimitiveFloat, PrimitiveInt, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, easy clearCacheAll, easy int, easy seed, 孤海注释]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3极速版sigma强化+潜空间放大 （2采）可选提示词优化最多9图_3音频_3视频全能参考生视频 小脸不崩！打斗不糊！-优化_1960222169320075266.json, 视频生成/图生视频/迄今超强MiniMax-H3开源版 多图or最多9图_3音频_3视频全能参考图生视频数字人口播产品带货AI漫剧可选二采有效去油防脸崩2倍速+官方8步量化加速版_1977300673618419713.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_327

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3极速版sigma强化+潜空间放大 （2采）可选提示词优化最多9图_3音频_3视频全能参考生视频 小脸不崩！打斗不糊！-优化_1960222169320075266.json、视频生成/图生视频/迄今超强MiniMax-H3开源版 多图or最多9图_3音频_3视频全能参考图生视频数字人口播产品带货AI漫剧可选二采有效去油防脸崩2倍速+官方8步量化加速版_1977300673618419713.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：42%

## 共有节点

全部 2 个 workflow 都包含：
- `Any To String (mtb)`
- `AudioCrop`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `ImageResizeKJv2`
- `JjkText`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PreviewAudio`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `easy clearCacheAll`
- `easy int`
- `easy seed`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `H3SigmaRefiner` —— 1/2 个有
- `LTXVConcatAVLatent` —— 1/2 个有
- `LTXVSeparateAVLatent` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `MiniMaxH3SigmaShift` —— 1/2 个有
- `MinimaxH3LatentUpscaler3D` —— 1/2 个有
- `PT_H3ConcatAVLatent` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `SolAttnMiniMax` —— 1/2 个有
- `SplitSigmas` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `VAEEncodeAudio` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有
- `ZNGB_ImageBatchMulti` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有
- `llama_cpp_model_loader` —— 1/2 个有
- `llama_cpp_parameters` —— 1/2 个有
- `llama_cpp_unload_model` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
