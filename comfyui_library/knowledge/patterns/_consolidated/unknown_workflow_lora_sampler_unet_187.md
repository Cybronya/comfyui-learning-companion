---
name: unknown_workflow_lora_sampler_unet_187
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.905
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen_edit_2509童装上身工作流_2010558260528553985.json, 图片生成/图生图/【阡陌】 Qwen-Imag-eEdit 图像编辑解决偏移问题_1969954034549485570.json, 图片生成/图生图/千问edit一致性编辑（小志jason开源）_1968291733631053826.json, 图片生成/图生图/单图套装 _ 更换服装-qwen_image_edit_2511_2099760789157670914.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_187

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/qwen_edit_2509童装上身工作流_2010558260528553985.json、图片生成/图生图/【阡陌】 Qwen-Imag-eEdit 图像编辑解决偏移问题_1969954034549485570.json、图片生成/图生图/千问edit一致性编辑（小志jason开源）_1968291733631053826.json、图片生成/图生图/单图套装 _ 更换服装-qwen_image_edit_2511_2099760789157670914.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 3/4 个有
- `ConditioningZeroOut` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `TextEncodeQwenImageEdit_lrzjason` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `Easy_QwenEdit2509` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `TextEncodeQwenImageEditPlusPro_lrzjason` —— 1/4 个有
- `TextInputNode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 20 | 4 | 27% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 4 | 53% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 20，4 个样本，取值分散，一致性仅 27%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
