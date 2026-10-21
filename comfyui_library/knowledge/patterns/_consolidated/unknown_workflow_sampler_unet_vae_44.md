---
name: unknown_workflow_sampler_unet_vae_44
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.840667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/H3工作流_2088343591486840833.json, 视频生成/图生视频/MINIMAX-H3-图生视频_2084159275156467714.json, 视频生成/图生视频/MINIMAX-H3-图生视频_2084308814681169921.json, 视频生成/图生视频/MiniMax H3 4步 首尾帧图生视频_2090639499977117697.json, 视频生成/图生视频/MiniMax H3 4步 首帧图生视频_2090629891019599874.json, 视频生成/图生视频/MiniMax+H3+图生视频+加速版工作流_2087098569571524609.json, 视频生成/图生视频/MiniMaxH3加速版工作流图生视频ENGENG_2087088986627067905.json, 视频生成/图生视频/MiniMaxH3视频生成工作流加速版首尾帧ENGENG_2087088340184162306.json, 视频生成/图生视频/Minimax H3 多参 Lightx2v 加速_2087571144038764548.json, 视频生成/图生视频/Minimax H3多参音视频生成开源版（9图3视频3音频）_2087076628211003394.json, 视频生成/图生视频/MinimaxH3多参_2085409741941067777.json, 视频生成/文生视频/MiniMax H3 lightx2v 4步加速图生视频工作流_2086324212742049794.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_44

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/H3工作流_2088343591486840833.json、视频生成/图生视频/MINIMAX-H3-图生视频_2084159275156467714.json、视频生成/图生视频/MINIMAX-H3-图生视频_2084308814681169921.json、视频生成/图生视频/MiniMax H3 4步 首尾帧图生视频_2090639499977117697.json、视频生成/图生视频/MiniMax H3 4步 首帧图生视频_2090629891019599874.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 12 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 9/12 个有
- `MiniMaxH3ImageToVideo` —— 9/12 个有
- `ImageScaleToTotalPixels` —— 7/12 个有
- `PathchSageAttentionKJ` —— 7/12 个有
- `CR Text` —— 6/12 个有
- `MiniMaxH3SigmaShift` —— 6/12 个有
- `GetImageSize` —— 5/12 个有
- `LoadAudio` —— 3/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/12 个有
- `PreviewAny` —— 3/12 个有
- `RH_LLMAPI_Pro_Node` —— 3/12 个有
- `ResizeImageMaskNode` —— 3/12 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 3/12 个有
- `MiniMaxH3BlockCacheT8` —— 2/12 个有
- `EasyCache` —— 1/12 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/12 个有
- `ResizeAndPadImage` —— 1/12 个有
- `SetNode` —— 1/12 个有
- `SpectrumSDXL` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
