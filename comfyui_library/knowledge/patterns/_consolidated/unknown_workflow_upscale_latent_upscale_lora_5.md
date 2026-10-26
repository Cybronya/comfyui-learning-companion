---
name: unknown_workflow_upscale_latent_upscale_lora_5
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.723
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/H3高质量全能参考（二采加速版）_2088785262628397058.json, 视频生成/图生视频/MiniMax H3数字人视频带货！多图生视频_2102748591906451458.json, 视频生成/图生视频/MiniMax-H3 数字人视频带货-多图参考生视频_2096052002777288705.json, 视频生成/图生视频/MiniMax-H3_ Digital Avatars for Video E-co数字人视频带货_2108137283806392322.json, 视频生成/图生视频/MiniMax-H3_ Digital Avatars for Video E-co数字人视频带货_2108165309235548162.json, 视频生成/图生视频/MiniMax-H3_ Digital Avatars for Video E-co数字人视频带货！_2095315877355937794.json, 视频生成/图生视频/MiniMax-H3_ 数字人视频带货！_2097134810035740673.json, 视频生成/图生视频/MiniMax-H3_Digital_Avatars_for_Video_E-co数字人视频带货_2110655333088710658.json, 视频生成/图生视频/MiniMax-H3开源 数字人视频带货 H3多图生视频_2097991965936799745.json, 视频生成/图生视频/MiniMax-H3开源 数字人视频带货 H3多图生视频_2098027200141414401.json, 视频生成/图生视频/MiniMax-H3开源 数字人视频带货 H3多图生视频_2104158521985163265.json, 视频生成/图生视频/MiniMax-H3开源 数字人视频带货 H3多图生视频_2104200339196047362.json, 视频生成/图生视频/MiniMaxH3  数字人视频带货  H3多图生视频_2097942688929767426.json, 视频生成/图生视频/MiniMaxH3 图生视频！2K快速版！_2103052957838307329.json, 视频生成/图生视频/MiniMaxH3_MV采样器直出对嘴形_10+3高动态Latent_upscale_2091535367416664065.json, 视频生成/图生视频/minimax_h3_fast-清晰武戏-四图_2109487427214733314.json, 视频生成/图生视频/多图生视频，超强数字人视频带货！可用于多人场景视频制作_2103095600538546178.json, 视频生成/图生视频/小脸不崩！打斗不糊！H3 sigma强化+潜空间放大工作流（不油啦！）_2089513420025589761.json, 视频生成/图生视频/小脸不崩！打斗不糊！H3 sigma强化+潜空间放大工作流（不油啦！）_2114208903440453633.json, 视频生成/文生视频/海螺二采直出1080P视频H3 sigma强化+潜空间2倍放大（Remix融合模型去油腻）_2091655065831563265.json, 视频生成/文生视频/（0824）万象AI+海螺二采直出1080P（自动提示词）_2091672393700962305.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_5

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（视频生成/图生视频/H3高质量全能参考（二采加速版）_2088785262628397058.json、视频生成/图生视频/MiniMax H3数字人视频带货！多图生视频_2102748591906451458.json、视频生成/图生视频/MiniMax-H3 数字人视频带货-多图参考生视频_2096052002777288705.json、视频生成/图生视频/MiniMax-H3_ Digital Avatars for Video E-co数字人视频带货_2108137283806392322.json、视频生成/图生视频/MiniMax-H3_ Digital Avatars for Video E-co数字人视频带货_2108165309235548162.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 21 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 20/21 个有
- `GetNode` —— 19/21 个有
- `SetNode` —— 19/21 个有
- `VHS_VideoCombine` —— 17/21 个有
- `ManualSigmas` —— 16/21 个有
- `JjkText` —— 14/21 个有
- `MiniMaxH3SigmaShift` —— 8/21 个有
- `PrimitiveStringMultiline` —— 8/21 个有
- `ModelAttentionBackend` —— 7/21 个有
- `ModelPreviewOverrideKJ` —— 6/21 个有
- `SplitSigmas` —— 6/21 个有
- `CreateVideo` —— 5/21 个有
- `SaveVideo` —— 5/21 个有
- `H3SigmaRefiner` —— 4/21 个有
- `LoadAudio` —— 4/21 个有
- `RHLLMChatNode` —— 3/21 个有
- `BlockSparseAttention` —— 2/21 个有
- `JjkShowText` —— 2/21 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/21 个有
- `easy showAnything` —— 2/21 个有
- `AudioCrop` —— 1/21 个有
- `AudioInfoNode` —— 1/21 个有
- `Float` —— 1/21 个有
- `Int` —— 1/21 个有
- `PreviewAudio` —— 1/21 个有
- `QwenH3PromptLocal` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
