---
name: unknown_workflow_video_sampler_unet_19
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.7705
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoadImage, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MINIMAX-H3 多图参考短剧一键生成_2085997938811166721.json, 视频生成/图生视频/MINIMAX-H3动漫画风加速低显存全功能工作流_2099295189230772226.json, 视频生成/图生视频/MINIMAX-H3图生视频_2093614146712592385.json, 视频生成/图生视频/MINIMAX-H3图生视频单图参考_2085995526268477441.json, 视频生成/图生视频/MINIMAX-H3工作流-8-20_2086750733025767426.json, 视频生成/图生视频/MINIMAX-H3工作流-自用_2086126941140242434.json, 视频生成/图生视频/MINIMAX-H3工作流合集_2086380256604282881.json, 视频生成/图生视频/MINIMAX-H3工作流合集（最新版）_2094331708098301954.json, 视频生成/图生视频/MINIMAX-H3工作流合集（注意开关）_2108385005096497153.json, 视频生成/图生视频/MINIMAX-H3工作流文生，图生，全能参考_2093745550528172034.json, 视频生成/图生视频/MiniMax H3全能参考工作流_2084457467743920129.json, 视频生成/图生视频/MiniMax H3｜竖屏人像情绪特写_2111201860685230081.json, 视频生成/图生视频/Minimax H3剪枝版BF16首帧生视频_2094406920504434690.json, 视频生成/图生视频/MinimaxH3开源版-首_尾帧-加速版_2089597414054383618.json, 视频生成/图生视频/MinimaxH3开源版-首_尾帧-加速版_2109156809616486402.json, 视频生成/图生视频/多图参考生成视频Minimax+H3 极致满血1K-10秒 双bf16-+sage加速_2090611037820243970.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_19

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/MINIMAX-H3 多图参考短剧一键生成_2085997938811166721.json、视频生成/图生视频/MINIMAX-H3动漫画风加速低显存全功能工作流_2099295189230772226.json、视频生成/图生视频/MINIMAX-H3图生视频_2093614146712592385.json、视频生成/图生视频/MINIMAX-H3图生视频单图参考_2085995526268477441.json、视频生成/图生视频/MINIMAX-H3工作流-8-20_2086750733025767426.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `LoadImage`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 15/16 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 13/16 个有
- `PrimitiveStringMultiline` —— 13/16 个有
- `LoraLoaderBypassModelOnly` —— 12/16 个有
- `LoadAudio` —— 11/16 个有
- `Fast Groups Bypasser (rgthree)` —— 8/16 个有
- `UniBlockSwap` —— 6/16 个有
- `BasicScheduler` —— 3/16 个有
- `CR Prompt Text` —— 3/16 个有
- `KSamplerSelect` —— 3/16 个有
- `LayerUtility: PurgeVRAM V2` —— 3/16 个有
- `LoraLoaderModelOnly` —— 2/16 个有
- `AudioCrop` —— 1/16 个有
- `PrimitiveInt` —— 1/16 个有
- `RH_LLMAPI_Pro_Node` —— 1/16 个有
- `TTResolutionSelector` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
