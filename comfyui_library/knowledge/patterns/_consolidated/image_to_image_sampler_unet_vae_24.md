---
name: image_to_image_sampler_unet_vae_24
type: Image To Image
frequency: 8
level: weak
coverage: 0.86525
common_nodes: [CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen2511_单图编辑_2013164817997107201.json, 图片生成/图生图/qwen_Edit_2511多图编辑工作流_2077225997874847745.json, 图片生成/图生图/qwen_edit_2511单图编辑_2077221456840314881.json, 图片生成/图生图/全量qwen edit 2512多图编辑工作流_2068333416139026434.json, 图片生成/图生图/千问图像编辑_产品材质更换工作流_2106390652362772481.json, 图片生成/图生图/单图编辑_2067956866138857473.json, 图片生成/图生图/小红书换装_2075185550822301697.json, 图片生成/图生图/角色转视角_2009539978879049729.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_24

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/qwen2511_单图编辑_2013164817997107201.json、图片生成/图生图/qwen_Edit_2511多图编辑工作流_2077225997874847745.json、图片生成/图生图/qwen_edit_2511单图编辑_2077221456840314881.json、图片生成/图生图/全量qwen edit 2512多图编辑工作流_2068333416139026434.json、图片生成/图生图/千问图像编辑_产品材质更换工作流_2106390652362772481.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `FluxKontextImageScale` —— 6/8 个有
- `PreviewImage` —— 6/8 个有
- `CFGNorm` —— 5/8 个有
- `Image Comparer (rgthree)` —— 3/8 个有
- `Text Multiline` —— 3/8 个有
- `DF_Image_scale_to_side` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `Image Save` —— 2/8 个有
- `ImageBatchMultiple+` —— 1/8 个有
- `ImageSharpen` —— 1/8 个有
- `Text Concatenate` —— 1/8 个有
- `Text Load Line From File` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 8 | 19% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 8 | 28% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，8 个样本，取值分散，一致性仅 19%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，8 个样本，取值分散，一致性仅 28%
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（7/8 个样本）：Steps较低可能导致细节不足
