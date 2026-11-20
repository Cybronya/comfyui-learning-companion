---
name: unknown_workflow_lora_sampler_unet_321
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8775
common_nodes: [CLIPLoader, CR Text, CR Text Concatenate, Compositor3, CompositorConfig3, ConditioningZeroOut, GrowMask, KSampler (Efficient), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoader, PreviewImage, SaveImage, ShowText|pysssss, TextEncodeQwenImageEditPlusAdvance_lrzjason, UnetLoaderGGUF, VAELoader, easy imageRemBg]
problems: []
missing: []
members: [图片生成/图生图/Qwen-Edit2509万物迁移终极版_1983069141798154241.json, 平台全量/Qwen2509万物产品迁移融合_1983724138604994561.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_321

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit2509万物迁移终极版_1983069141798154241.json、平台全量/Qwen2509万物产品迁移融合_1983724138604994561.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `CR Text Concatenate`
- `Compositor3`
- `CompositorConfig3`
- `ConditioningZeroOut`
- `GrowMask`
- `KSampler (Efficient)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UnetLoaderGGUF`
- `VAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `NunchakuQwenImageDiTLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta57 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta57，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
