---
name: unknown_workflow_upscale_latent_upscale_lora_48
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.818333
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/H3全能参考生视频-练习模式_2092890005231464450.json, 视频生成/文生视频/H3基础模式_10步+3步Latent Upscaler_2090818143013924865.json, 视频生成/文生视频/H3文生视频Tao 3步lora二采RES4LYF_2100959295356628994.json, 视频生成/文生视频/MiniMax-H3 fl2v单模型二采无编解码放大_2093393143118000129.json, 视频生成/文生视频/MiniMax-H3 极限复杂大动态与人脸去油腻工作流_2096278728602112001.json, 视频生成/文生视频/Minimax H3多参 Taomate 3 steplora 二采生视频_2100938444443832322.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_48

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/H3全能参考生视频-练习模式_2092890005231464450.json、视频生成/文生视频/H3基础模式_10步+3步Latent Upscaler_2090818143013924865.json、视频生成/文生视频/H3文生视频Tao 3步lora二采RES4LYF_2100959295356628994.json、视频生成/文生视频/MiniMax-H3 fl2v单模型二采无编解码放大_2093393143118000129.json、视频生成/文生视频/MiniMax-H3 极限复杂大动态与人脸去油腻工作流_2096278728602112001.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 5/6 个有
- `MiniMaxH3SigmaShift` —— 5/6 个有
- `ModelAttentionBackend` —— 5/6 个有
- `SaveVideo` —— 5/6 个有
- `ModelPreviewOverrideKJ` —— 4/6 个有
- `PrimitiveStringMultiline` —— 4/6 个有
- `BasicScheduler` —— 3/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `MiniMaxH3ImageToVideo` —— 3/6 个有
- `MiniMaxH3ReferenceToVideo` —— 3/6 个有
- `SplitSigmas` —— 3/6 个有
- `VHS_VideoCombine` —— 3/6 个有
- `ClownsharKSampler_Beta` —— 2/6 个有
- `SeedGenerator` —— 2/6 个有
- `Text` —— 2/6 个有
- `AnyBooleanSwitch` —— 1/6 个有
- `ComfySwitchNode` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `MiniMaxChunkFeedForward` —— 1/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/6 个有
- `PathchSageAttentionKJ` —— 1/6 个有
- `PrimitiveBoolean` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `UniBlockSwap` —— 1/6 个有
- `VRAM_Debug` —— 1/6 个有
- `布尔孤海` —— 1/6 个有

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
