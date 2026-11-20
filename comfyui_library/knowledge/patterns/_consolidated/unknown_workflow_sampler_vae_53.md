---
name: unknown_workflow_sampler_vae_53
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.847
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3｜5图多参考快速出片｜5-15秒｜稳定版_2091107780571783170.json, 视频生成/文生视频/MiniMax+H3+T2V+文生视频+加速版_2084297867275096065.json, 视频生成/文生视频/MiniMax+H3+T2V+文生视频低显存加速版（6~8GB）_2085705254150168577.json, 视频生成/文生视频/MiniMax+H3+开源版！多图参考生视频！_2084526961619202049.json, 视频生成/文生视频/MiniMax+H3+开源版！文生视频！_2084526946423234561.json, 视频生成/文生视频/minimaxH3文生+参考生视频_2084286286344581121.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_53

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3｜5图多参考快速出片｜5-15秒｜稳定版_2091107780571783170.json、视频生成/文生视频/MiniMax+H3+T2V+文生视频+加速版_2084297867275096065.json、视频生成/文生视频/MiniMax+H3+T2V+文生视频低显存加速版（6~8GB）_2085705254150168577.json、视频生成/文生视频/MiniMax+H3+开源版！多图参考生视频！_2084526961619202049.json、视频生成/文生视频/MiniMax+H3+开源版！文生视频！_2084526946423234561.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `PrimitiveStringMultiline` —— 5/6 个有
- `VAEDecode` —— 5/6 个有
- `MiniMaxH3ImageToVideo` —— 4/6 个有
- `SaveImage` —— 4/6 个有
- `UNETLoader` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/6 个有
- `MiniMaxH3ReferenceToVideo` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `DiffusionModelLoaderKJ` —— 2/6 个有
- `DuckHideNode` —— 2/6 个有
- `VHS_LoadVideo` —— 2/6 个有
- `LoadAudio` —— 1/6 个有
- `LoadVideo` —— 1/6 个有
- `RHMiniMaxH3Ref2VAImageReference` —— 1/6 个有
- `TextInput_` —— 1/6 个有
- `UniBlockSwap` —— 1/6 个有
- `VAEDecodeTiled` —— 1/6 个有
- `easy positive` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
