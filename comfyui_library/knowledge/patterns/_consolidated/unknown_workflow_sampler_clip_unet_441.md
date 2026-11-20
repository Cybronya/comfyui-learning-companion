---
name: unknown_workflow_sampler_clip_unet_441
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.712
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, PrimitiveStringMultiline, QWEN_TextProcess, RH_Translator, ResolutionSelector, SaveImage, SkipLayerGuidanceDiTSimple, UNETLoader, VAEDecode, VAELoader, ZML_MultiTextInput3, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MOSS-Image _ 8步DMD _ 批量生图_2114233647191650306.json, 图片生成/文生图/MOSS-Image｜SFT 50步高质量文生图·新手入门版_2114188712623034369.json, 视频生成/文生视频/MOSS-Image_8步DMD_批量生图_2114890353022169089.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_441

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/MOSS-Image _ 8步DMD _ 批量生图_2114233647191650306.json、图片生成/文生图/MOSS-Image｜SFT 50步高质量文生图·新手入门版_2114188712623034369.json、视频生成/文生视频/MOSS-Image_8步DMD_批量生图_2114890353022169089.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 3 个 workflow 都包含：
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
- `Int2String` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `StringToInt` —— 2/3 个有
- `StringToNumber` —— 2/3 个有
- `TextSwitchCase` —— 2/3 个有
- `ZML_AnyTypeSwitchFive` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 50 | 3 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 3 | 43% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 50，3 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，3 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
