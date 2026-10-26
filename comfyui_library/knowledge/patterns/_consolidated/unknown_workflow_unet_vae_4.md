---
name: unknown_workflow_unet_vae_4
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.88925
common_nodes: [CLIPLoader, MiniMaxH3ImageToVideo, ResolutionSelector, UNETLoader, VAELoader]
problems: []
missing: []
members: [数字人/数字人/minimax H3-rapid_2084240131556470785.json, 视频生成/图生视频/万象+RH-Minimax_h3_4宫格图生视频_2084272132292435970.json, "视频生成/图生视频/图生视频,首尾帧,MiniMax H3,音画同步,AI视频_2106272459883368449.json", 视频生成/图生视频/海螺-Minimax_H3_图生视频-优化版_2085285557453807618.json, 视频生成/图生视频/海螺H3(minimax H3)首尾帧生视频加速开源版_2084885078169186305.json, 视频生成/图生视频/海螺H3)首尾帧生视频_2085148305012649985.json, 视频生成/图生视频/海螺Minimax_H3_图生视频——极速优化版_2084239451739484161.json, 视频生成/文生视频/Minimax H3 首尾帧丨首帧丨尾帧丨文生视频丨老许Gary🎉_2084172294758424577.json, 视频生成/文生视频/Minimax_h3_文生视频_2088656070670643202.json, 视频生成/文生视频/minimax-h3 -标准官方工作流（文生_首尾帧生视频）_2094754298751180802.json, 视频生成/文生视频/minimax_h3文生视频 图生视频 首尾帧+sage加速_2084126972392857602.json, 视频生成/文生视频/minimax_h3文生视频 图生视频 首尾帧+sage加速_2085982926470213634.json, 视频生成/文生视频/海螺-Minimax_H3_文生视频-优化版_2085285483189456897.json, 视频生成/文生视频/海螺H3(Minimax h3)文生视频加速开源版_2084173653360599042.json, 视频生成/文生视频/海螺Minimax_H3_文生视频——极速优化版_2084238982388477954.json, 视频生成/文生视频/首尾帧生视频+_2084526811551195138.json]
source: knowledge_consolidation
---

# unknown_workflow_unet_vae_4

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（数字人/数字人/minimax H3-rapid_2084240131556470785.json、视频生成/图生视频/万象+RH-Minimax_h3_4宫格图生视频_2084272132292435970.json、视频生成/图生视频/图生视频,首尾帧,MiniMax H3,音画同步,AI视频_2106272459883368449.json、视频生成/图生视频/海螺-Minimax_H3_图生视频-优化版_2085285557453807618.json、视频生成/图生视频/海螺H3(minimax H3)首尾帧生视频加速开源版_2084885078169186305.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `MiniMaxH3ImageToVideo`
- `ResolutionSelector`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 15/16 个有
- `BasicScheduler` —— 15/16 个有
- `KSamplerSelect` —— 15/16 个有
- `PathchSageAttentionKJ` —— 15/16 个有
- `RandomNoise` —— 15/16 个有
- `SamplerCustomAdvanced` —— 15/16 个有
- `VAEDecode` —— 15/16 个有
- `VAEDecodeAudio` —— 15/16 个有
- `CR Text` —— 14/16 个有
- `LoadImage` —— 12/16 个有
- `PainterVRAM` —— 12/16 个有
- `VHS_VideoCombine` —— 12/16 个有
- `GetImageSize` —— 10/16 个有
- `ImageScaleToTotalPixels` —— 10/16 个有
- `ComfyMathExpression` —— 8/16 个有
- `INTConstant` —— 8/16 个有
- `PrimitiveFloat` —— 8/16 个有
- `SimpleMath+` —— 8/16 个有
- `CreateVideo` —— 5/16 个有
- `SaveVideo` —— 5/16 个有
- `EasyCache` —— 4/16 个有
- `Label (rgthree)` —— 3/16 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/16 个有
- `PreviewImage` —— 1/16 个有
- `workflow>采样解码` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
