---
name: unknown_workflow_lora_sampler_clip_315
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.961
common_nodes: [ApplyPulidFlux, CLIPTextEncode, CR Text, DeepTranslatorTextNode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, JoinStringMulti, KSampler, LoadImage, LoraLoaderModelOnly, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, SaveImage, Text Multiline (Code Compatible), UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/全能图片G-4o可爱Q版玩偶手办套装_1911234851108810753.json, 平台全量/全能图片G4o可爱Q版3D玩偶手办玩具套装-StarAI_1911176835886186497.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_315

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/全能图片G-4o可爱Q版玩偶手办套装_1911234851108810753.json、平台全量/全能图片G4o可爱Q版3D玩偶手办玩具套装-StarAI_1911176835886186497.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyPulidFlux`
- `CLIPTextEncode`
- `CR Text`
- `DeepTranslatorTextNode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `JoinStringMulti`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `SaveImage`
- `Text Multiline (Code Compatible)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Joy_caption` —— 1/2 个有
- `Joy_caption_load` —— 1/2 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/2 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 28，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
