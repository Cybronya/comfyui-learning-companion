---
name: unknown_workflow_sampler_unet_vae_119
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.85375
common_nodes: [BatchImagesNode, CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, PrimitiveBoolean, QwenImage21Cache, ResolutionSelector, SaveImage, ShowText|pysssss, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader, easy positive]
problems: []
missing: []
members: [图片生成/反推提示词/Qwen image 2.1 图片编辑工作流（官方高质量版）_2103413517125771266.json, 图片生成/图生图/1-Aiden-Qwen2.1图片编辑测试工作流！_2103123040820350977.json, 图片生成/图生图/Qwen Image 2.1 图片编辑工作流（官流） 2609_2105934523547602945.json, 图片生成/图生图/Qwen Image 2.1漫转真工作流2609_2105932118147817473.json, 图片生成/图生图/Qwen image 2.1漫转真工作流（AIGC特异点）_2104062048404590594.json, 图片生成/图生图/千问2.1图片编辑测试工作流！_2107274754737664002.json, 图片生成/图生图/智能修图丨Qwen Image 2.1丨指令增强·多图编辑_2113116700873940993.json, 图片生成/文生图/千问2.1图片编辑测试工作流！_2106938314304610306.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_119

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/反推提示词/Qwen image 2.1 图片编辑工作流（官方高质量版）_2103413517125771266.json、图片生成/图生图/1-Aiden-Qwen2.1图片编辑测试工作流！_2103123040820350977.json、图片生成/图生图/Qwen Image 2.1 图片编辑工作流（官流） 2609_2105934523547602945.json、图片生成/图生图/Qwen Image 2.1漫转真工作流2609_2105932118147817473.json、图片生成/图生图/Qwen image 2.1漫转真工作流（AIGC特异点）_2104062048404590594.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 8 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PrimitiveBoolean`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `ShowText|pysssss`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `JoinStrings` —— 7/8 个有
- `孤海注释` —— 7/8 个有
- `ImageScaleToTotalPixels` —— 6/8 个有
- `忽略多组孤海` —— 5/8 个有
- `ImageConcatMulti` —— 3/8 个有
- `ModelPreviewOverrideKJ` —— 3/8 个有
- `PreviewImage` —— 3/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `EmptyImage` —— 1/8 个有
- `JsonExtractString` —— 1/8 个有
- `RegexMatch` —— 1/8 个有
- `StringConcatenate` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 896 - 1024 | 8 | 96% |
| 高度 | 1024 | 1024 - 1184 | 8 | 95% |
| 采样步数 | 25 | 25 - 25 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 896 - 1024，8 个样本，取值集中（一致性 96%）
- 高度 中位数 1024，观测区间 1024 - 1184，8 个样本，取值集中（一致性 95%）
- 采样步数 中位数 25，观测区间 25 - 25，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
