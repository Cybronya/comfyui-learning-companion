---
name: unknown_workflow_sampler_unet_vae_168
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.838143
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/开源 Minimax-H3 多参全模态音视频生成_2084313713590493186.json, 视频生成/图生视频/开源 Minimax-H3 数字人（多参视频生成）_2084210486131908609.json, 视频生成/图生视频/海螺H3 多参视频（加速节点-加速版）768P_2085282734813044738.json, 视频生成/图生视频/海螺H3 数字人（多参视频生成）开源版_2085277180266893314.json, 视频生成/图生视频/海螺H3八步极速生成全能参考生视频_2087529254698446850.json, 视频生成/文生视频/Minimax H3多参视频生成+全节点注释_2084873538615472129.json, 视频生成/文生视频/Minimax-h3 多模态全能参考版_2093519190757044225.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_168

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/开源 Minimax-H3 多参全模态音视频生成_2084313713590493186.json、视频生成/图生视频/开源 Minimax-H3 数字人（多参视频生成）_2084210486131908609.json、视频生成/图生视频/海螺H3 多参视频（加速节点-加速版）768P_2085282734813044738.json、视频生成/图生视频/海螺H3 数字人（多参视频生成）开源版_2085277180266893314.json、视频生成/图生视频/海螺H3八步极速生成全能参考生视频_2087529254698446850.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 5/7 个有
- `ResolutionSelector` —— 5/7 个有
- `CR Text` —— 4/7 个有
- `PathchSageAttentionKJ` —— 4/7 个有
- `PrimitiveStringMultiline` —— 4/7 个有
- `VHS_LoadVideoFFmpeg` —— 4/7 个有
- `Label (rgthree)` —— 3/7 个有
- `EasyCache` —— 2/7 个有
- `Int` —— 2/7 个有
- `AnyBooleanSwitch` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `MiniMaxH3BlockCacheT8` —— 1/7 个有
- `PrimitiveBoolean` —— 1/7 个有
- `SolAttnPatch` —— 1/7 个有
- `Text` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
