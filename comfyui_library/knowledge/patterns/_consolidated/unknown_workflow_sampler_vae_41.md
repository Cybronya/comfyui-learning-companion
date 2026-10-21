---
name: unknown_workflow_sampler_vae_41
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.984
common_nodes: [BasicGuider, BasicScheduler, CreateVideo, LoadAudio, LoadImage, MiniMaxH3Easy, MiniMaxH3EasyLoader, MiniMaxH3EasyOutput, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeAudio]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 一站式工作流_2110358590795108353.json, 视频生成/文生视频/MiniMax H3 真全能参考工作流_2085567946600046593.json, 视频生成/文生视频/MiniMax_H3_全能参考-即梦写法_2085624803662323714.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_41

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 一站式工作流_2110358590795108353.json、视频生成/文生视频/MiniMax H3 真全能参考工作流_2085567946600046593.json、视频生成/文生视频/MiniMax_H3_全能参考-即梦写法_2085624803662323714.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CreateVideo`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyLoader`
- `MiniMaxH3EasyOutput`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeAudio`

**可变部分**（部分 workflow 才有）：
- `KSamplerSelect` —— 2/3 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `AudioAdjustVolume` —— 1/3 个有
- `EasyCache` —— 1/3 个有
- `LoadVideo` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `MiniMaxH3BlockCacheT8` —— 1/3 个有
- `MiniMaxH3TurboLoRA` —— 1/3 个有
- `MiniMaxH3TurboSampler` —— 1/3 个有
- `SolAttnPatch` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
