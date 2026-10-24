---
name: unknown_workflow_sampler_unet_vae_135
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.79775
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3文生视频Org开源版_2084176715890380801.json, 视频生成/文生视频/MiniMax H3文生视频_2089703538363555842.json, 视频生成/文生视频/MiniMax H3文生视频工作流_2084632853681369090.json, 视频生成/文生视频/MiniMax H3：文生视频_2085911182791241729.json, 视频生成/文生视频/MiniMax H3：文生视频_2095792903498067969.json, 视频生成/文生视频/MiniMax 文生视频-Sage Attention 加速版工作流_2084924005185843201.json, 视频生成/文生视频/MiniMax+H3+开源版！文生视频！_2084526946423234561.json, 视频生成/文生视频/Minimax H3 Veda 稀疏注意力8步极速版 文生视频_2108479691337326593.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_135

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3文生视频Org开源版_2084176715890380801.json、视频生成/文生视频/MiniMax H3文生视频_2089703538363555842.json、视频生成/文生视频/MiniMax H3文生视频工作流_2084632853681369090.json、视频生成/文生视频/MiniMax H3：文生视频_2085911182791241729.json、视频生成/文生视频/MiniMax H3：文生视频_2095792903498067969.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 7/8 个有
- `ResolutionSelector` —— 7/8 个有
- `SaveVideo` —— 7/8 个有
- `PrimitiveInt` —— 3/8 个有
- `CR Text` —— 2/8 个有
- `ComfySwitchNode` —— 2/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `PathchSageAttentionKJ` —— 2/8 个有
- `PrimitiveBoolean` —— 2/8 个有
- `DuckHideNode` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `SaveImage` —— 1/8 个有
- `SpectrumSDXL` —— 1/8 个有
- `VHS_VideoCombine` —— 1/8 个有
- `VedaSparseAttention` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
