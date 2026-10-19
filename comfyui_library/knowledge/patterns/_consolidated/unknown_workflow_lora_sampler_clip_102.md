---
name: unknown_workflow_lora_sampler_clip_102
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8915
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, HD UltimateSDUpscale]
members: [图片生成/文生图/1922342634764042241.json, 图片生成/文生图/1942877686643798017.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_102

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1922342634764042241.json、图片生成/文生图/1942877686643798017.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `HD UltimateSDUpscale` —— 1/2 个有
- `ImageCompositeWatermark` —— 1/2 个有
- `LayerMask: LoadSegmentAnythingModels` —— 1/2 个有
- `LayerMask: SegmentAnythingUltra V3` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 832 | - | 2 | 92% |
| 高度 | 928 | - | 2 | 55% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 832，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- 高度 中位数 928，样本不足，未给区间，2 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：LayerMask: LoadSegmentAnythingModels、LayerMask: SegmentAnythingUltra V3、HD UltimateSDUpscale
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
