---
name: unknown_workflow_sampler_vae_72
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.926
common_nodes: [BasicGuider, BasicScheduler, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3Easy, MiniMaxH3EasyLoader, MiniMaxH3EasyOutput, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeAudio, VHS_LoadVideo]
problems: []
missing: []
members: [视频生成/图生视频/minimax_h3_r2v参考生视频_2087105829878190082.json, 视频生成/文生视频/MiniMax H3 真全能参考工作流_2085567946600046593.json, 视频生成/文生视频/MiniMax_H3_全能参考-即梦写法_2085624803662323714.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_72

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/minimax_h3_r2v参考生视频_2087105829878190082.json、视频生成/文生视频/MiniMax H3 真全能参考工作流_2085567946600046593.json、视频生成/文生视频/MiniMax_H3_全能参考-即梦写法_2085624803662323714.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyLoader`
- `MiniMaxH3EasyOutput`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeAudio`
- `VHS_LoadVideo`

**可变部分**（部分 workflow 才有）：
- `EasyCache` —— 2/3 个有
- `LoadAudio` —— 2/3 个有
- `AudioAdjustVolume` —— 1/3 个有
- `ComfySwitchNode` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `MiniMaxH3BlockCacheT8` —— 1/3 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/3 个有
- `SolAttnPatch` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
