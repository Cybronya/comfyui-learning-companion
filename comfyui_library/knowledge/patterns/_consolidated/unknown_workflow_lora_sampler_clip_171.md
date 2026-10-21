---
name: unknown_workflow_lora_sampler_clip_171
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9165
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [Text Multiline]
members: [图片生成/文生图/1984515249296523265.json, 图片生成/文生图/Flux文生图-中文提示词_2078378003817656321.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_171

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1984515249296523265.json、图片生成/文生图/Flux文生图-中文提示词_2078378003817656321.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
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
- `ChinesePrompt_Mix` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `Int` —— 1/2 个有
- `JoinStrings` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1536 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
