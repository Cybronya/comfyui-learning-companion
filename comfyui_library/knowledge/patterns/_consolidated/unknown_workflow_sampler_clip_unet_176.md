---
name: unknown_workflow_sampler_clip_unet_176
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.873667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [Text Concatenate, Text Multiline]
members: [图片生成/文生图/1902293777606975490.json, 图片生成/文生图/1904702749529845761.json, 图片生成/文生图/1906558127117111297.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_176

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1902293777606975490.json、图片生成/文生图/1904702749529845761.json、图片生成/文生图/1906558127117111297.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `ControlNetLoader` —— 1/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `InfiniteYouApply` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `UltimateSDUpscale` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1152 | - | 2 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1152，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 这些节点还没有知识卡，系统对它们的理解有限：Text Concatenate、Text Multiline
