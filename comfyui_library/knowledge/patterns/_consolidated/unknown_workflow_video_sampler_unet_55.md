---
name: unknown_workflow_video_sampler_unet_55
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.8525
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3多参卡点换装工作流_2097696437873242114.json, 视频生成/图生视频/MiniMaxH3-双角色+指定背景3图生视频！加速版！_2089258074396774402.json, 视频生成/图生视频/Minimax-H3 多参考图  电商服装视频_2089669546205601794.json, 视频生成/图生视频/Minimax-H3 多参考图_2085260972230537218.json, 视频生成/图生视频/人像VLOG丨MiniMax-H3丨三图参考·音画生成_2100863837363851266.json, 视频生成/图生视频/人像VLOG丨MiniMax-H3丨三图参考·音画生成_2101132610901733377.json, 视频生成/图生视频/电商产品展示 图片参考生视频 minimax h3_2085356615661875201.json, 音频生成/音频生成/minimax_h3 参考图生视频+sage加速_2085965890079776770.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_55

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3多参卡点换装工作流_2097696437873242114.json、视频生成/图生视频/MiniMaxH3-双角色+指定背景3图生视频！加速版！_2089258074396774402.json、视频生成/图生视频/Minimax-H3 多参考图  电商服装视频_2089669546205601794.json、视频生成/图生视频/Minimax-H3 多参考图_2085260972230537218.json、视频生成/图生视频/人像VLOG丨MiniMax-H3丨三图参考·音画生成_2100863837363851266.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
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
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 7/8 个有
- `KSamplerSelect` —— 7/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/8 个有
- `ImageResizeKJv2` —— 4/8 个有
- `ImageScaleToTotalPixels` —— 4/8 个有
- `JjkText` —— 4/8 个有
- `PathchSageAttentionKJ` —— 3/8 个有
- `EasyCache` —— 2/8 个有
- `LoraLoaderBypassModelOnly` —— 2/8 个有
- `CM_FloatToInt` —— 1/8 个有
- `ImageConcanate` —— 1/8 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `RHMiniMaxH3PromptOptimizerMedia` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
