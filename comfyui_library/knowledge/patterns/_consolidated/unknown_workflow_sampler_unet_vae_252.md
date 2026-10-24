---
name: unknown_workflow_sampler_unet_vae_252
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.71625
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/海螺文生视频_2085524853020512258.json, 视频生成/文生视频/超强文生视频MiniMax-H3 ！加速版！_2086330916049346562.json, 视频生成/文生视频/迄今超强MiniMax-H3文生视频！2倍速！量化加速官方8步Lora再提速50%_1926516021497335809.json, 视频生成/文生视频/首尾帧加速图minimax_h3_lightx2v生文生ENG_2087087697318998017.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_252

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/海螺文生视频_2085524853020512258.json、视频生成/文生视频/超强文生视频MiniMax-H3 ！加速版！_2086330916049346562.json、视频生成/文生视频/迄今超强MiniMax-H3文生视频！2倍速！量化加速官方8步Lora再提速50%_1926516021497335809.json、视频生成/文生视频/首尾帧加速图minimax_h3_lightx2v生文生ENG_2087087697318998017.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 4 个 workflow 都包含：
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
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/4 个有
- `JjkText` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `EasyCache` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
