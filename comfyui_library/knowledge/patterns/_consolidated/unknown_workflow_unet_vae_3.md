---
name: unknown_workflow_unet_vae_3
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.83
common_nodes: [CLIPLoader, CR Text, MiniMaxH3ImageToVideo, PathchSageAttentionKJ, ResolutionSelector, UNETLoader, VAELoader]
problems: []
missing: []
members: [数字人/数字人/minimax H3-rapid_2084240131556470785.json, 视频生成/图生视频/万象+RH-Minimax_h3_4宫格图生视频_2084272132292435970.json, "视频生成/图生视频/图生视频,首尾帧,MiniMax H3,音画同步,AI视频_2106272459883368449.json", 视频生成/图生视频/海螺-Minimax_H3_图生视频-优化版_2085285557453807618.json, 视频生成/图生视频/海螺H3(minimax H3)首尾帧生视频加速开源版_2084885078169186305.json, 视频生成/图生视频/海螺H3)首尾帧生视频_2085148305012649985.json, 视频生成/图生视频/海螺Minimax_H3_图生视频——极速优化版_2084239451739484161.json, 视频生成/文生视频/MiniMax-H3 图生视频 5秒1080p视频只需8分钟+全节点注释_2084557666449444865.json, 视频生成/文生视频/MiniMax-H3 文生视频 5秒1080p视频只需8分钟+全节点注释_2084777365707776002.json, 视频生成/文生视频/MiniMax-H3 文生视频 5秒1080p视频只需8分钟+全节点注释_2094043847910318082.json, 视频生成/文生视频/Minimax H3 首尾帧丨首帧丨尾帧丨文生视频丨老许Gary🎉_2084172294758424577.json, 视频生成/文生视频/Minimax_h3_文生视频_2088656070670643202.json, 视频生成/文生视频/minimax-h3 -标准官方工作流（文生_首尾帧生视频）_2094754298751180802.json, 视频生成/文生视频/minimaxH3文生视频工作流（超级加速版）_2084925338584436737.json]
source: knowledge_consolidation
---

# unknown_workflow_unet_vae_3

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（数字人/数字人/minimax H3-rapid_2084240131556470785.json、视频生成/图生视频/万象+RH-Minimax_h3_4宫格图生视频_2084272132292435970.json、视频生成/图生视频/图生视频,首尾帧,MiniMax H3,音画同步,AI视频_2106272459883368449.json、视频生成/图生视频/海螺-Minimax_H3_图生视频-优化版_2085285557453807618.json、视频生成/图生视频/海螺H3(minimax H3)首尾帧生视频加速开源版_2084885078169186305.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `MiniMaxH3ImageToVideo`
- `PathchSageAttentionKJ`
- `ResolutionSelector`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 13/14 个有
- `BasicScheduler` —— 13/14 个有
- `KSamplerSelect` —— 13/14 个有
- `RandomNoise` —— 13/14 个有
- `SamplerCustomAdvanced` —— 13/14 个有
- `VAEDecode` —— 13/14 个有
- `VAEDecodeAudio` —— 13/14 个有
- `LoadImage` —— 12/14 个有
- `PainterVRAM` —— 9/14 个有
- `VHS_VideoCombine` —— 9/14 个有
- `INTConstant` —— 8/14 个有
- `SimpleMath+` —— 8/14 个有
- `GetImageSize` —— 7/14 个有
- `ImageScaleToTotalPixels` —— 7/14 个有
- `ComfyMathExpression` —— 6/14 个有
- `CreateVideo` —— 6/14 个有
- `EasyCache` —— 6/14 个有
- `SaveVideo` —— 6/14 个有
- `Int` —— 3/14 个有
- `PrimitiveFloat` —— 3/14 个有
- `Label (rgthree)` —— 2/14 个有
- `Fast Groups Bypasser (rgthree)` —— 1/14 个有
- `ModelPatchTorchSettings` —— 1/14 个有
- `PreviewImage` —— 1/14 个有
- `SetReserveVRAM` —— 1/14 个有
- `workflow>采样解码` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
