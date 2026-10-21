---
name: unknown_workflow_lora_sampler_clip_151
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.976
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: TextJoin]
members: [图片生成/文生图/1946032541281251330.json, 图片生成/文生图/1948753188301221890.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_151

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1946032541281251330.json、图片生成/文生图/1948753188301221890.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DisplayText` —— 1/2 个有
- `Joy_caption_two_advanced` —— 1/2 个有
- `Joy_caption_two_load` —— 1/2 个有
- `Joy_extra_options` —— 1/2 个有
- `LayerUtility: TextJoin` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `TextInput_` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | - | 2 | 86% |
| 高度 | 1212 | - | 2 | 84% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 896，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 高度 中位数 1212，样本不足，未给区间，2 个样本，取值集中（一致性 84%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: TextJoin
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
