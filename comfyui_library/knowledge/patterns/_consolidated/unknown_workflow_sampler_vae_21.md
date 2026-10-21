---
name: unknown_workflow_sampler_vae_21
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.694308
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 T2V comfyorg_2084874841076887553.json, 视频生成/文生视频/MiniMax H3 T2V 文生视频 加速版_2086019169908248577.json, 视频生成/文生视频/MiniMax H3 T2V 文生视频_2089602856834912257.json, 视频生成/文生视频/MiniMax H3 T2V 文生视频_2097227552527052802.json, 视频生成/文生视频/MiniMax H3 T2V（文生视频）_2084535052926545922.json, 视频生成/文生视频/MiniMax H3 T2V（文生视频）_2092541585006354433.json, 视频生成/文生视频/MiniMax H3 加速版 文生视频_2086639037351284737.json, 视频生成/文生视频/MiniMax H3 图生视频（SageAttention 加速版）_2085990371192037378.json, 视频生成/文生视频/MiniMax H3 图生视频（SageAttention+LoRA 双重加速）_2086288398037372929.json, 视频生成/文生视频/MiniMax H3 多参生视频 加速版_2084297922312761346.json, 视频生成/文生视频/MiniMax H3多参2倍速（开源版）V2_2086281240478576641.json, 视频生成/文生视频/MiniMax+H3+开源版！多图参考生视频！_2084526961619202049.json, 视频生成/文生视频/Minimax H3文生视频、图生视频、参考生视频、动作迁移、人物替换自由切换，双重加速版_2086132690054639617.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_21

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 T2V comfyorg_2084874841076887553.json、视频生成/文生视频/MiniMax H3 T2V 文生视频 加速版_2086019169908248577.json、视频生成/文生视频/MiniMax H3 T2V 文生视频_2089602856834912257.json、视频生成/文生视频/MiniMax H3 T2V 文生视频_2097227552527052802.json、视频生成/文生视频/MiniMax H3 T2V（文生视频）_2084535052926545922.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 11/13 个有
- `SaveVideo` —— 11/13 个有
- `MiniMaxH3ImageToVideo` —— 10/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/13 个有
- `UNETLoader` —— 9/13 个有
- `Label (rgthree)` —— 6/13 个有
- `LoadImage` —— 6/13 个有
- `PrimitiveStringMultiline` —— 6/13 个有
- `DiffusionModelLoaderKJ` —— 4/13 个有
- `GetNode` —— 4/13 个有
- `SetNode` —— 4/13 个有
- `VHS_LoadVideo` —— 4/13 个有
- `LoadAudio` —— 3/13 个有
- `MiniMaxH3BlockCacheT8` —— 3/13 个有
- `MiniMaxH3ReferenceToVideo` —— 3/13 个有
- `Fast Groups Bypasser (rgthree)` —— 2/13 个有
- `LoraLoaderBypassModelOnly` —— 2/13 个有
- `SaveImage` —— 2/13 个有
- `Text` —— 2/13 个有
- `VHS_VideoCombine` —— 2/13 个有
- `CM_FloatToInt` —— 1/13 个有
- `CR Prompt Text` —— 1/13 个有
- `DuckHideNode` —— 1/13 个有
- `Int` —— 1/13 个有
- `RHMiniMaxH3Ref2VAImageReference` —— 1/13 个有
- `Switch any [Crystools]` —— 1/13 个有
- `VHS_VideoInfo` —— 1/13 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 1/13 个有
- `孤海注释` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
