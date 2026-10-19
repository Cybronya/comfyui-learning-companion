---
name: unknown_workflow_sampler_clip_unet_96
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.693
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSamplerSelect, LoadImage, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text Concatenate, LayerUtility: PurgeVRAM, Lora Loader Stack (rgthree)]
members: [图片生成/文生图/1925439864089530369.json, 图片生成/文生图/1930926287748313090.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_96

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1925439864089530369.json、图片生成/文生图/1930926287748313090.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/2 个有
- `DeepTranslatorTextNode` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `JJC_JoyCaption` —— 1/2 个有
- `JanusImageUnderstanding` —— 1/2 个有
- `JanusModelLoader` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `Lora Loader Stack (rgthree)` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `TextInputBasic` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text Concatenate、LayerUtility: PurgeVRAM、Lora Loader Stack (rgthree)
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
