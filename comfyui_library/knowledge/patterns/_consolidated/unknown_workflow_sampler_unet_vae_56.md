---
name: unknown_workflow_sampler_unet_vae_56
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.825714
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/H3工作流_2088343591486840833.json, 视频生成/图生视频/MINIMAX-H3-图生视频_2084159275156467714.json, 视频生成/图生视频/MINIMAX-H3-图生视频_2084308814681169921.json, 视频生成/图生视频/MiniMax H3 4步 首尾帧图生视频_2090639499977117697.json, 视频生成/图生视频/MiniMax H3 4步 首帧图生视频_2090629891019599874.json, 视频生成/图生视频/Minimax H3 多参 Lightx2v 加速_2087571144038764548.json, 视频生成/图生视频/Minimax-H3-8步加速-多参考生视频（平均3.5分钟出5秒）_2085387387793928194.json, 视频生成/图生视频/Minimax-H3-图生视频（Lightx2v加速）_2085944759729872898.json, 视频生成/图生视频/Minimax-H3-多参考生成 官流_2095740048577744897.json, 视频生成/图生视频/Minimax-h3 多模态全能参考_2084472101880287234.json, 视频生成/图生视频/Minimax3-参考生视频-8月8日版_2086541785450500098.json, 视频生成/图生视频/MinimaxH3多参_2085409741941067777.json, 视频生成/图生视频/加速高质开源MiniMax+H3+FL2VA开源版-首尾帧参考生视频+++_2084152775365189633.json, 视频生成/文生视频/MiniMax H3多参2倍速（开源版）V2_2086281240478576641.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_56

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/H3工作流_2088343591486840833.json、视频生成/图生视频/MINIMAX-H3-图生视频_2084159275156467714.json、视频生成/图生视频/MINIMAX-H3-图生视频_2084308814681169921.json、视频生成/图生视频/MiniMax H3 4步 首尾帧图生视频_2090639499977117697.json、视频生成/图生视频/MiniMax H3 4步 首帧图生视频_2090629891019599874.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
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
- `CR Text` —— 7/14 个有
- `LoadAudio` —— 7/14 个有
- `LoraLoaderModelOnly` —— 7/14 个有
- `MiniMaxH3ImageToVideo` —— 6/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/14 个有
- `PrimitiveStringMultiline` —— 6/14 个有
- `MiniMaxH3ReferenceToVideo` —— 4/14 个有
- `PathchSageAttentionKJ` —— 4/14 个有
- `PreviewAny` —— 4/14 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 4/14 个有
- `ImageScaleToTotalPixels` —— 3/14 个有
- `MiniMaxH3BlockCacheT8` —— 3/14 个有
- `RH_LLMAPI_Pro_Node` —— 3/14 个有
- `VHS_LoadVideo` —— 3/14 个有
- `MiniMaxH3SigmaShift` —— 2/14 个有
- `SetNode` —— 2/14 个有
- `GetNode` —— 1/14 个有
- `RHLLMChatNode` —— 1/14 个有
- `SpectrumApplyMiniMaxH3` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
