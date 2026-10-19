---
name: unknown_workflow_video_sampler_unet_41
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.857143
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3多参卡点换装工作流_2097696437873242114.json, 视频生成/图生视频/MiniMaxH3-双角色+指定背景3图生视频！加速版！_2089258074396774402.json, 视频生成/图生视频/MiniMax_ref2v_imgvideoaudio_2092306138221072386.json, 视频生成/图生视频/Minimax H3多参音视频生成开源版（9图3视频3音频）_2084892402388652033.json, 视频生成/图生视频/Minimax H3多参音视频生成开源版（9图3视频3音频）_2086998199218294786.json, 视频生成/图生视频/aidir-Minimax_h3_多参考图生视频_2087056895474491393.json, 视频生成/图生视频/h3-参考生成视频-加速版_2085877996057088001.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_41

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3多参卡点换装工作流_2097696437873242114.json、视频生成/图生视频/MiniMaxH3-双角色+指定背景3图生视频！加速版！_2089258074396774402.json、视频生成/图生视频/MiniMax_ref2v_imgvideoaudio_2092306138221072386.json、视频生成/图生视频/Minimax H3多参音视频生成开源版（9图3视频3音频）_2084892402388652033.json、视频生成/图生视频/Minimax H3多参音视频生成开源版（9图3视频3音频）_2086998199218294786.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
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
- `BasicScheduler` —— 6/7 个有
- `KSamplerSelect` —— 6/7 个有
- `PathchSageAttentionKJ` —— 6/7 个有
- `LoadAudio` —— 5/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `VHS_LoadVideo` —— 5/7 个有
- `PainterVRAM` —— 4/7 个有
- `LoraLoaderBypassModelOnly` —— 3/7 个有
- `EasyCache` —— 2/7 个有
- `CM_FloatToInt` —— 1/7 个有
- `FlashVSRNode` —— 1/7 个有
- `ImageConcanate` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/7 个有
- `RHMiniMaxH3PromptOptimizerMedia` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `Sleep` —— 1/7 个有
- `SolAttnPatch` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
