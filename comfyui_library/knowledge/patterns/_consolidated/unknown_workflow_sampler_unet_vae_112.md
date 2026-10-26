---
name: unknown_workflow_sampler_unet_vae_112
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.863889
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3-多图参考生视频_2100470995197980673.json, 视频生成/图生视频/MiniMax_H3全能多参手写提示词_2084680682755936257.json, 视频生成/图生视频/MiniMax_H3全能多参自动提示词版_2084314426563452929.json, 视频生成/图生视频/Minimax H3 - 参考生视频_2095080820255059969.json, 视频生成/图生视频/Minimax H3-最佳动态战斗版V2_2096214859611467777.json, 视频生成/图生视频/minimax h3多参模式武器打斗_2095692154944442370.json, 视频生成/文生视频/MiniMax_H3_打斗强化工作流（二采+打斗lora+动作修复）_2092573716482969601.json, 视频生成/文生视频/minimaxH3文生视频武器打斗转用工作流_2095690809084571649.json, 视频生成/文生视频/剑斗多参模式_2094373732667187201.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_112

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3-多图参考生视频_2100470995197980673.json、视频生成/图生视频/MiniMax_H3全能多参手写提示词_2084680682755936257.json、视频生成/图生视频/MiniMax_H3全能多参自动提示词版_2084314426563452929.json、视频生成/图生视频/Minimax H3 - 参考生视频_2095080820255059969.json、视频生成/图生视频/Minimax H3-最佳动态战斗版V2_2096214859611467777.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 8/9 个有
- `PrimitiveStringMultiline` —— 7/9 个有
- `DisableNoise` —— 6/9 个有
- `ExtendIntermediateSigmas` —— 6/9 个有
- `SplitSigmasDenoise` —— 6/9 个有
- `CreateVideo` —— 5/9 个有
- `SaveVideo` —— 5/9 个有
- `CLIPTextEncode` —— 4/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/9 个有
- `PathchSageAttentionKJ` —— 4/9 个有
- `VHS_VideoCombine` —— 4/9 个有
- `easy cleanGpuUsed` —— 4/9 个有
- `easy showAnything` —— 2/9 个有
- `孤海注释` —— 2/9 个有
- `CR Text` —— 1/9 个有
- `LTXVConcatAVLatent` —— 1/9 个有
- `LTXVSeparateAVLatent` —— 1/9 个有
- `MinimaxH3LatentUpscaler3D` —— 1/9 个有
- `ModelAttentionBackend` —— 1/9 个有
- `ModelPreviewOverrideKJ` —— 1/9 个有
- `NanFengH3ReleaseBeforeDecode` —— 1/9 个有
- `RHHiddenNodes` —— 1/9 个有
- `RH_LLMAPI_Pro_Node` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
