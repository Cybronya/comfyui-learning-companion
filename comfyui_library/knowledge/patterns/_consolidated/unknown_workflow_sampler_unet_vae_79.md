---
name: unknown_workflow_sampler_unet_vae_79
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.671545
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3  8.20_2084615308018540545.json, 视频生成/图生视频/MiniMax H3  8.22_2091004876800217090.json, 视频生成/图生视频/MiniMax H3图生视频动作面部优化工作流_2089680420211347458.json, 视频生成/图生视频/MiniMaxH3+lightx2v加速不油版-单双采_2084916996847792130.json, 视频生成/图生视频/MiniMax_H3_双采样潜空间放大直出1080p_2096948674386550786.json, 视频生成/图生视频/Minimax H3 人物电影级视频工作流（完美解决脸部崩坏问题）_2089732704005877761.json, 视频生成/图生视频/Minimax H3 图生视频 双采样+sigma强化 潜空间放大工作流 小脸不崩漫剧必备！_2089543355335274497.json, 视频生成/图生视频/Minimax H3 图生视频 双采样+sigma强化 潜空间放大工作流 小脸不崩漫剧必备！_2089917740520919041.json, 视频生成/图生视频/Minimax H3 多图参考 真实感极佳_2092151387793747970.json, 视频生成/图生视频/Minimax H3 脸不崩！打斗不糊！H3 sigma强化+超清放大，生成1080P视频，效果极佳，不过速度为普通流的2倍_2089537626373181442.json, 视频生成/图生视频/Minimax H3全能多模态--二采放大（加速+sigma强化）工作流_2092164749025964033.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_79

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3  8.20_2084615308018540545.json、视频生成/图生视频/MiniMax H3  8.22_2091004876800217090.json、视频生成/图生视频/MiniMax H3图生视频动作面部优化工作流_2089680420211347458.json、视频生成/图生视频/MiniMaxH3+lightx2v加速不油版-单双采_2084916996847792130.json、视频生成/图生视频/MiniMax_H3_双采样潜空间放大直出1080p_2096948674386550786.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：67%

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
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 9/11 个有
- `H3SigmaRefiner` —— 9/11 个有
- `LoraLoaderModelOnly` —— 9/11 个有
- `ModelAttentionBackend` —— 9/11 个有
- `ModelPreviewOverrideKJ` —— 9/11 个有
- `SaveVideo` —— 9/11 个有
- `PrimitiveStringMultiline` —— 8/11 个有
- `SolAttnMiniMax` —— 8/11 个有
- `GetNode` —— 7/11 个有
- `SetNode` —— 7/11 个有
- `MinimaxH3LatentUpscaler3D` —— 6/11 个有
- `MinimaxH3LatentUpscalerNode3D` —— 5/11 个有
- `LoadAudio` —— 3/11 个有
- `easy cleanGpuUsed` —— 3/11 个有
- `Fast Groups Bypasser (rgthree)` —— 2/11 个有
- `Label (rgthree)` —— 2/11 个有
- `Lora Loader Stack (rgthree)` —— 2/11 个有
- `PixaromaSaveMp4` —— 2/11 个有
- `SigmasToFloat` —— 2/11 个有
- `Float` —— 1/11 个有
- `GetVideoComponents` —— 1/11 个有
- `LayerUtility: PurgeVRAM V2` —— 1/11 个有
- `LoadVideo` —— 1/11 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 1/11 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 1/11 个有
- `MiniMaxLowVRAMAttention` —— 1/11 个有
- `MinimaxH3LatentUpscalerNode2D` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
