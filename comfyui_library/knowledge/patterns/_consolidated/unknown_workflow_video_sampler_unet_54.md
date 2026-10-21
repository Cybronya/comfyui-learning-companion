---
name: unknown_workflow_video_sampler_unet_54
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.752833
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax+H3单图生视频版_2093705769144373249.json, 视频生成/图生视频/MiniMax-H3 首尾帧图生视频_2084637924326465538.json, 视频生成/图生视频/MiniMax-H3开源 单图生视频版_2094011380541247489.json, 视频生成/图生视频/MiniMax_H3图生视频自动提示词版_2084335214544908289.json, 视频生成/文生视频/MiniMax_H3文生视频自动提示词版_2084361115349372930.json, 视频生成/文生视频/加速版！Minimax H3！开源免费版！文生视频！_2085198371240898561.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_54

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/MiniMax+H3单图生视频版_2093705769144373249.json、视频生成/图生视频/MiniMax-H3 首尾帧图生视频_2084637924326465538.json、视频生成/图生视频/MiniMax-H3开源 单图生视频版_2094011380541247489.json、视频生成/图生视频/MiniMax_H3图生视频自动提示词版_2084335214544908289.json、视频生成/文生视频/MiniMax_H3文生视频自动提示词版_2084361115349372930.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/6 个有
- `PathchSageAttentionKJ` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `孤海注释` —— 4/6 个有
- `CR Text` —— 3/6 个有
- `PrimitiveStringMultiline` —— 3/6 个有
- `GetNode` —— 2/6 个有
- `ImageCrop+` —— 2/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `ImageScaleToTotalPixels` —— 2/6 个有
- `PainterVRAM` —— 2/6 个有
- `RHHiddenNodes` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `VHS_LoadVideoFFmpeg` —— 2/6 个有
- `MiniMaxH3BlockCacheT8` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
