---
name: unknown_workflow_sampler_vae_54
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9755
common_nodes: [BasicGuider, BasicScheduler, CreateVideo, KSamplerSelect, MiniMaxH3Easy, MiniMaxH3EasyLoader, MiniMaxH3EasyOutput, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeAudio]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 真全能参考工作流_2085567946600046593.json, 视频生成/文生视频/MiniMax_H3_Easy_hybrid全能参考极简多合一工作流_2105216168821878786.json, 视频生成/文生视频/MiniMax_H3_全能参考-即梦写法_2085624803662323714.json, 视频生成/文生视频/MinimaxH3工作流多合一极简版_2088792747246444545.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_54

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 真全能参考工作流_2085567946600046593.json、视频生成/文生视频/MiniMax_H3_Easy_hybrid全能参考极简多合一工作流_2105216168821878786.json、视频生成/文生视频/MiniMax_H3_全能参考-即梦写法_2085624803662323714.json、视频生成/文生视频/MinimaxH3工作流多合一极简版_2088792747246444545.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyLoader`
- `MiniMaxH3EasyOutput`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeAudio`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/4 个有
- `PathchSageAttentionKJ` —— 3/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `AudioAdjustVolume` —— 1/4 个有
- `EasyCache` —— 1/4 个有
- `MiniMaxH3BlockCacheT8` —— 1/4 个有
- `MiniMaxH3EasyMediaLoader` —— 1/4 个有
- `SolAttnPatch` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
