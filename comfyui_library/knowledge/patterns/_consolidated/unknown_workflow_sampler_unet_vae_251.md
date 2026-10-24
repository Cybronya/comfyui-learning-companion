---
name: unknown_workflow_sampler_unet_vae_251
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.82375
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/动作迁MINIMAX-H3移ENG角色一致性动作迁移图生视频_2087087046383984642.json, 视频生成/图生视频/参考生视频_MiniMax H3_2084453784557809665.json, 视频生成/图生视频/多参图生视频-开源版MIniMAXH3_2084494818100731905.json, 视频生成/图生视频/海螺H3八步极速生成全能参考生视频_2087529254698446850.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_251

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/动作迁MINIMAX-H3移ENG角色一致性动作迁移图生视频_2087087046383984642.json、视频生成/图生视频/参考生视频_MiniMax H3_2084453784557809665.json、视频生成/图生视频/多参图生视频-开源版MIniMAXH3_2084494818100731905.json、视频生成/图生视频/海螺H3八步极速生成全能参考生视频_2087529254698446850.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 2/4 个有
- `AILab_ImageStitch` —— 1/4 个有
- `AnyBooleanSwitch` —— 1/4 个有
- `CM_IntToFloat` —— 1/4 个有
- `GetVideoComponents` —— 1/4 个有
- `JoinStrings` —— 1/4 个有
- `LoadVideo` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有
- `easy int` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
