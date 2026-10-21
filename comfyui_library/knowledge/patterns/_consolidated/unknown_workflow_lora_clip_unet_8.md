---
name: unknown_workflow_lora_clip_unet_8
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6265
common_nodes: [CLIPTextEncode, CR Load LoRA, DualCLIPLoader, EmptyLatentImage, FluxGuidance, JjkShowText, JjkText, LoraLoader, PrimitiveInt, RH_Translator, SaveImage, UNETLoader, workflow>ace, workflow>采样]
problems: []
missing: [Label (rgthree), workflow>ace, CR Load LoRA, workflow>采样]
members: [图片生成/文生图/1980542326344957953.json, 图片生成/文生图/文生图批量一致性多姿势美女图_1995149863115534337.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet_8

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1980542326344957953.json、图片生成/文生图/文生图批量一致性多姿势美女图_1995149863115534337.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：63%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Load LoRA`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `JjkShowText`
- `JjkText`
- `LoraLoader`
- `PrimitiveInt`
- `RH_Translator`
- `SaveImage`
- `UNETLoader`
- `workflow>ace`
- `workflow>采样`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | - | 2 | 100% |
| 高度 | 1920 | - | 2 | 100% |
| LoRA 模型强度 | 0.8 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Label (rgthree)、workflow>ace、CR Load LoRA、workflow>采样
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
