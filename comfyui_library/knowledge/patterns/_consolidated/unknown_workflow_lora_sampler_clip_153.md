---
name: unknown_workflow_lora_sampler_clip_153
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.773
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DeepTranslatorTextNode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LoadImageMask, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, String Literal, Text, Text Load Line From File, UNETLoader, VAEDecode, VAELoader, easy forLoopEnd, easy forLoopStart]
problems: []
missing: [String Literal, Text Load Line From File, easy forLoopEnd, easy forLoopStart]
members: [图片生成/文生图/1947936412476801026.json, 图片生成/文生图/1948523697077387265.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_153

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1947936412476801026.json、图片生成/文生图/1948523697077387265.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DeepTranslatorTextNode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoadImageMask`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `String Literal`
- `Text`
- `Text Load Line From File`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy forLoopEnd`
- `easy forLoopStart`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | - | 2 | 100% |
| 高度 | 1552 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1552，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：String Literal、Text Load Line From File、easy forLoopEnd、easy forLoopStart
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
