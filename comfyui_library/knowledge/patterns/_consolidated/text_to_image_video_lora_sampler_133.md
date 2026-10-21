---
name: text_to_image_video_lora_sampler_133
type: Text To Image
frequency: 5
level: strong
coverage: 0.5332
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize, GetNode, Int, JjkText, KSampler, KSamplerSelect, KepStringLiteral, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, PrimitiveFloat, PrimitiveStringMultiline, RTXVideoSuperResolution, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, easy clearCacheAll, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/全模态v2.0超频版 MiniMax H3舞蹈视频搭配新提示词增强_2106529812016881665.json, 视频生成/文生视频/全模态v2.0混合模型｜MiniMax H3极速二采官流加速强化_2091791683448041474.json, 视频生成/文生视频/全模态v2.0超频版 MiniMax H3舞蹈视频搭配新提示词增强_2095073732317507585.json, 视频生成/文生视频/首尾帧v2.0混合模型｜MiniMax H3 sigma增强官流加速_2091796776314560513.json, 视频生成/视频生视频/全模态v2.0超频版 MiniMax H3舞蹈视频搭配新提示词增强_2106529812016881665.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_133

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/全模态v2.0超频版 MiniMax H3舞蹈视频搭配新提示词增强_2106529812016881665.json、视频生成/文生视频/全模态v2.0混合模型｜MiniMax H3极速二采官流加速强化_2091791683448041474.json、视频生成/文生视频/全模态v2.0超频版 MiniMax H3舞蹈视频搭配新提示词增强_2095073732317507585.json、视频生成/文生视频/首尾帧v2.0混合模型｜MiniMax H3 sigma增强官流加速_2091796776314560513.json、视频生成/视频生视频/全模态v2.0超频版 MiniMax H3舞蹈视频搭配新提示词增强_2106529812016881665.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：53%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetNode`
- `Int`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `KepStringLiteral`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RTXVideoSuperResolution`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `easy clearCacheAll`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Float` —— 4/5 个有
- `LTXVConcatAVLatent` —— 4/5 个有
- `LTXVSeparateAVLatent` —— 4/5 个有
- `MathExpression|pysssss` —— 4/5 个有
- `MiniMaxH3ReferenceToVideo` —— 4/5 个有
- `MinimaxH3LatentUpscaler3D` —— 4/5 个有
- `SplitSigmas` —— 4/5 个有
- `VHS_LoadAudioUpload` —— 4/5 个有
- `VHS_LoadVideo` —— 4/5 个有
- `LoadAudioUI` —— 3/5 个有
- `MiniMaxChunkFeedForward` —— 3/5 个有
- `MiniMaxLowVRAMAttention` —— 3/5 个有
- `String Literal` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `llama_cpp_instruct_adv` —— 3/5 个有
- `llama_cpp_model_loader` —— 3/5 个有
- `llama_cpp_parameters` —— 3/5 个有
- `MiniMaxH3GenerationTailLoader` —— 2/5 个有
- `MiniMaxH3PromptEnhancer` —— 2/5 个有
- `UniBlockSwap` —— 2/5 个有
- `ExtendIntermediateSigmas` —— 1/5 个有
- `MiniMaxH3ImageToVideo` —— 1/5 个有
- `ResizeImageMaskNode` —— 1/5 个有
- `UnloadAllModels` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
