---
name: unknown_workflow_video_sampler_unet_7
type: Unknown Workflow
frequency: 31
level: moderate
coverage: 0.747903
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3MultiRateSamplerEXPT8, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MINIMAX-H3图生视频单图参考_2085995526268477441.json, 视频生成/图生视频/MINIMAX-H3工作流-8-20_2086750733025767426.json, 视频生成/图生视频/MINIMAX-H3工作流-自用_2086126941140242434.json, 视频生成/图生视频/MINIMAX-H3工作流合集_2086380256604282881.json, 视频生成/图生视频/MINIMAX-H3工作流合集_2114520951739215874.json, 视频生成/图生视频/MINIMAX-H3工作流合集_多流程整合版_2115636138307317762.json, 视频生成/图生视频/MINIMAX-H3工作流合集（最新版）_2094331708098301954.json, 视频生成/图生视频/MINIMAX-H3工作流合集（注意开关）_2108385005096497153.json, 视频生成/图生视频/MINIMAX-H3工作流文生，图生，全能参考_2093745550528172034.json, 视频生成/图生视频/MiniMax H3全能参考工作流_2084457467743920129.json, 视频生成/图生视频/MiniMax H3｜竖屏人像情绪特写_2111201860685230081.json, 视频生成/图生视频/MinimaxH3开源版-首_尾帧-加速版_2089597414054383618.json, 视频生成/图生视频/MinimaxH3开源版-首_尾帧-加速版_2109156809616486402.json, 视频生成/图生视频/[MiniMax-H3] 高保真图生视频：静止图像动态化与运镜重构 _ 视频生成 _ 图生视频 __2060992668020338689.json, 视频生成/图生视频/[MiniMax-H3] 高保真图生视频：静止图像动态化与运镜重构 _ 视频生成 _ 图生视频 __2100475521611157506.json, 视频生成/图生视频/[MiniMax-H3] 高保真图生视频：静止图像动态化与运镜重构 _ 视频生成 _ 图生视频 __2100747392579624962.json, 视频生成/图生视频/h3开源加速版MINIMAX-H3工作流合集文单图生多图参考4步lora加速_2097216684217163777.json, 视频生成/图生视频/h3开源加速版MINIMAX-H3工作流合集文单图生多图参考4步lora加速_2097636379042869250.json, 视频生成/图生视频/minimax h3_2089645770512359426.json, 视频生成/图生视频/一个普通的工作流_2094967354697535490.json, 视频生成/图生视频/全能参考 加速版_2086341513830817793.json, 视频生成/图生视频/多参考视频MINIMAX-H3工作流_2089733467306283009.json, 视频生成/图生视频/（3图）MINIMAX短剧_2111253911762989057.json, 视频生成/文生视频/H3-文生视频（16：9）_2085696662042931202.json, 视频生成/文生视频/MINIMAX-H3 一键生成叙事短片_2085916314648014849.json, 视频生成/文生视频/MINIMAX-H3 开源加速版工作流4步lora加速合集h3文单图生多图参考_2087132475666550785.json, 视频生成/文生视频/h3开源加速版MINIMAX-H3工作流合集文单图生多图参考4步lora加速_2087034230105792514.json, 视频生成/文生视频/【CommintAI】MINIMAX H3 工作流合集_2085882928617316354.json, 视频生成/文生视频/【Work-Fisher】MINIMAX-H3工作流合集_2084259935344480258.json, 视频生成/文生视频/【南可nkss】MINIMAX-H3工作流合集_2108370588418002945.json, 视频生成/文生视频/测试使用_2094631681096507394.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_7

> 由 `engine/knowledge_consolidation` 从 31 个 workflow 归纳得出（视频生成/图生视频/MINIMAX-H3图生视频单图参考_2085995526268477441.json、视频生成/图生视频/MINIMAX-H3工作流-8-20_2086750733025767426.json、视频生成/图生视频/MINIMAX-H3工作流-自用_2086126941140242434.json、视频生成/图生视频/MINIMAX-H3工作流合集_2086380256604282881.json、视频生成/图生视频/MINIMAX-H3工作流合集_2114520951739215874.json…）

- **类型**：Unknown Workflow
- **样本数**：31
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 31 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3MultiRateSamplerEXPT8`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderBypassModelOnly` —— 30/31 个有
- `ResolutionSelector` —— 30/31 个有
- `LoadImage` —— 29/31 个有
- `LoadAudio` —— 22/31 个有
- `Fast Groups Bypasser (rgthree)` —— 19/31 个有
- `UniBlockSwap` —— 19/31 个有
- `RHLLMChatNode` —— 4/31 个有
- `1hew_LoadVideoToImage` —— 3/31 个有
- `PreviewAny` —— 3/31 个有
- `JjkText` —— 1/31 个有
- `LoraLoaderModelOnly` —— 1/31 个有
- `PrimitiveInt` —— 1/31 个有
- `RH_LLMAPI_Pro_Node` —— 1/31 个有
- `TTResolutionSelector` —— 1/31 个有
- `easy showAnything` —— 1/31 个有
- `孤海注释` —— 1/31 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
