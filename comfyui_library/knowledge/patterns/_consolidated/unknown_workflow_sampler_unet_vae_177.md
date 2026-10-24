---
name: unknown_workflow_sampler_unet_vae_177
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.7515
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax+H3单图生视频版_2093705769144373249.json, 视频生成/图生视频/MiniMax-H3 首尾帧图生视频_2084637924326465538.json, 视频生成/图生视频/MiniMax-H3开源 单图生视频版_2094011380541247489.json, 视频生成/图生视频/MiniMax_H3图生视频自动提示词版_2084335214544908289.json, 视频生成/文生视频/260817001.MiniMax H3 文生丨图生视频_2089296462692835330.json, 视频生成/文生视频/MiniMax H3图生视频、首尾帧_2085351688180953090.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_177

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/MiniMax+H3单图生视频版_2093705769144373249.json、视频生成/图生视频/MiniMax-H3 首尾帧图生视频_2084637924326465538.json、视频生成/图生视频/MiniMax-H3开源 单图生视频版_2094011380541247489.json、视频生成/图生视频/MiniMax_H3图生视频自动提示词版_2084335214544908289.json、视频生成/文生视频/260817001.MiniMax H3 文生丨图生视频_2089296462692835330.json…）

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
- `CR Text` —— 4/6 个有
- `ImageCrop+` —— 4/6 个有
- `ImageScaleToTotalPixels` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `VHS_VideoCombine` —— 4/6 个有
- `孤海注释` —— 4/6 个有
- `GetNode` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `CreateVideo` —— 2/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `SaveVideo` —— 2/6 个有
- `VHS_LoadVideoFFmpeg` —— 2/6 个有
- `JjkText` —— 1/6 个有
- `PainterVRAM` —— 1/6 个有
- `RHHiddenNodes` —— 1/6 个有
- `workflow>核心` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
