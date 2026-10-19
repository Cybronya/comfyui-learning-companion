---
name: unknown_workflow_sampler_unet_vae_110
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.8315
common_nodes: [BatchImagesNode, CLIPLoader, ComfySwitchNode, EmptyLatentImage, JoinStrings, KSampler, LoadImage, PrimitiveBoolean, QwenImage21Cache, ResolutionSelector, SaveImage, ShowText|pysssss, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader, easy positive, 孤海注释]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, easy positive, 忽略多组孤海]
members: [图片生成/反推提示词/Qwen image 2.1 图片编辑工作流（官方高质量版）_2103413517125771266.json, 图片生成/图生图/2105932118147817473.json, 图片生成/图生图/2105934523547602945.json, 图片生成/图生图/千问2.1图片编辑测试工作流！_2107274754737664002.json, 图片生成/文生图/Qwen image 2.1 图片编辑工作流（官方高质量版）_2103413517125771266.json, 图片生成/文生图/千问2.1图片编辑测试工作流！_2106938314304610306.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_110

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/反推提示词/Qwen image 2.1 图片编辑工作流（官方高质量版）_2103413517125771266.json、图片生成/图生图/2105932118147817473.json、图片生成/图生图/2105934523547602945.json、图片生成/图生图/千问2.1图片编辑测试工作流！_2107274754737664002.json、图片生成/文生图/Qwen image 2.1 图片编辑工作流（官方高质量版）_2103413517125771266.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
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
- `ImageScaleToTotalPixels` —— 5/6 个有
- `忽略多组孤海` —— 5/6 个有
- `ImageConcatMulti` —— 2/6 个有
- `ModelPreviewOverrideKJ` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `EmptyImage` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 6 | 100% |
| 高度 | 1024 | 1024 - 1024 | 6 | 100% |
| 采样步数 | 25 | 25 - 25 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、easy positive、忽略多组孤海
