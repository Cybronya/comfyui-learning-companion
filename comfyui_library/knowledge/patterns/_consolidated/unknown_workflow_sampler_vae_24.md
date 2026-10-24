---
name: unknown_workflow_sampler_vae_24
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.864273
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax+H3+H25  多参8步视频生成_2090783049813413889.json, 视频生成/图生视频/MiniMax-H3 Ref2va 参考生视频标准版_2095421074551951361.json, 视频生成/图生视频/MiniMaxH3_参考生_参考图_无加速_有LoRA_---(4)_2090348925667602434.json, 视频生成/图生视频/MiniMaxH3多图参考生视频！加速版！艾橘溪_2084254355036925953.json, 视频生成/图生视频/MiniMax_H3_R2V_3参考图_LightX2V_4步_2090336616714956801.json, 视频生成/图生视频/Minimax H3 Veda 稀疏注意力8步极速版 参考生视频_2108491242530234370.json, 视频生成/图生视频/Minimax H3 参考图和参考视音频生成视频满血版_2105625287546462210.json, 视频生成/图生视频/单图参考生视频 生产力版 MiniMax+H3+H25+Hybrid_2088526268315820034.json, 视频生成/文生视频/10ErosMax+test4多参考_2087899966655262721.json, 视频生成/文生视频/MiniMax H3 H25 Hybrid 多参8步最优对比测试_2088184113558806529.json, 视频生成/文生视频/MiniMax+H3+H25+Hybrid+多参8步最优实现_2088303974402318338.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_24

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/MiniMax+H3+H25  多参8步视频生成_2090783049813413889.json、视频生成/图生视频/MiniMax-H3 Ref2va 参考生视频标准版_2095421074551951361.json、视频生成/图生视频/MiniMaxH3_参考生_参考图_无加速_有LoRA_---(4)_2090348925667602434.json、视频生成/图生视频/MiniMaxH3多图参考生视频！加速版！艾橘溪_2084254355036925953.json、视频生成/图生视频/MiniMax_H3_R2V_3参考图_LightX2V_4步_2090336616714956801.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
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
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 10/11 个有
- `LoraLoaderModelOnly` —— 9/11 个有
- `LoadAudio` —— 8/11 个有
- `UNETLoader` —— 8/11 个有
- `LoadVideo` —— 7/11 个有
- `PathchSageAttentionKJ` —— 7/11 个有
- `GetVideoComponents` —— 6/11 个有
- `MiniMaxH3SigmaShift` —— 5/11 个有
- `MiniMaxH3HybridLoader` —— 4/11 个有
- `TrimAudioDuration` —— 4/11 个有
- `Video Slice` —— 4/11 个有
- `AddLabel` —— 3/11 个有
- `ImageScaleToTotalPixels` —— 3/11 个有
- `ComfySwitchNode` —— 2/11 个有
- `PrimitiveBoolean` —— 2/11 个有
- `PrimitiveInt` —— 2/11 个有
- `LoraLoaderBypassModelOnly` —— 1/11 个有
- `VedaSparseAttention` —— 1/11 个有
- `easy imageRemBg` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
