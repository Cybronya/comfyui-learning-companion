---
name: unknown_workflow_lora_sampler_vae_13
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.5525
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, GetNode, H3SigmaRefiner, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SetNode, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/全能参考二次采样_MInimaxH3_2090972732266733570.json, 视频生成/文生视频/啊癫 minimaxh3极速版二采潜空间直接放大（去油版）_2093957991434379265.json, 视频生成/文生视频/收藏级！H3 加速+二采+打斗全能工作流拆解系列05集_2092970619469123586.json, 视频生成/文生视频/海螺H3 sigma强化+潜空间放大+高清人脸工作流_2089624110652551169.json, 视频生成/文生视频/海螺H3优化 小脸 打斗 浅空间_2091512771916681217.json, 视频生成/文生视频/海螺二采直出1080P视频H3 sigma强化+潜空间2倍放大（Remix融合模型去油腻）_2091655065831563265.json, 视频生成/文生视频/（0824）万象AI+海螺二采直出1080P（自动提示词）_2091672393700962305.json, 视频生成/文生视频/🔪🔪H3突破15秒！长视频不劣化！工作流拆解系列06集_2093951850499366914.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_13

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/全能参考二次采样_MInimaxH3_2090972732266733570.json、视频生成/文生视频/啊癫 minimaxh3极速版二采潜空间直接放大（去油版）_2093957991434379265.json、视频生成/文生视频/收藏级！H3 加速+二采+打斗全能工作流拆解系列05集_2092970619469123586.json、视频生成/文生视频/海螺H3 sigma强化+潜空间放大+高清人脸工作流_2089624110652551169.json、视频生成/文生视频/海螺H3优化 小脸 打斗 浅空间_2091512771916681217.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `GetNode`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetNode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 7/8 个有
- `LTXVSeparateAVLatent` —— 7/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/8 个有
- `MiniMaxH3SigmaShift` —— 7/8 个有
- `ModelAttentionBackend` —— 7/8 个有
- `ModelPreviewOverrideKJ` —— 7/8 个有
- `UNETLoader` —— 7/8 个有
- `VAEDecode` —— 7/8 个有
- `VAEDecodeAudio` —— 7/8 个有
- `SplitSigmas` —— 6/8 个有
- `LoadAudio` —— 5/8 个有
- `MinimaxH3LatentUpscaler3D` —— 5/8 个有
- `SolAttnMiniMax` —— 3/8 个有
- `easy showAnything` —— 3/8 个有
- `RHLLMChatNode` —— 2/8 个有
- `VHS_LoadVideo` —— 2/8 个有
- `孤海注释` —— 2/8 个有
- `ExtendIntermediateSigmas` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `Fast Groups Muter (rgthree)` —— 1/8 个有
- `GetImageRangeFromBatch` —— 1/8 个有
- `H3LatentUpscaleByJingchen573` —— 1/8 个有
- `MiniMaxH3AVDecodeT8` —— 1/8 个有
- `MiniMaxH3AddGuide` —— 1/8 个有
- `MiniMaxH3HybridLoader` —— 1/8 个有
- `MiniMaxLowVRAMAttention` —— 1/8 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/8 个有
- `VHS_VideoCombine` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
