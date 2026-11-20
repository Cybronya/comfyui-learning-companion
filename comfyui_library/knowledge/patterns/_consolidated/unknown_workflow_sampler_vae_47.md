---
name: unknown_workflow_sampler_vae_47
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.53
common_nodes: [CFGNorm, CLIPLoader, GetNode, Image Comparer (rgthree), ImageStitch, KSampler (Efficient), LoadImage, ModelSamplingAuraFlow, PreviewImage, Prompts Everywhere, SaveImage, Seed Everywhere, SetNode, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一键运行：QWEN姿态提取换一切_1981202190071136258.json, 平台全量/nunchaku-qwen-image-edit-2509-lightningv2.0 多图修复_1972851463997333505.json, 平台全量/一键nunchaku-qwen-image-edit-2509-lightningv2 单图修复_1972846607475625985.json, 平台全量/一键运行：Qwen-edit-2509-fp8 单图修改 图像修复 图像换背景_1972486318280404994.json, 平台全量/一键运行：Qwen-edit-2509-fp8 多图编辑 图像修复 局部修复_1972481890114596866.json, 平台全量/一键运行：nunchaku-qwen-image-edit-2509 单图修复，修图，换背景_1972842122837708802.json, 平台全量/一键运行：nunchaku-qwen-image-edit-2509 多图编辑 图像修复 0 0 0_1972495847126724610.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_47

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/一键运行：QWEN姿态提取换一切_1981202190071136258.json、平台全量/nunchaku-qwen-image-edit-2509-lightningv2.0 多图修复_1972851463997333505.json、平台全量/一键nunchaku-qwen-image-edit-2509-lightningv2 单图修复_1972846607475625985.json、平台全量/一键运行：Qwen-edit-2509-fp8 单图修改 图像修复 图像换背景_1972486318280404994.json、平台全量/一键运行：Qwen-edit-2509-fp8 多图编辑 图像修复 局部修复_1972481890114596866.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：53%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageStitch`
- `KSampler (Efficient)`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `Prompts Everywhere`
- `SaveImage`
- `Seed Everywhere`
- `SetNode`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `NunchakuQwenImageDiTLoader` —— 5/7 个有
- `UNETLoader` —— 2/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `OpenposePreprocessor` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 7 | 55% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 7 | 55% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
