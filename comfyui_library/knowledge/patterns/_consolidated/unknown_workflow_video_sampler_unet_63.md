---
name: unknown_workflow_video_sampler_unet_63
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.777143
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/H3全能参考工作流_2093000289442942977.json, 视频生成/文生视频/MINIMAX-H3 多参工作流_2084509251074093057.json, 视频生成/文生视频/MINIMAX-H3 文生_单图_首尾帧 工作流_2085269429079855106.json, 视频生成/文生视频/MINIMAX-H3多参_2086757864504385537.json, 视频生成/文生视频/MiniMaxH3+多合一稳定MAX｜4步8步加速（自用）_2092482860316971010.json, 视频生成/文生视频/MiniMaxH3三合一简易稳定生产力Pro_2087108217645133826.json, 视频生成/文生视频/视频生成（文生_图生_参考生）Minimax-H3_2087564591730618370.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_63

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/H3全能参考工作流_2093000289442942977.json、视频生成/文生视频/MINIMAX-H3 多参工作流_2084509251074093057.json、视频生成/文生视频/MINIMAX-H3 文生_单图_首尾帧 工作流_2085269429079855106.json、视频生成/文生视频/MINIMAX-H3多参_2086757864504385537.json、视频生成/文生视频/MiniMaxH3+多合一稳定MAX｜4步8步加速（自用）_2092482860316971010.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 7 个 workflow 都包含：
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
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 6/7 个有
- `LoadAudio` —— 6/7 个有
- `MiniMaxH3ReferenceToVideo` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `VHS_LoadVideo` —— 6/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `MiniMaxH3ImageToVideo` —— 4/7 个有
- `CFGGuider` —— 1/7 个有
- `ConditioningZeroOut` —— 1/7 个有
- `ImpactSwitch` —— 1/7 个有
- `LazySwitchKJ` —— 1/7 个有
- `MiniMaxH3BlockCacheT8` —— 1/7 个有
- `MiniMaxH3SigmaShift` —— 1/7 个有
- `MuyeTextEditOutput` —— 1/7 个有
- `PrimitiveBoolean` —— 1/7 个有
- `ReservedVRAMSetter` —— 1/7 个有
- `UniBlockSwap` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
