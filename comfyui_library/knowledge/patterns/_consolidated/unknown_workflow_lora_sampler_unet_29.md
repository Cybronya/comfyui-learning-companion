---
name: unknown_workflow_lora_sampler_unet_29
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.583471
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, H3SigmaRefiner, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Minimax_H3_ref_顶级多参_v2_短剧向_2114729086584188929.json, 图片生成/图生图/Minimax_H3_ref_顶级多参_v2_短剧向_2115438049093054466.json, 图片生成/图生图/Minimax_H3_ref_顶级多参_v2_短剧向_2115662711223832578.json, 平台全量/minimax h3多参战斗视频v1_2092865544071499777.json, 视频生成/图生视频/H3 sigma强化+潜空间放大工作流_2089596339163320321.json, 视频生成/图生视频/H3 sigma强化+潜空间放大工作流_2091173937257472002.json, 视频生成/图生视频/H3 sigma强化_2090416810561728514.json, 视频生成/图生视频/MiniMax H3 sigma强化+潜空间放大工作流-小脸不崩-脸不油，高动态不崩脸_2093136040067428353.json, 视频生成/图生视频/MiniMax H3图生视频(多参考)_2091406664456040450.json, 视频生成/图生视频/MiniMax H3图生视频动作面部优化工作流_2089680420211347458.json, 视频生成/图生视频/MiniMax_H3_双采样潜空间放大直出1080p_2096948674386550786.json, 视频生成/图生视频/Minimax H3 人物电影级视频工作流（完美解决脸部崩坏问题）_2089732704005877761.json, 视频生成/图生视频/Minimax H3 图生视频 双采样+sigma强化 潜空间放大工作流 小脸不崩漫剧必备！_2089543355335274497.json, 视频生成/图生视频/Minimax H3 图生视频 双采样+sigma强化 潜空间放大工作流 小脸不崩漫剧必备！_2089917740520919041.json, 视频生成/图生视频/Minimax H3 脸不崩！打斗不糊！H3 sigma强化+超清放大，生成1080P视频，效果极佳，不过速度为普通流的2倍_2089537626373181442.json, 视频生成/图生视频/Minimax H3全能多模态--二采放大（加速+sigma强化）工作流_2092164749025964033.json, 视频生成/文生视频/H3 高清优化版-小脸不崩-运动不模糊_2089690104179810306.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_29

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/Minimax_H3_ref_顶级多参_v2_短剧向_2114729086584188929.json、图片生成/图生图/Minimax_H3_ref_顶级多参_v2_短剧向_2115438049093054466.json、图片生成/图生图/Minimax_H3_ref_顶级多参_v2_短剧向_2115662711223832578.json、平台全量/minimax h3多参战斗视频v1_2092865544071499777.json、视频生成/图生视频/H3 sigma强化+潜空间放大工作流_2089596339163320321.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 16/17 个有
- `GetNode` —— 15/17 个有
- `SetNode` —— 15/17 个有
- `BasicGuider` —— 14/17 个有
- `LTXVConcatAVLatent` —— 13/17 个有
- `LTXVSeparateAVLatent` —— 13/17 个有
- `ModelAttentionBackend` —— 13/17 个有
- `ModelPreviewOverrideKJ` —— 13/17 个有
- `SplitSigmas` —— 13/17 个有
- `SolAttnMiniMax` —— 12/17 个有
- `MinimaxH3LatentUpscaler3D` —— 6/17 个有
- `MinimaxH3LatentUpscalerNode3D` —— 6/17 个有
- `CFGGuider` —— 3/17 个有
- `CLIPTextEncode` —— 3/17 个有
- `Label (rgthree)` —— 3/17 个有
- `QwenH3PromptLocal` —— 3/17 个有
- `YC_ShowText` —— 3/17 个有
- `忽略多组孤海` —— 3/17 个有
- `MinimaxH3LatentUpscalerNode2D` —— 2/17 个有
- `Fast Groups Bypasser (rgthree)` —— 1/17 个有
- `Float` —— 1/17 个有
- `GetVideoComponents` —— 1/17 个有
- `H3DistanceAttentionPatcher` —— 1/17 个有
- `H3DynamicCFGScheduler` —— 1/17 个有
- `ImageResizeKJv2` —— 1/17 个有
- `LayerUtility: PurgeVRAM V2` —— 1/17 个有
- `LoadAudio` —— 1/17 个有
- `LoadVideo` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
