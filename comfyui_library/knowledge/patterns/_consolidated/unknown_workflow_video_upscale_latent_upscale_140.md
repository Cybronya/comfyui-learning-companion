---
name: unknown_workflow_video_upscale_latent_upscale_140
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.694
common_nodes: [BasicGuider, BasicScheduler, ExtendIntermediateSigmas, FlashVSRNode, GetNode, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3IntegrationAdapterGH, MiniMaxH3IntegrationGH, MiniMaxH3MemoryEfficientSageAttentionPatch, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VHS_VideoCombine, easy anythingIndexSwitch, easy ifElse]
problems: []
missing: []
members: [视频生成/图生视频/【MINIMAX-H3】地表最强能文能武双采工作流_2102043265943031809.json, 视频生成/文生视频/【MINIMAX-H3】地表最强能文能武双采工作流_2102043265943031809.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_140

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/【MINIMAX-H3】地表最强能文能武双采工作流_2102043265943031809.json、视频生成/文生视频/【MINIMAX-H3】地表最强能文能武双采工作流_2102043265943031809.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `ExtendIntermediateSigmas`
- `FlashVSRNode`
- `GetNode`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxH3IntegrationAdapterGH`
- `MiniMaxH3IntegrationGH`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VHS_VideoCombine`
- `easy anythingIndexSwitch`
- `easy ifElse`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
