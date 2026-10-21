---
name: unknown_workflow_sampler_clip_unet_223
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.828
common_nodes: [AILab_QwenVL, BasicGuider, BasicScheduler, CLIPTextEncode, CustomAddLabel, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, Int, JjkText, KSamplerSelect, LayerUtility: PurgeVRAM V2, ModelSamplingFlux, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SeedVR2, ShowText, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: PurgeVRAM V2, easy cleanGpuUsed]
members: [图片生成/文生图/1973761942366064641.json, 图片生成/文生图/SRPO-image-generation-电影级皮肤质感-文生图-自动提示词_2025756081611345922.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_223

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1973761942366064641.json、图片生成/文生图/SRPO-image-generation-电影级皮肤质感-文生图-自动提示词_2025756081611345922.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CustomAddLabel`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `Int`
- `JjkText`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `ModelSamplingFlux`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2`
- `ShowText`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BatchTextReplace` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `Text` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy ifElse` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM V2、easy cleanGpuUsed
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
