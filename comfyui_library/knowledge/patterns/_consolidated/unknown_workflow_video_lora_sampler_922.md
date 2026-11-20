---
name: unknown_workflow_video_lora_sampler_922
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.987333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyMediaLoader, MiniMaxH3EasyModelAdapter, MiniMaxH3EasyOutput, ModelAttentionBackend, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/漫剧自用，低消耗版_2096831553887358978.json, 视频生成/文生视频/图音视参考工作流_2101747777444343810.json, 视频生成/视频生视频/图音视参考工作流_2120732126168571906.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_922

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/漫剧自用，低消耗版_2096831553887358978.json、视频生成/文生视频/图音视参考工作流_2101747777444343810.json、视频生成/视频生视频/图音视参考工作流_2120732126168571906.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 3 个 workflow 都包含：
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
- `GetLatentSizeAndCount` —— 2/3 个有
- `H3SigmaRefiner` —— 2/3 个有
- `Seed (rgthree)` —— 2/3 个有
- `VAEDecode` —— 2/3 个有
- `MiniMaxH3ChunkFeedForward` —— 1/3 个有
- `MiniMaxH3SigmaShift` —— 1/3 个有
- `MiniMaxLowVRAMAttention` —— 1/3 个有
- `SolAttnPatch` —— 1/3 个有
- `XB_VAEDecode` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
