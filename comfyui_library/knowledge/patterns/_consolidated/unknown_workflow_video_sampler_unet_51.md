---
name: unknown_workflow_video_sampler_unet_51
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.5195
common_nodes: [Any Switch (rgthree), BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, Fast Groups Bypasser (rgthree), GetNode, JoinStringMulti, KSamplerSelect, LoadAudio, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, StringConcatenate, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3图片加音色参考生视频-自动提示词优化-V1_2086980450555355138.json, 视频生成/图生视频/MiniMax H3图片加音色参考生视频-自动提示词优化-V2.1_2083091369735843842.json, 视频生成/图生视频/Minimax H3 二采优化版+Gemma4_2089334608109334530.json, 视频生成/图生视频/Minimax H3 提示词优化&视频画质优化_2087010732222279682.json, 视频生成/图生视频/绘影-MiniMax H3 参考生视频-混合25-49-int8-720P-V2_2102552907047596033.json, 视频生成/文生视频/H3 全能多参+4步加速+提示词优化_2087394908050124802.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_51

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3图片加音色参考生视频-自动提示词优化-V1_2086980450555355138.json、视频生成/图生视频/MiniMax H3图片加音色参考生视频-自动提示词优化-V2.1_2083091369735843842.json、视频生成/图生视频/Minimax H3 二采优化版+Gemma4_2089334608109334530.json、视频生成/图生视频/Minimax H3 提示词优化&视频画质优化_2087010732222279682.json、视频生成/图生视频/绘影-MiniMax H3 参考生视频-混合25-49-int8-720P-V2_2102552907047596033.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 6 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `JoinStringMulti`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `StringConcatenate`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 5/6 个有
- `llama_cpp_instruct_adv` —— 5/6 个有
- `llama_cpp_model_loader` —— 5/6 个有
- `llama_cpp_parameters` —— 5/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/6 个有
- `PurgeVRAM_UTK` —— 4/6 个有
- `ToString` —— 4/6 个有
- `MiniMaxH3SigmaShift` —— 3/6 个有
- `Any To String (mtb)` —— 2/6 个有
- `ModelAttentionBackend` —— 2/6 个有
- `PT_H3ConcatAVLatent` —— 2/6 个有
- `PrimitiveInt` —— 2/6 个有
- `H3LatentUpscaleByJingchen573` —— 1/6 个有
- `H3SigmaRefiner` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `LTXVSeparateAVLatent` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `MiniMaxChunkFeedForward` —— 1/6 个有
- `MiniMaxLowVRAMAttention` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `SplitSigmas` —— 1/6 个有
- `TextGenerate` —— 1/6 个有
- `VAEEncode` —— 1/6 个有
- `VAEEncodeAudio` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有
- `ZNGB_ImageBatchMulti` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
