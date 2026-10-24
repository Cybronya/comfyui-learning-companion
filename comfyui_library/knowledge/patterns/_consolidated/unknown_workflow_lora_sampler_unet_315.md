---
name: unknown_workflow_lora_sampler_unet_315
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.972
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy float]
problems: []
missing: []
members: [视频生成/图生视频/余温MINIMAX H3多参生视频工作流_2110183533531713537.json, 视频生成/文生视频/余温MINIMAX H3多参生视频工作流_2107841554848247809.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_315

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/余温MINIMAX H3多参生视频工作流_2110183533531713537.json、视频生成/文生视频/余温MINIMAX H3多参生视频工作流_2107841554848247809.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy float`

**可变部分**（部分 workflow 才有）：
- `GetVideoComponents` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `RH_Astra` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
