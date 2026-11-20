---
name: unknown_workflow_controlnet_sampler_clip_33
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.747333
common_nodes: [AIO_Preprocessor, Anything Everywhere, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, KSampler (Efficient), LayerFilter: HDREffects, LoadImage, ModelSamplingAuraFlow, PreviewImage, Prompts Everywhere, SaveImage, Seed Everywhere, SetUnionControlNetType, StringConstantMultiline, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/一键运行：标准 Qwen InstantX Union ControlNet 图像控制_1962344245782888449.json, 平台全量/一键运行：Nunchaku  InstantX Union ControlNet for Qwen_1962353291436998658.json, 平台全量/一键运行：nunchaku QWEN EDIT CN工作流 图像修改_1968857642133331969.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_33

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/一键运行：标准 Qwen InstantX Union ControlNet 图像控制_1962344245782888449.json、平台全量/一键运行：Nunchaku  InstantX Union ControlNet for Qwen_1962353291436998658.json、平台全量/一键运行：nunchaku QWEN EDIT CN工作流 图像修改_1968857642133331969.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `Anything Everywhere`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `KSampler (Efficient)`
- `LayerFilter: HDREffects`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `Prompts Everywhere`
- `SaveImage`
- `Seed Everywhere`
- `SetUnionControlNetType`
- `StringConstantMultiline`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `NunchakuQwenImageDiTLoader` —— 2/3 个有
- `ImageStitch` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `UNETLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.75 | 0.75 - 1 | 3 | 86% |
| 采样步数 | 20 | 8 - 30 | 3 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 3 | 53% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 0.5 - 1 | 3 | 72% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.75，观测区间 0.75 - 1，3 个样本，取值集中（一致性 86%）
- 采样步数 中位数 20，观测区间 8 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，3 个样本
