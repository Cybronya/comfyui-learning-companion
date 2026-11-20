---
name: unknown_workflow_lora_sampler_unet_146
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.829833
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/h3-万物比基尼_2117047552452419585.json, 平台全量/minimax_h3复刻短视频爆款_2094782500068487169.json, 视频生成/图生视频/H3 taomate 3步加速 中远距离不崩脸_2099163346699374593.json, 视频生成/图生视频/H3 角色替换_2085882691152605185.json, 视频生成/图生视频/H3视频衔接_2095145130473902082.json, 视频生成/图生视频/h3双采样高清流_2092571899955081218.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_146

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/h3-万物比基尼_2117047552452419585.json、平台全量/minimax_h3复刻短视频爆款_2094782500068487169.json、视频生成/图生视频/H3 taomate 3步加速 中远距离不崩脸_2099163346699374593.json、视频生成/图生视频/H3 角色替换_2085882691152605185.json、视频生成/图生视频/H3视频衔接_2095145130473902082.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `MiniMaxLowVRAMAttention` —— 5/6 个有
- `ModelAttentionBackend` —— 5/6 个有
- `PrimitiveFloat` —— 5/6 个有
- `SaveVideo` —— 5/6 个有
- `VAEDecodeAudio` —— 5/6 个有
- `VHS_LoadVideo` —— 4/6 个有
- `FlashVSRNode` —— 3/6 个有
- `H3SigmaRefiner` —— 3/6 个有
- `LTXVConcatAVLatent` —— 3/6 个有
- `LTXVSeparateAVLatent` —— 3/6 个有
- `MinimaxH3LatentUpscaler3D` —— 3/6 个有
- `ModelPreviewOverrideKJ` —— 3/6 个有
- `SaveImage` —— 3/6 个有
- `Sleep` —— 3/6 个有
- `SplitSigmas` —— 3/6 个有
- `MiniMaxChunkFeedForward` —— 2/6 个有
- `FL_UnloadAllModels` —— 1/6 个有
- `GetImageRangeFromBatch` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `MiniMaxH3AddGuide` —— 1/6 个有
- `MiniMaxH3PromptEnhancerT8` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `VHS_VideoCombine` —— 1/6 个有
- `easy seed` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
