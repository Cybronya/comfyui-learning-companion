---
name: unknown_workflow_sampler_unet_vae_31
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.8698
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Minimax-H3-T2V 开源版本+文生视频_2084249084893945858.json, 视频生成/文生视频/Minimax-H3-文生视频-sage+cache双重加速（5秒3.5分钟）_2084572415069351938.json, 视频生成/文生视频/Minimax-H3-文生视频BF16高质量768P-双重加速（T8-cache）_2085387569700888577.json, 视频生成/文生视频/Minimax-H3-文生视频（Lightx2v加速）_2085988885787660289.json, 视频生成/文生视频/Minimax-H3-文生视频（Lightx2v正式版）_2087549637837283330.json, 视频生成/文生视频/Minimax-H3_T2V（文生视频_本地可用）_2084287507390353409.json, 视频生成/文生视频/Minimax-H3文生视频8步工作流_2095380668011343873.json, 视频生成/文生视频/MinimaxH3LORA加速工作流ENG文生视频4步ENG_2087097542533279745.json, 视频生成/文生视频/MinimaxH3文生视频 量化加速版_2084540140541792258.json, 视频生成/文生视频/MinimaxH3文生视频 量化加速版_2084680217980915713.json, 视频生成/文生视频/MinimaxH3文生视频4步LORA加速工作流_2084217093255421954.json, 视频生成/文生视频/MinimaxH3文生视频8步工作流_2087038591577972737.json, 视频生成/文生视频/MinimaxH3文生视频8步工作流_2099773191228051457.json, 视频生成/文生视频/Minimax文生视频(2倍速！量化加速版)_2084823710980206594.json, 视频生成/文生视频/Minimax文生视频高质量极速版_2084997026189758466.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_31

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/文生视频/Minimax-H3-T2V 开源版本+文生视频_2084249084893945858.json、视频生成/文生视频/Minimax-H3-文生视频-sage+cache双重加速（5秒3.5分钟）_2084572415069351938.json、视频生成/文生视频/Minimax-H3-文生视频BF16高质量768P-双重加速（T8-cache）_2085387569700888577.json、视频生成/文生视频/Minimax-H3-文生视频（Lightx2v加速）_2085988885787660289.json、视频生成/文生视频/Minimax-H3-文生视频（Lightx2v正式版）_2087549637837283330.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 15 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 7/15 个有
- `CR Prompt Text` —— 6/15 个有
- `PathchSageAttentionKJ` —— 6/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/15 个有
- `SolAttnPatch` —— 3/15 个有
- `EasyCache` —— 2/15 个有
- `Float` —— 2/15 个有
- `MiniMaxH3BlockCacheT8` —— 2/15 个有
- `MuyeTextEditOutput` —— 2/15 个有
- `RTXVideoSuperResolution` —— 2/15 个有
- `easy int` —— 2/15 个有
- `ModelAttentionBackend` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
