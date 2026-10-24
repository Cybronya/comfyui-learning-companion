---
name: unknown_workflow_sampler_unet_vae_134
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.811875
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3开源版 首尾帧生视频 加速版 自动生成转场视频_2084634965546987521.json, 视频生成/图生视频/MiniMax-H3开源版 首尾帧生视频 加速版 自动生成转场视频_2084974736878161922.json, 视频生成/图生视频/MiniMaxH3 首尾帧生视频！加速版！艾橘溪_2084497876612370434.json, 视频生成/图生视频/MiniMaxH3+首尾帧生视频！加速版_2085236338848260097.json, 视频生成/图生视频/MiniMax_H3_i2v_2088871530771083265.json, 视频生成/图生视频/i2va_minimax_h3_vaeint8_api_2103863320280391681.json, 视频生成/图生视频/minimax h3 竖屏版_2084459891346993153.json, 视频生成/图生视频/首尾帧生视频 MiniMaxH3+！加速版_2086649496523591681.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_134

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3开源版 首尾帧生视频 加速版 自动生成转场视频_2084634965546987521.json、视频生成/图生视频/MiniMax-H3开源版 首尾帧生视频 加速版 自动生成转场视频_2084974736878161922.json、视频生成/图生视频/MiniMaxH3 首尾帧生视频！加速版！艾橘溪_2084497876612370434.json、视频生成/图生视频/MiniMaxH3+首尾帧生视频！加速版_2085236338848260097.json、视频生成/图生视频/MiniMax_H3_i2v_2088871530771083265.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ImageToVideo`
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
- `ImageResizeKJv2` —— 7/8 个有
- `PathchSageAttentionKJ` —— 6/8 个有
- `AILab_QwenVL_Advanced` —— 5/8 个有
- `GetNode` —— 5/8 个有
- `Image Stitch` —— 5/8 个有
- `ImageScaleDownToSize` —— 5/8 个有
- `LayerUtility: PurgeVRAM` —— 5/8 个有
- `SetNode` —— 5/8 个有
- `easy positive` —— 5/8 个有
- `LoraLoader` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `Seed (rgthree)` —— 1/8 个有
- `Text` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 0 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
