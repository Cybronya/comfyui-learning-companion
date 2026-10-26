---
name: unknown_workflow_sampler_unet_vae_115
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.809556
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3：文生视频_2085911182791241729.json, 视频生成/文生视频/MiniMax H3：文生视频_2095792903498067969.json, 视频生成/文生视频/MiniMax 文生视频-Sage Attention 加速版工作流_2084924005185843201.json, 视频生成/文生视频/MiniMax+H3+开源版！文生视频！_2084526946423234561.json, 视频生成/文生视频/MiniMaxH3文生视频_2112906168044703746.json, 视频生成/文生视频/MiniMaxH3文生视频_2113106645902520321.json, 视频生成/文生视频/Minimax H3 文生视频_2085256821585039362.json, 视频生成/文生视频/minimax_h3_t2v官方文生视频_2114188003567554561.json, 视频生成/文生视频/海螺H3-4步lora工作流_2085326968886743042.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_115

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3：文生视频_2085911182791241729.json、视频生成/文生视频/MiniMax H3：文生视频_2095792903498067969.json、视频生成/文生视频/MiniMax 文生视频-Sage Attention 加速版工作流_2084924005185843201.json、视频生成/文生视频/MiniMax+H3+开源版！文生视频！_2084526946423234561.json、视频生成/文生视频/MiniMaxH3文生视频_2112906168044703746.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/9 个有
- `ComfySwitchNode` —— 3/9 个有
- `PathchSageAttentionKJ` —— 3/9 个有
- `PrimitiveBoolean` —— 3/9 个有
- `PrimitiveInt` —— 3/9 个有
- `CR Text` —— 2/9 个有
- `DuckHideNode` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `MiniMaxH3SigmaShift` —— 1/9 个有
- `SaveImage` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
