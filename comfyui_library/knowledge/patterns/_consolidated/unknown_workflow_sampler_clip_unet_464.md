---
name: unknown_workflow_sampler_clip_unet_464
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.697
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, PrimitiveStringMultiline, QWEN_TextProcess, RH_Translator, ResolutionSelector, SaveImage, SkipLayerGuidanceDiTSimple, UNETLoader, VAEDecode, VAELoader, ZML_MultiTextInput3, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MOSS-Image _ 8步DMD _ 批量生图_2114233647191650306.json, 图片生成/文生图/MOSS-Image｜SFT 50步高质量文生图·新手入门版_2114188712623034369.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_464

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/MOSS-Image _ 8步DMD _ 批量生图_2114233647191650306.json、图片生成/文生图/MOSS-Image｜SFT 50步高质量文生图·新手入门版_2114188712623034369.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `PrimitiveStringMultiline`
- `QWEN_TextProcess`
- `RH_Translator`
- `ResolutionSelector`
- `SaveImage`
- `SkipLayerGuidanceDiTSimple`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `ZML_MultiTextInput3`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Int2String` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `StringToInt` —— 1/2 个有
- `StringToNumber` —— 1/2 个有
- `TextSwitchCase` —— 1/2 个有
- `ZML_AnyTypeSwitchFive` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 27 | - | 2 | 15% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 50% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 27，样本不足，未给区间，2 个样本，取值分散，一致性仅 15%
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
