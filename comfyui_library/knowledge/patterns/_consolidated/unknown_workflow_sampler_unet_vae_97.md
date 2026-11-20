---
name: unknown_workflow_sampler_unet_vae_97
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.8645
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, KSamplerSelect, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/H3+pika 极速文生视频_2116147294390284289.json, 视频生成/文生视频/H3-文生视频_2088176717721591810.json, 视频生成/文生视频/H3-氛围感短视频_2096431562895220737.json, 视频生成/文生视频/H3-氛围感网红打卡点短视频制作_2096832540542857218.json, 视频生成/文生视频/H3基础模式_10步+3步Latent Upscaler_2090818143013924865.json, 视频生成/文生视频/H3文生视频Tao 3步lora二采RES4LYF_2100959295356628994.json, 视频生成/文生视频/MiniMax H3 FL2VA｜文生+首尾帧全能视频_2090027189914918914.json, 视频生成/文生视频/MiniMax H3 Ref2VA｜多参考全能视频生成_2090060185078419458.json, 视频生成/文生视频/Minimax H3 多参生视频潜空间放大二采_2093173371193352193.json, 视频生成/文生视频/Minimax H3多参 Taomate 3 steplora 二采生视频_2100938444443832322.json, 视频生成/文生视频/人物真实低动态H3+sigma强化+潜空间放大工作流 双采_2096114490512330753.json, 视频生成/文生视频/海螺H3-高效4步-脸部护持_2091172705780461570.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_97

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/文生视频/H3+pika 极速文生视频_2116147294390284289.json、视频生成/文生视频/H3-文生视频_2088176717721591810.json、视频生成/文生视频/H3-氛围感短视频_2096431562895220737.json、视频生成/文生视频/H3-氛围感网红打卡点短视频制作_2096832540542857218.json、视频生成/文生视频/H3基础模式_10步+3步Latent Upscaler_2090818143013924865.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 11/12 个有
- `PrimitiveFloat` —— 11/12 个有
- `CreateVideo` —— 10/12 个有
- `LoadImage` —— 10/12 个有
- `BasicScheduler` —— 9/12 个有
- `SaveVideo` —— 9/12 个有
- `LTXVConcatAVLatent` —— 8/12 个有
- `LTXVSeparateAVLatent` —— 8/12 个有
- `MiniMaxH3SigmaShift` —— 8/12 个有
- `MinimaxH3LatentUpscaler3D` —— 8/12 个有
- `ModelPreviewOverrideKJ` —— 8/12 个有
- `PrimitiveStringMultiline` —— 8/12 个有
- `ManualSigmas` —— 7/12 个有
- `MiniMaxH3ReferenceToVideo` —— 7/12 个有
- `ModelAttentionBackend` —— 7/12 个有
- `SplitSigmas` —— 6/12 个有
- `MiniMaxH3ImageToVideo` —— 5/12 个有
- `VHS_VideoCombine` —— 5/12 个有
- `H3SigmaRefiner` —— 4/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/12 个有
- `Text` —— 3/12 个有
- `AudioCrop` —— 2/12 个有
- `ClownsharKSampler_Beta` —— 2/12 个有
- `ConditioningZeroOut` —— 2/12 个有
- `LoadAudio` —— 2/12 个有
- `SeedGenerator` —— 2/12 个有
- `StringFunction|pysssss` —— 2/12 个有
- `VHS_LoadVideo` —— 2/12 个有
- `easy showAnything` —— 2/12 个有
- `FloatConstant` —— 1/12 个有
- `INTConstant` —— 1/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `MiniMaxChunkFeedForward` —— 1/12 个有
- `PrimitiveInt` —— 1/12 个有
- `RHLLMChatNode` —— 1/12 个有
- `忽略多组孤海` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | simple | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 100% |
| 采样算法 | 3 | - | 2 | 100% |
| 调度器 | 1 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 simple，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
