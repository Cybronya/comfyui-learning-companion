---
name: unknown_workflow_video_sampler_unet_30
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.898846
common_nodes: [BasicScheduler, CLIPLoader, KSamplerSelect, MiniMaxH3ImageToVideo, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Minimax_h3_超级加速图生视频_2084162376542281729.json, 视频生成/图生视频/Minimax_h3_超级加速首尾帧图生视频_2084842867264155649.json, 视频生成/图生视频/video_minimax_h3_i2v_2084181095406456833.json, 视频生成/图生视频/video_minimax_h3_i2v_turbo_lora_2086152939638452226.json, 视频生成/图生视频/video_minimax_h3_i2v_turbo_lora_2sampling_2086306419887923201.json, 视频生成/图生视频/万象+RH-Minimax_h3_4宫格图生视频_2084272132292435970.json, "视频生成/图生视频/图生视频,首尾帧,MiniMax H3,音画同步,AI视频_2106272459883368449.json", 视频生成/图生视频/海螺-Minimax_H3_图生视频-优化版_2085285557453807618.json, 视频生成/图生视频/海螺H3(minimax H3)首尾帧生视频加速开源版_2084885078169186305.json, 视频生成/图生视频/海螺Minimax_H3_图生视频——极速优化版_2084239451739484161.json, 视频生成/文生视频/Minimax H3 首尾帧丨首帧丨尾帧丨文生视频丨老许Gary🎉_2084172294758424577.json, 视频生成/文生视频/Minimax_h3_文生视频_2088656070670643202.json, 视频生成/文生视频/Minimax_h3_文生视频_2094242510569828353.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_30

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/Minimax_h3_超级加速图生视频_2084162376542281729.json、视频生成/图生视频/Minimax_h3_超级加速首尾帧图生视频_2084842867264155649.json、视频生成/图生视频/video_minimax_h3_i2v_2084181095406456833.json、视频生成/图生视频/video_minimax_h3_i2v_turbo_lora_2086152939638452226.json、视频生成/图生视频/video_minimax_h3_i2v_turbo_lora_2sampling_2086306419887923201.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 11/13 个有
- `LoadImage` —— 11/13 个有
- `CR Text` —— 10/13 个有
- `GetImageSize` —— 10/13 个有
- `ImageScaleToTotalPixels` —— 10/13 个有
- `PainterVRAM` —— 10/13 个有
- `PathchSageAttentionKJ` —— 10/13 个有
- `ResolutionSelector` —— 10/13 个有
- `INTConstant` —— 8/13 个有
- `SimpleMath+` —— 8/13 个有
- `ComfyMathExpression` —— 5/13 个有
- `LoraLoaderModelOnly` —— 5/13 个有
- `PrimitiveFloat` —— 5/13 个有
- `EasyCache` —— 3/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/13 个有
- `CFGGuider` —— 2/13 个有
- `ConditioningZeroOut` —— 2/13 个有
- `DisableNoise` —— 1/13 个有
- `Label (rgthree)` —— 1/13 个有
- `MiniMaxChunkFeedForward` —— 1/13 个有
- `MiniMaxLowVRAMAttention` —— 1/13 个有
- `SplitSigmas` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
