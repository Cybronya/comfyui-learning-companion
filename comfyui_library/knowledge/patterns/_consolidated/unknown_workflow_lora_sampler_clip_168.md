---
name: unknown_workflow_lora_sampler_clip_168
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9145
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, DetailDaemonSamplerNode, DualCLIPLoader, Image Comparer (rgthree), JWImageResizeByLongerSide, KSamplerSelect, LoadImage, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, StyleModelApplySimple, StyleModelLoader, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [CR Text]
members: [图片生成/文生图/1981983365639356418.json, 图片生成/文生图/Flux基础文生图工作流_1997984984822611970.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_168

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1981983365639356418.json、图片生成/文生图/Flux基础文生图工作流_1997984984822611970.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `DetailDaemonSamplerNode`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `JWImageResizeByLongerSide`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelApplySimple`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Joy_caption_two` —— 1/2 个有
- `Joy_caption_two_load` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
