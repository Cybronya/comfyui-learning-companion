---
name: unknown_workflow_sampler_unet_vae_69
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.851917
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/超审！minimax_h3_it2v(参考生视频)  ！_2084667157266391041.json, 图片生成/文生图/超审！minimax_h3_it2v(图_文生视频) ！_2084665406370963457.json, 视频生成/图生视频/H3-参考生视频（全能参考）_2087759964113821697.json, 视频生成/图生视频/H3多参图生视频_2084177913167040514.json, 视频生成/图生视频/MINIMAX-H3-图片加音频参考生视频-有提示词模板-int8和fp8_2084515925415522306.json, 视频生成/图生视频/MINIMAX-H3_多图参考生视频_2084844223446208514.json, 视频生成/图生视频/MiniMax H3 4图生视频+音频接入_2090184072877395969.json, 视频生成/图生视频/MiniMax H3 ComfyUI多图（音视频）参考模板工作流（官方模板）_2085042609009020929.json, 视频生成/图生视频/MiniMax H3 R2V comfyorg_2085736828308643841.json, 视频生成/图生视频/MiniMax H3 参考生视频_2084543006513909761.json, 视频生成/图生视频/MiniMax H3 参考生视频_2085194930540077058.json, 视频生成/图生视频/MiniMax H3 参考生视频（Sage加速）2608_2085826399662854146.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_69

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/超审！minimax_h3_it2v(参考生视频)  ！_2084667157266391041.json、图片生成/文生图/超审！minimax_h3_it2v(图_文生视频) ！_2084665406370963457.json、视频生成/图生视频/H3-参考生视频（全能参考）_2087759964113821697.json、视频生成/图生视频/H3多参图生视频_2084177913167040514.json、视频生成/图生视频/MINIMAX-H3-图片加音频参考生视频-有提示词模板-int8和fp8_2084515925415522306.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 11/12 个有
- `PrimitiveStringMultiline` —— 11/12 个有
- `CreateVideo` —— 10/12 个有
- `SaveVideo` —— 10/12 个有
- `VAEDecode` —— 10/12 个有
- `VAEDecodeAudio` —— 10/12 个有
- `LoadAudio` —— 8/12 个有
- `VHS_LoadVideo` —— 7/12 个有
- `EasyCache` —— 3/12 个有
- `PathchSageAttentionKJ` —— 3/12 个有
- `JjkText` —— 2/12 个有
- `LTXVSeparateAVLatent` —— 2/12 个有
- `SaveImage` —— 2/12 个有
- `SaveLatent` —— 2/12 个有
- `CR Text` —— 1/12 个有
- `FlashVSRInitPipe` —— 1/12 个有
- `FlashVSRNodeAdv` —— 1/12 个有
- `LayerMask: RemBgUltra` —— 1/12 个有
- `MiniMaxH3ImageToVideo` —— 1/12 个有
- `SolAttnPatch` —— 1/12 个有
- `VHS_VideoCombine` —— 1/12 个有
- `忽略多组孤海` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
