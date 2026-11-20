---
name: unknown_workflow_video_sampler_unet_37
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.599875
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax+H3单图生视频版_2093705769144373249.json, 视频生成/图生视频/MiniMax-H3开源 单图生视频版_2094011380541247489.json, 视频生成/图生视频/MiniMax_H3图生视频自动提示词版_2084335214544908289.json, 视频生成/图生视频/Minimax H3 首尾帧图生视频_2084915506569633793.json, 视频生成/图生视频/【傲雪AIGC】MiniMax+H3首尾帧生视频版_2093696527855341570.json, 视频生成/文生视频/MiniMax+H3文生视频_2089205361046810625.json, 视频生成/文生视频/MiniMax-H3开源 文生视频_2094359561212882945.json, 视频生成/文生视频/MiniMax-H3开源 文生视频_2094381288823287810.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_37

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MiniMax+H3单图生视频版_2093705769144373249.json、视频生成/图生视频/MiniMax-H3开源 单图生视频版_2094011380541247489.json、视频生成/图生视频/MiniMax_H3图生视频自动提示词版_2084335214544908289.json、视频生成/图生视频/Minimax H3 首尾帧图生视频_2084915506569633793.json、视频生成/图生视频/【傲雪AIGC】MiniMax+H3首尾帧生视频版_2093696527855341570.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 7/8 个有
- `孤海注释` —— 7/8 个有
- `GetNode` —— 6/8 个有
- `LoadImage` —— 6/8 个有
- `SetNode` —— 6/8 个有
- `VHS_LoadVideoFFmpeg` —— 6/8 个有
- `LoraLoaderModelOnly` —— 4/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/8 个有
- `ModelAttentionBackend` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `Text` —— 4/8 个有
- `ImageScaleToTotalPixels` —— 3/8 个有
- `CR Text` —— 2/8 个有
- `ImageCrop+` —— 2/8 个有
- `ImageResizeKJv2` —— 2/8 个有
- `PathchSageAttentionKJ` —— 2/8 个有
- `GetImageSize` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `RHHiddenNodes` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
