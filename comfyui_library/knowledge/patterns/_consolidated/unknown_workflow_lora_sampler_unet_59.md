---
name: unknown_workflow_lora_sampler_unet_59
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.885545
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, Lora Loader Stack (rgthree), MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PixaromaSaveMp4, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SigmasToFloat, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [平台全量/MiniMax Ref2VA 角色替换 动作迁移_2091448414428028930.json, 视频生成/图生视频/MiniMax H3  8.20_2084615308018540545.json, 视频生成/图生视频/MiniMax H3  8.22_2091004876800217090.json, 视频生成/图生视频/MiniMax H3 全参考模式（多参专用）_2089144368086208514.json, 视频生成/图生视频/MiniMax H3 全参考模式（多参专用）_2095002353236795393.json, 视频生成/图生视频/MiniMax H3 双图参考生视频_2090580862466347010.json, 视频生成/图生视频/MiniMaxH3全参考模式+三采+sigma强化+潜空间放大_2089928928285773826.json, 视频生成/图生视频/Minimax H3 Latent采样放大8_18_2089383455539941377.json, 视频生成/图生视频/双4步 H3采样 8.17_2085295391691591682.json, 视频生成/文生视频/(ref)Minimax-H3全面优化模型工作流（动作_表情_动态模糊修复_特效）_2093928908566646786.json, 视频生成/文生视频/(ref)Minimax-H3官方4步究极高画质双采工作流（新模型）_2090053764232335361.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_59

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（平台全量/MiniMax Ref2VA 角色替换 动作迁移_2091448414428028930.json、视频生成/图生视频/MiniMax H3  8.20_2084615308018540545.json、视频生成/图生视频/MiniMax H3  8.22_2091004876800217090.json、视频生成/图生视频/MiniMax H3 全参考模式（多参专用）_2089144368086208514.json、视频生成/图生视频/MiniMax H3 全参考模式（多参专用）_2095002353236795393.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `Lora Loader Stack (rgthree)`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PixaromaSaveMp4`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SigmasToFloat`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 10/11 个有
- `ComfySwitchNode` —— 9/11 个有
- `DisableNoise` —— 9/11 个有
- `ExtendIntermediateSigmas` —— 9/11 个有
- `PrimitiveInt` —— 9/11 个有
- `easy boolean` —— 9/11 个有
- `LatentUpscaleBy` —— 8/11 个有
- `PrimitiveStringMultiline` —— 8/11 个有
- `GetImageRangeFromBatch` —— 7/11 个有
- `ImageResizeKJv2` —— 7/11 个有
- `VHS_LoadVideo` —— 7/11 个有
- `MiniMaxH3SigmaShift` —— 3/11 个有
- `SolAttnMiniMax` —— 3/11 个有
- `UniBlockSwap` —— 3/11 个有
- `VRAMReserver` —— 3/11 个有
- `MinimaxH3LatentUpscalerNode3D` —— 2/11 个有
- `ModelAttentionBackend` —— 2/11 个有
- `easy cleanGpuUsed` —— 2/11 个有
- `H3SigmaRefiner` —— 1/11 个有
- `MiniMaxH3AVDecodeT8` —— 1/11 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 1/11 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 1/11 个有
- `MinimaxH3LatentUpscaler3D` —— 1/11 个有
- `ModelPreviewOverrideKJ` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
