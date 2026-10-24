---
name: unknown_workflow_lora_sampler_unet_31
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.903786
common_nodes: [CLIPLoader, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, Text Multiline, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2511 角色卡制作（多视图 一次生四张）_2084585873563283457.json, 图片生成/图生图/qw2511多视角生成_2090289452240424962.json, 图片生成/图生图/千问2511图像编辑--去除水印高清修复_2084592160590098433.json, 图片生成/图生图/千问2511图像编辑--去除水印高清修复_2085683389117583362.json, 图片生成/图生图/千问2511图像编辑--去除水印高清修复_2086644313802498050.json, 图片生成/图生图/千问2511图像编辑--去除水印高清修复_2090269031159918593.json, 图片生成/图生图/千问2511图像编辑--自定义宽高_2020380197228388353.json, 图片生成/图生图/千问2511图像编辑通用版_2084595796892282882.json, 图片生成/图生图/千问2511图像编辑通用版_2087122490438012930.json, 图片生成/图生图/千问三图编辑工作流_2028325946230575105.json, 图片生成/图生图/千问单图编辑工作流_2088595857103998978.json, 图片生成/图生图/图像编辑，换背景工作流_2096106081322885122.json, 图片生成/图生图/图像编辑，换背景工作流_2097141363073703937.json, 图片生成/图生图/图像编辑，换背景工作流_2097237375155007489.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_31

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Qwen2511 角色卡制作（多视图 一次生四张）_2084585873563283457.json、图片生成/图生图/qw2511多视角生成_2090289452240424962.json、图片生成/图生图/千问2511图像编辑--去除水印高清修复_2084592160590098433.json、图片生成/图生图/千问2511图像编辑--去除水印高清修复_2085683389117583362.json、图片生成/图生图/千问2511图像编辑--去除水印高清修复_2086644313802498050.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `Text Multiline`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 13/14 个有
- `CR Text Concatenate` —— 13/14 个有
- `FluxKontextImageScale` —— 12/14 个有
- `LayerUtility: ImageReel` —— 12/14 个有
- `LayerUtility: ImageReelComposit` —— 12/14 个有
- `AILab_QwenVL` —— 11/14 个有
- `EmptyLatentImage` —— 11/14 个有
- `QWEN_TextDisplay` —— 11/14 个有
- `PreviewImage` —— 2/14 个有
- `easy imageScaleDownToSize` —— 2/14 个有
- `ImageMergeNode` —— 1/14 个有
- `MuyeTextEditOutput` —— 1/14 个有
- `QwenImageIntegratedKSampler` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 1280 - 1536 | 11 | 94% |
| 高度 | 1280 | 1024 - 1280 | 11 | 94% |
| 采样步数 | 8 | 8 - 8 | 13 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 93% |
| 调度器 | simple | - | 14 | 93% |
| 重绘幅度 | 1 | 1 - 6.55328e+14 | 14 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1280，观测区间 1280 - 1536，11 个样本，取值集中（一致性 94%）
- 高度 中位数 1280，观测区间 1024 - 1280，11 个样本，取值集中（一致性 94%）
- 采样步数 中位数 8，观测区间 8 - 8，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 93%
- 调度器 最常用 simple，14 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 6.55328e+14，14 个样本，取值分散，一致性仅 0%
- 风险：重绘幅度 观测到 6.55328e+14，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 高发问题（20/14 个样本）：Steps较低可能导致细节不足
