---
name: unknown_workflow_video_lora_sampler_983
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.981
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyMediaLoader, MiniMaxH3EasyModelAdapter, MiniMaxH3EasyOutput, ModelAttentionBackend, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/漫剧自用，低消耗版_2096831553887358978.json, 视频生成/文生视频/图音视参考工作流_2101747777444343810.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_983

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/漫剧自用，低消耗版_2096831553887358978.json、视频生成/文生视频/图音视参考工作流_2101747777444343810.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyMediaLoader`
- `MiniMaxH3EasyModelAdapter`
- `MiniMaxH3EasyOutput`
- `ModelAttentionBackend`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetLatentSizeAndCount` —— 1/2 个有
- `H3SigmaRefiner` —— 1/2 个有
- `MiniMaxH3ChunkFeedForward` —— 1/2 个有
- `MiniMaxH3SigmaShift` —— 1/2 个有
- `MiniMaxLowVRAMAttention` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有
- `SolAttnPatch` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `XB_VAEDecode` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
