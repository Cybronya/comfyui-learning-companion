---
name: unknown_workflow_sampler_unet_vae_58
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.704364
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3：文生视频_2085911182791241729.json, 视频生成/文生视频/MiniMax H3：文生视频_2095792903498067969.json, 视频生成/文生视频/MiniMax 文生视频-Sage Attention 加速版工作流_2084924005185843201.json, 视频生成/文生视频/MiniMax+H3+文生视频_2084466075869208578.json, 视频生成/文生视频/MiniMax-4步加速工作流_2085226868072083458.json, 视频生成/文生视频/MiniMax-H3 图生视频 5秒1080p视频只需8分钟+全节点注释_2084557666449444865.json, 视频生成/文生视频/MiniMax-H3 文生视频 5秒1080p视频只需8分钟+全节点注释_2084777365707776002.json, 视频生成/文生视频/MiniMax-H3 文生视频 5秒1080p视频只需8分钟+全节点注释_2094043847910318082.json, 视频生成/文生视频/MiniMax-H3-参考生视频_2085243192571686914.json, 视频生成/文生视频/MiniMaxH3+多合一稳定MAX｜4步8步加速（自用）_2092482860316971010.json, 视频生成/文生视频/Minimax H3 Veda 稀疏注意力8步极速版 文生视频_2108479691337326593.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_58

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3：文生视频_2085911182791241729.json、视频生成/文生视频/MiniMax H3：文生视频_2095792903498067969.json、视频生成/文生视频/MiniMax 文生视频-Sage Attention 加速版工作流_2084924005185843201.json、视频生成/文生视频/MiniMax+H3+文生视频_2084466075869208578.json、视频生成/文生视频/MiniMax-4步加速工作流_2085226868072083458.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 10/11 个有
- `SaveVideo` —— 10/11 个有
- `MiniMaxH3ImageToVideo` —— 9/11 个有
- `PrimitiveFloat` —— 8/11 个有
- `LoadImage` —— 6/11 个有
- `PathchSageAttentionKJ` —— 6/11 个有
- `EasyCache` —— 4/11 个有
- `LoraLoaderModelOnly` —— 4/11 个有
- `PrimitiveStringMultiline` —— 4/11 个有
- `CR Text` —— 3/11 个有
- `Int` —— 3/11 个有
- `MiniMaxH3ReferenceToVideo` —— 3/11 个有
- `PrimitiveBoolean` —— 3/11 个有
- `ComfySwitchNode` —— 2/11 个有
- `LoadAudio` —— 2/11 个有
- `PrimitiveInt` —— 2/11 个有
- `VHS_LoadVideo` —— 2/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `LazySwitchKJ` —— 1/11 个有
- `MiniMaxH3SigmaShift` —— 1/11 个有
- `VHS_VideoCombine` —— 1/11 个有
- `VedaSparseAttention` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
