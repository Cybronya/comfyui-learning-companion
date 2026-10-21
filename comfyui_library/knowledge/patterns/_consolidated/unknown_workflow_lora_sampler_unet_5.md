---
name: unknown_workflow_lora_sampler_unet_5
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.600769
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1.MinimaxH3双采样V2版本（自用修改布局）！_2089749289575731202.json, 视频生成/图生视频/MiniMax H3五分钟生成1080p高清（可视化全模态高清输出）_2093962334623584257.json, 视频生成/图生视频/MiniMax H3全能参考，二采放大_2092138431697735681.json, 视频生成/图生视频/MiniMax H3全能插件+双采1080p高清（8步加速）8-30_2093712107018743809.json, 视频生成/图生视频/MiniMax H3全能插件+双采1080p高清（8步加速）8-30_2093741169816723457.json, 视频生成/图生视频/MiniMax_H3_双采样潜空间放大直出1080p_2096948674386550786.json, 视频生成/图生视频/Minimax H3 人物电影级视频工作流（完美解决脸部崩坏问题）_2089732704005877761.json, 视频生成/图生视频/Minimax H3 图生视频 双采样+sigma强化 潜空间放大工作流 小脸不崩漫剧必备！_2089543355335274497.json, 视频生成/图生视频/Minimax H3 图生视频 双采样+sigma强化 潜空间放大工作流 小脸不崩漫剧必备！_2089917740520919041.json, 视频生成/图生视频/Minimax H3全能多模态--二采放大（加速+sigma强化）工作流_2092164749025964033.json, 视频生成/图生视频/h3潜空间放大工作流老八_2089878151064276994.json, 视频生成/图生视频/minimaxH3海螺智能提示词优化加速双采样高清放大工作流_2093339172751888385.json, 视频生成/文生视频/minimaxH3海螺智能提示词优化加速双采样高清放大工作流-StarAI_2087299228723933186.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_5

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/1.MinimaxH3双采样V2版本（自用修改布局）！_2089749289575731202.json、视频生成/图生视频/MiniMax H3五分钟生成1080p高清（可视化全模态高清输出）_2093962334623584257.json、视频生成/图生视频/MiniMax H3全能参考，二采放大_2092138431697735681.json、视频生成/图生视频/MiniMax H3全能插件+双采1080p高清（8步加速）8-30_2093712107018743809.json、视频生成/图生视频/MiniMax H3全能插件+双采1080p高清（8步加速）8-30_2093741169816723457.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `H3SigmaRefiner` —— 12/13 个有
- `PrimitiveFloat` —— 12/13 个有
- `SolAttnMiniMax` —— 11/13 个有
- `VAEDecode` —— 11/13 个有
- `VAEDecodeAudio` —— 11/13 个有
- `ComfyMathExpression` —— 9/13 个有
- `GetNode` —— 9/13 个有
- `LoadImage` —— 9/13 个有
- `MiniMaxH3ReferenceToVideo` —— 9/13 个有
- `MinimaxH3LatentUpscaler3D` —— 9/13 个有
- `PrimitiveStringMultiline` —— 9/13 个有
- `SetNode` —— 9/13 个有
- `VHS_VideoCombine` —— 7/13 个有
- `CreateVideo` —— 6/13 个有
- `Label (rgthree)` —— 6/13 个有
- `SaveVideo` —— 6/13 个有
- `Fast Groups Bypasser (rgthree)` —— 5/13 个有
- `MiniMaxH3Unified` —— 4/13 个有
- `MinimaxH3LatentUpscalerNode3D` —— 4/13 个有
- `CR Text` —— 3/13 个有
- `ExtendIntermediateSigmas` —— 3/13 个有
- `LoraLoaderBypassModelOnly` —— 2/13 个有
- `MiniMaxH3AVDecodeT8` —— 2/13 个有
- `PathchSageAttentionKJ` —— 2/13 个有
- `ShowText|pysssss` —— 2/13 个有
- `StariAI-MiniMaxH3-Skill` —— 2/13 个有
- `孤海注释` —— 2/13 个有
- `CR Prompt Text` —— 1/13 个有
- `GetVideoComponents` —— 1/13 个有
- `JWStringToFloat` —— 1/13 个有
- `LayerUtility: PurgeVRAM V2` —— 1/13 个有
- `LoadAudio` —— 1/13 个有
- `LoadVideo` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
