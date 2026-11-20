---
name: unknown_workflow_upscale_latent_upscale_lora_30
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.691364
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/minimaxh3-多参+latent二采_2090316749035106305.json, 图片生成/文生图/啊癫 minimaxh3极速版二采潜空间直接放大_2091125688710553601.json, 平台全量/H3_2115259037750226945.json, 平台全量/H3多场景_倒推版_2119461304372125697.json, 平台全量/minimaxh3 9图3视频3音频二采高清 8步lora_2093162980975403010.json, 数字人/数字人/老王房产专用流-Minimax+H3双模双采_2097619417130684417.json, 视频生成/图生视频/DG_图生视频（一张图+提示词）（H3 sigma强化+潜空间放大 参考生视频工作流_2094345515814178817.json, 视频生成/图生视频/DG_图生视频（三张图+提示词）（H3 sigma强化+潜空间放大 参考生视频工作流_2094347086996271105.json, 视频生成/图生视频/DG_图生视频（两张图+提示词）（H3 sigma强化+潜空间放大 参考生视频工作流_2094341092257914881.json, 视频生成/图生视频/DG_视频编辑（视频+提示词）（H3 sigma强化+潜空间放大 参考生视频工作流_2094349718418710529.json, 视频生成/文生视频/DG_文生视频（提示词生视频）（H3 sigma强化+潜空间放大 参考生视频工作流_2094343576493846530.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_30

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/minimaxh3-多参+latent二采_2090316749035106305.json、图片生成/文生图/啊癫 minimaxh3极速版二采潜空间直接放大_2091125688710553601.json、平台全量/H3_2115259037750226945.json、平台全量/H3多场景_倒推版_2119461304372125697.json、平台全量/minimaxh3 9图3视频3音频二采高清 8步lora_2093162980975403010.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 10/11 个有
- `H3SigmaRefiner` —— 10/11 个有
- `MiniMaxH3ReferenceToVideo` —— 10/11 个有
- `MiniMaxH3SigmaShift` —— 10/11 个有
- `UNETLoader` —— 10/11 个有
- `CreateVideo` —— 9/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/11 个有
- `SaveVideo` —— 9/11 个有
- `GetNode` —— 8/11 个有
- `LoadAudio` —— 8/11 个有
- `SetNode` —— 8/11 个有
- `VHS_VideoCombine` —— 8/11 个有
- `SolAttnMiniMax` —— 6/11 个有
- `VHS_LoadVideo` —— 6/11 个有
- `Getter` —— 5/11 个有
- `ImageConcanate` —— 5/11 个有
- `MiniMaxH3AVDecodeT8` —— 5/11 个有
- `PreviewAudio` —— 5/11 个有
- `RH_Translator` —— 5/11 个有
- `Setter` —— 5/11 个有
- `VHS_LoadVideoPath` —— 5/11 个有
- `WooshLoadFlow` —— 5/11 个有
- `WooshSample` —— 5/11 个有
- `WooshTextEncode` —— 5/11 个有
- `ExtendIntermediateSigmas` —— 2/11 个有
- `MiniMaxLowVRAMAttention` —— 2/11 个有
- `easy cleanGpuUsed` —— 2/11 个有
- `AudioAdjustVolume` —— 1/11 个有
- `AudioMerge` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `MiniMaxH3HybridLoader` —— 1/11 个有
- `MiniMaxH3Unified` —— 1/11 个有
- `SolAttnPatch` —— 1/11 个有
- `easy int` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
