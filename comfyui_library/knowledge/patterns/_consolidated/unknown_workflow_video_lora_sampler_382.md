---
name: unknown_workflow_video_lora_sampler_382
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.753167
common_nodes: [Any Switch (rgthree), BasicGuider, CLIPLoader, ComfyMathExpression, Fast Groups Bypasser (rgthree), GetImageSize, ImageScaleToTotalPixels, ImpactConditionalBranch, LoadImage, LoraLoaderModelOnly, MiniMaxH3DualClockSamplerT8, MiniMaxH3ImageToVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, Seed (rgthree), UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/MiniMax H3 V4 加速 8步便宜高分辨率Lightx2v新版_2096506669005103105.json, 视频生成/图生视频/MiniMax+H3+turbo+V4 加速 图生视频_2087377151829045249.json, 视频生成/文生视频/MiniMax H3加速-雷动_2089901234252763137.json, 视频生成/文生视频/MiniMax H3多合一加速工作流_2087814171474874370.json, 视频生成/文生视频/MiniMax H3多合一加速模糊修复工作流_2088889982973992961.json, 视频生成/文生视频/MiniMax+H3+turbo+V4 加速 多合一工作流_2087055785581965313.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_382

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/MiniMax H3 V4 加速 8步便宜高分辨率Lightx2v新版_2096506669005103105.json、视频生成/图生视频/MiniMax+H3+turbo+V4 加速 图生视频_2087377151829045249.json、视频生成/文生视频/MiniMax H3加速-雷动_2089901234252763137.json、视频生成/文生视频/MiniMax H3多合一加速工作流_2087814171474874370.json、视频生成/文生视频/MiniMax H3多合一加速模糊修复工作流_2088889982973992961.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 6 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `ImpactConditionalBranch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 3/6 个有
- `Fast Bypasser (rgthree)` —— 3/6 个有
- `PrimitiveBoolean` —— 3/6 个有
- `easy boolean` —— 3/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `BasicScheduler` —— 1/6 个有
- `KSamplerSelect` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
