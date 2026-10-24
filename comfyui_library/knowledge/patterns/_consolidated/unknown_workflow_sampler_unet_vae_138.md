---
name: unknown_workflow_sampler_unet_vae_138
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.843
common_nodes: [BatchImagesNode, CLIPLoader, ComfySwitchNode, EmptyLatentImage, JoinStrings, KSampler, LoadImage, PrimitiveBoolean, QwenImage21Cache, ResolutionSelector, SaveImage, ShowText|pysssss, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader, easy positive, 孤海注释]
problems: []
missing: []
members: [图片生成/反推提示词/Qwen image 2.1 图片编辑工作流（官方高质量版）_2103413517125771266.json, 图片生成/图生图/1-Aiden-Qwen2.1图片编辑测试工作流！_2103123040820350977.json, 图片生成/图生图/Qwen Image 2.1 图片编辑工作流（官流） 2609_2105934523547602945.json, 图片生成/图生图/Qwen Image 2.1漫转真工作流2609_2105932118147817473.json, 图片生成/图生图/Qwen image 2.1漫转真工作流（AIGC特异点）_2104062048404590594.json, 图片生成/图生图/千问2.1图片编辑测试工作流！_2107274754737664002.json, 图片生成/文生图/千问2.1图片编辑测试工作流！_2106938314304610306.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_138

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/Qwen image 2.1 图片编辑工作流（官方高质量版）_2103413517125771266.json、图片生成/图生图/1-Aiden-Qwen2.1图片编辑测试工作流！_2103123040820350977.json、图片生成/图生图/Qwen Image 2.1 图片编辑工作流（官流） 2609_2105934523547602945.json、图片生成/图生图/Qwen Image 2.1漫转真工作流2609_2105932118147817473.json、图片生成/图生图/Qwen image 2.1漫转真工作流（AIGC特异点）_2104062048404590594.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `JoinStrings`
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 5/7 个有
- `忽略多组孤海` —— 5/7 个有
- `ImageConcatMulti` —— 3/7 个有
- `ModelPreviewOverrideKJ` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `EmptyImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 7 | 100% |
| 高度 | 1024 | 1024 - 1024 | 7 | 100% |
| 采样步数 | 25 | 25 - 25 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
