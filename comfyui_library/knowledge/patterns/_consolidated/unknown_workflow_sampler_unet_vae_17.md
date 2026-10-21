---
name: unknown_workflow_sampler_unet_vae_17
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.811444
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoadImage, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax+H3+turbo+V4 加速 图生视频_2087377151829045249.json, 视频生成/图生视频/MiniMax+H3图生视频（首帧视频、尾帧视频、首尾帧视频）_2084465463463075842.json, 视频生成/图生视频/MiniMax-H3 图生视频（首尾帧）_2084150513402204161.json, 视频生成/图生视频/Minimax H3-i2v 官方版图生视频_2084176815941308418.json, 视频生成/图生视频/Minimax H3-i2v 官方版图生视频_2084449411379326978.json, 视频生成/图生视频/Minimax H3-i2v 官方版图生视频_2084464401641467905.json, 视频生成/图生视频/Minimax H3-i2v 官方版图生视频_2084552805813149698.json, 视频生成/图生视频/Minimax-H3-T2V 开源版本 图生视频_2084262714964275202.json, 视频生成/图生视频/Minimax-H3-图生视频（Lightx2v加速）_2085944759729872898.json, 视频生成/图生视频/VividMuse_MiniMax_H3_图生视频_2084274037685051393.json, 视频生成/图生视频/lightx2v 300%加速 MinimaxH3-文生+图生视频（支持首尾帧）_2084260178744139778.json, 视频生成/图生视频/minimax H3 开源版图生视频-4步加速极速版_2087727783698059266.json, 视频生成/文生视频/MINIMAX-H3 文生_单图_首尾帧 工作流_2085269429079855106.json, 视频生成/文生视频/MiniMax H3 图生视频 首尾帧生视频_2085441158259494913.json, 视频生成/文生视频/MiniMax H3加速-雷动_2089901234252763137.json, 视频生成/文生视频/MiniMax H3多合一加速工作流_2087814171474874370.json, 视频生成/文生视频/MiniMax H3多合一加速模糊修复工作流_2088889982973992961.json, 视频生成/文生视频/MiniMax+H3+turbo+V4 加速 多合一工作流_2087055785581965313.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_17

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/MiniMax+H3+turbo+V4 加速 图生视频_2087377151829045249.json、视频生成/图生视频/MiniMax+H3图生视频（首帧视频、尾帧视频、首尾帧视频）_2084465463463075842.json、视频生成/图生视频/MiniMax-H3 图生视频（首尾帧）_2084150513402204161.json、视频生成/图生视频/Minimax H3-i2v 官方版图生视频_2084176815941308418.json、视频生成/图生视频/Minimax H3-i2v 官方版图生视频_2084449411379326978.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `LoadImage`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 15/18 个有
- `BasicScheduler` —— 14/18 个有
- `GetImageSize` —— 14/18 个有
- `KSamplerSelect` —— 14/18 个有
- `CreateVideo` —— 12/18 个有
- `SaveVideo` —— 12/18 个有
- `LoraLoaderModelOnly` —— 9/18 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/18 个有
- `Fast Groups Bypasser (rgthree)` —— 8/18 个有
- `ImpactConditionalBranch` —— 6/18 个有
- `Seed (rgthree)` —— 6/18 个有
- `VHS_VideoCombine` —— 6/18 个有
- `Any Switch (rgthree)` —— 5/18 个有
- `MiniMaxH3DualClockSamplerT8` —— 5/18 个有
- `easy boolean` —— 4/18 个有
- `PrimitiveStringMultiline` —— 3/18 个有
- `ComfySwitchNode` —— 2/18 个有
- `Fast Bypasser (rgthree)` —— 2/18 个有
- `PrimitiveBoolean` —— 2/18 个有
- `easy cleanGpuUsed` —— 2/18 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/18 个有
- `MiniMaxH3SigmaShift` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
