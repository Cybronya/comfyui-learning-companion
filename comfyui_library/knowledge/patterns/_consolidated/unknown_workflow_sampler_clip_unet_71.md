---
name: unknown_workflow_sampler_clip_unet_71
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.78275
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, LayerUtility: PurgeVRAM V2, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: PurgeVRAM V2, easy cleanGpuUsed]
members: [图片生成/文生图/1967418961937698817.json, 图片生成/文生图/1968322626772979714.json, 图片生成/文生图/1971799414320852993.json, 图片生成/文生图/1973761942366064641.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_71

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1967418961937698817.json、图片生成/文生图/1968322626772979714.json、图片生成/文生图/1971799414320852993.json、图片生成/文生图/1973761942366064641.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/4 个有
- `SeedVR2` —— 3/4 个有
- `AILab_QwenVL` —— 1/4 个有
- `CustomAddLabel` —— 1/4 个有
- `Int` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `RH_Translator` —— 1/4 个有
- `ShowText` —— 1/4 个有
- `TeaCache` —— 1/4 个有
- `Text` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM V2、easy cleanGpuUsed
