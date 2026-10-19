---
name: unknown_workflow_sampler_unet_vae_14
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.8284
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax+H3+turbo+V4 加速 图生视频_2087377151829045249.json, 视频生成/图生视频/MiniMax+H3图生视频（首帧视频、尾帧视频、首尾帧视频）_2084465463463075842.json, 视频生成/图生视频/MiniMax-H3 图生视频（首尾帧）_2084150513402204161.json, 视频生成/图生视频/MiniMax-H3-图生视频_2084259365334372354.json, 视频生成/图生视频/MiniMax-H3-图生视频（4步生视频超级加速）_2085221255543877633.json, 视频生成/图生视频/MiniMax-H3-首尾帧视频_2084274212876939265.json, 视频生成/图生视频/MiniMax-H3全能参考工作流_2084872705010130945.json, 视频生成/图生视频/MiniMaxH3首尾帧工作流 By 像素幻想Lab_2087128132951298049.json, 视频生成/图生视频/Minimax-H3 多参考图  电商服装视频_2089669546205601794.json, 视频生成/图生视频/Minimax-H3 多参考图_2085260972230537218.json, 视频生成/图生视频/minimax_h3_i2v_videoonly_2090443654421897217.json, 视频生成/图生视频/minimax_h3_i2v图生视频_2084166438562127874.json, 视频生成/图生视频/minimax_h3_图生视频_2084537327996719106.json, 视频生成/图生视频/minimax_h3_图生视频西瓜宝宝工作流_2084397677135089665.json, 视频生成/图生视频/minimax_h3_迷你别墅视频工作流_2084267933227900930.json, 视频生成/图生视频/▶▷MiniMaxH3-加速图生视频流_2089600631442067458.json, 视频生成/文生视频/MiniMax H3加速-雷动_2089901234252763137.json, 视频生成/文生视频/MiniMax H3多合一加速工作流_2087814171474874370.json, 视频生成/文生视频/MiniMax H3多合一加速模糊修复工作流_2088889982973992961.json, 视频生成/文生视频/MiniMax+H3+turbo+V4 加速 多合一工作流_2087055785581965313.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_14

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/MiniMax+H3+turbo+V4 加速 图生视频_2087377151829045249.json、视频生成/图生视频/MiniMax+H3图生视频（首帧视频、尾帧视频、首尾帧视频）_2084465463463075842.json、视频生成/图生视频/MiniMax-H3 图生视频（首尾帧）_2084150513402204161.json、视频生成/图生视频/MiniMax-H3-图生视频_2084259365334372354.json、视频生成/图生视频/MiniMax-H3-图生视频（4步生视频超级加速）_2085221255543877633.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 20 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecodeAudio` —— 19/20 个有
- `MiniMaxH3ImageToVideo` —— 17/20 个有
- `BasicScheduler` —— 16/20 个有
- `KSamplerSelect` —— 16/20 个有
- `ImageScaleToTotalPixels` —— 15/20 个有
- `GetImageSize` —— 13/20 个有
- `CreateVideo` —— 12/20 个有
- `SaveVideo` —— 12/20 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/20 个有
- `LoraLoaderModelOnly` —— 8/20 个有
- `VHS_VideoCombine` —— 8/20 个有
- `Fast Groups Bypasser (rgthree)` —— 7/20 个有
- `ImpactConditionalBranch` —— 6/20 个有
- `Seed (rgthree)` —— 6/20 个有
- `Any Switch (rgthree)` —— 5/20 个有
- `MiniMaxH3DualClockSamplerT8` —— 5/20 个有
- `MiniMaxH3ReferenceToVideo` —— 4/20 个有
- `easy boolean` —— 4/20 个有
- `ImageResizeKJv2` —— 3/20 个有
- `ComfySwitchNode` —— 2/20 个有
- `Fast Bypasser (rgthree)` —— 2/20 个有
- `PrimitiveBoolean` —— 2/20 个有
- `easy cleanGpuUsed` —— 2/20 个有
- `CR Prompt Text` —— 1/20 个有
- `GetNode` —— 1/20 个有
- `Label (rgthree)` —— 1/20 个有
- `SetNode` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
