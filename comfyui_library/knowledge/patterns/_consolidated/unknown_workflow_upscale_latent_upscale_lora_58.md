---
name: unknown_workflow_upscale_latent_upscale_lora_58
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.50925
common_nodes: [AudioCrop, BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, Fast Groups Bypasser (rgthree), GetNode, H3SigmaRefiner, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LayerUtility: PurgeVRAM, LoadAudio, LoadImage, LoraLoader, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveInt, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, ShowText|pysssss, Text Concatenate, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, easy positive]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 武打工作流_2096150765550260225.json, 视频生成/文生视频/MiniMax H3 武打工作流（多关键帧）_2095514314022150146.json, 视频生成/文生视频/MiniMax H3｜8步武术动作控制_2099893746019168258.json, 视频生成/文生视频/Minimax h3多参考双采打斗工作流_2095211630756974594.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_58

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 武打工作流_2096150765550260225.json、视频生成/文生视频/MiniMax H3 武打工作流（多关键帧）_2095514314022150146.json、视频生成/文生视频/MiniMax H3｜8步武术动作控制_2099893746019168258.json、视频生成/文生视频/Minimax h3多参考双采打斗工作流_2095211630756974594.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：51%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioCrop`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LayerUtility: PurgeVRAM`
- `LoadAudio`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `ShowText|pysssss`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 3/4 个有
- `AILab_QwenVL_PromptEnhancer` —— 2/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `EasyCache` —— 2/4 个有
- `KSampler` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `MiniMaxLowVRAMAttention` —— 2/4 个有
- `ModelPreviewOverrideKJ` —— 2/4 个有
- `RIFE VFI` —— 2/4 个有
- `RTXVideoSuperResolution` —— 2/4 个有
- `SplitSigmas` —— 2/4 个有
- `CreateVideo` —— 1/4 个有
- `H3ModeSwitch` —— 1/4 个有
- `ImageScale` —— 1/4 个有
- `MiniMaxH3AddGuide` —— 1/4 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 1/4 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 1/4 个有
- `RH_DLSS5Enhance` —— 1/4 个有
- `SaveVideo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0.35 | 0.2 - 0.4 | 4 | 74% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.35，观测区间 0.2 - 0.4，4 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
