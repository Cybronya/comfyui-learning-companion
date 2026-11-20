---
name: unknown_workflow_sampler_checkpoint_unet
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8145
common_nodes: [Anything Everywhere, Anything Everywhere3, CR SDXL Aspect Ratio, CR Split String, CR Text, CheckpointLoaderSimple, EmptyLatentImage, Fast Bypasser (rgthree), JjkText, MZ_ChatGLM3, MZ_ChatGLM3Loader, MZ_KolorsUNETLoader, ModelMergeSimple, Mute / Bypass Repeater (rgthree), SaveImage, SeaArtAppendPrompt, SeaArtApplyStory, SeaArtMergeStoryCondition, SeaArtStoryKSampler, TextCombinerTwo, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/角色一致性N8_1891102565306634242.json, 平台全量/角色一致性N20_1891045219503083521.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_unet

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/角色一致性N8_1891102565306634242.json、平台全量/角色一致性N20_1891045219503083521.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `Anything Everywhere3`
- `CR SDXL Aspect Ratio`
- `CR Split String`
- `CR Text`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `Fast Bypasser (rgthree)`
- `JjkText`
- `MZ_ChatGLM3`
- `MZ_ChatGLM3Loader`
- `MZ_KolorsUNETLoader`
- `ModelMergeSimple`
- `Mute / Bypass Repeater (rgthree)`
- `SaveImage`
- `SeaArtAppendPrompt`
- `SeaArtApplyStory`
- `SeaArtMergeStoryCondition`
- `SeaArtStoryKSampler`
- `TextCombinerTwo`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 3.5 | - | 2 | 100% |
| 采样算法 | dpmpp_2m_sde_gpu | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde_gpu，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
