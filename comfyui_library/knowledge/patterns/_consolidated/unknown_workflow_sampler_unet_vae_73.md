---
name: unknown_workflow_sampler_unet_vae_73
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8116
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, CreateVideo, MiniMaxH3ImageToVideo, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax-H3 fl2v_turbo加速_2088880527356026881.json, 视频生成/文生视频/MiniMaxH3_Larryvrh版加速_2085706255410225153.json, 视频生成/文生视频/MiniMaxh3双重加速文生视频_2087002916589756417.json, 视频生成/文生视频/Minimax H3 FL2VA 图片首尾帧视频_2095354444597784577.json, 视频生成/文生视频/Minimax H3 图生视频 最新8步增速工作流+全节点注释_2088628478857015297.json, 视频生成/文生视频/Minimax H3 文生视频 最新8步增速工作流_2087823188460920833.json, 视频生成/文生视频/Minimax H3 文生视频_2089487806417694721.json, 视频生成/文生视频/comfyui官方工作流-video_minimax_h3_t2v_2084148000615657474.json, 视频生成/文生视频/minimaxH3开源版文生视频(20step)_2092291766404870146.json, 视频生成/文生视频/【遇见AI】Minimax H3，文生图基础流_2084511826766811137.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_73

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/MiniMax-H3 fl2v_turbo加速_2088880527356026881.json、视频生成/文生视频/MiniMaxH3_Larryvrh版加速_2085706255410225153.json、视频生成/文生视频/MiniMaxh3双重加速文生视频_2087002916589756417.json、视频生成/文生视频/Minimax H3 FL2VA 图片首尾帧视频_2095354444597784577.json、视频生成/文生视频/Minimax H3 图生视频 最新8步增速工作流+全节点注释_2088628478857015297.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `MiniMaxH3ImageToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 9/10 个有
- `ResolutionSelector` —— 9/10 个有
- `BasicScheduler` —— 8/10 个有
- `KSamplerSelect` —— 6/10 个有
- `LoadImage` —— 6/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/10 个有
- `JjkText` —— 3/10 个有
- `LoraLoaderBypassModelOnly` —— 3/10 个有
- `CR Text` —— 2/10 个有
- `MiniMaxH3DualClockSamplerT8` —— 2/10 个有
- `MiniMaxH3TurboLoRA` —— 2/10 个有
- `MiniMaxH3TurboSampler` —— 2/10 个有
- `PixaromaDuration` —— 1/10 个有
- `PixaromaSizes` —— 1/10 个有
- `Text` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
