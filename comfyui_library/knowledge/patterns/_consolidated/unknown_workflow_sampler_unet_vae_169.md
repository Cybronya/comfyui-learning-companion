---
name: unknown_workflow_sampler_unet_vae_169
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.733875
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/H3_24G_3refs_声音参考_2106668851638390785.json, 视频生成/图生视频/H3单采版-无LoRA-480P_2099175040867725314.json, 视频生成/图生视频/H3多参图生视频_2084177913167040514.json, 视频生成/图生视频/MINIMAX H3多图参考生视频-lc_2088551068568477698.json, 视频生成/图生视频/MINIMAX H3官方多参工作流_2098996477975687170.json, 视频生成/图生视频/MINIMAX H3超强全能参考 参考图片 参考视频 参考音频 生视频  seedance平替 开源版_2084144506588450818.json, 视频生成/图生视频/MiniMax H3 多图生视频+音频+视频接入_2090198237796982786.json, 视频生成/图生视频/MinimaxH3全能参考多人物短剧工作流(开源量化加速版)速度提升质量不减_2086639379048652802.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_169

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/H3_24G_3refs_声音参考_2106668851638390785.json、视频生成/图生视频/H3单采版-无LoRA-480P_2099175040867725314.json、视频生成/图生视频/H3多参图生视频_2084177913167040514.json、视频生成/图生视频/MINIMAX H3多图参考生视频-lc_2088551068568477698.json、视频生成/图生视频/MINIMAX H3官方多参工作流_2098996477975687170.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 7/8 个有
- `PrimitiveStringMultiline` —— 7/8 个有
- `ResolutionSelector` —— 7/8 个有
- `SaveVideo` —— 7/8 个有
- `VAEDecode` —— 7/8 个有
- `ComfyMathExpression` —— 6/8 个有
- `PrimitiveFloat` —— 6/8 个有
- `GetVideoComponents` —— 3/8 个有
- `LoadVideo` —— 3/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `GetNode` —— 2/8 个有
- `SetNode` —— 2/8 个有
- `VHS_LoadVideo` —— 2/8 个有
- `EasyCache` —— 1/8 个有
- `ImpactFloat` —— 1/8 个有
- `LTXVSeparateAVLatent` —— 1/8 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 1/8 个有
- `PathchSageAttentionKJ` —— 1/8 个有
- `PrimitiveInt` —— 1/8 个有
- `ShowAnything|Mie` —— 1/8 个有
- `VAEDecodeTiled` —— 1/8 个有
- `VHS_VideoCombine` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
