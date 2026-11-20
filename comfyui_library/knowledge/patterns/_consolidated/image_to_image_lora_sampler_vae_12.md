---
name: image_to_image_lora_sampler_vae_12
type: Image To Image
frequency: 8
level: strong
coverage: 0.896875
common_nodes: [CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen2511_单图编辑_2013164817997107201.json, 图片生成/图生图/qwen_Edit_2511多图编辑工作流_2077225997874847745.json, 图片生成/图生图/▶千问Qwen漫画本子上色流2_2058936764278075393.json, 图片生成/图生图/提取电商图封面模板_2034665275026579457.json, 图片生成/图生图/角色转视角_2009539978879049729.json, 平台全量/▶千问Qwen漫画本子上色流1_2058940140168507393.json, 平台全量/▶千问Qwen漫画本子上色流3_2058944109188050945.json, 平台全量/千问Qwen漫画本子上色流(整合)_2027640239598084097.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_12

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/qwen2511_单图编辑_2013164817997107201.json、图片生成/图生图/qwen_Edit_2511多图编辑工作流_2077225997874847745.json、图片生成/图生图/▶千问Qwen漫画本子上色流2_2058936764278075393.json、图片生成/图生图/提取电商图封面模板_2034665275026579457.json、图片生成/图生图/角色转视角_2009539978879049729.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 7/8 个有
- `UNETLoader` —— 7/8 个有
- `Fast Groups Bypasser (rgthree)` —— 5/8 个有
- `ImageScaleToTotalPixels` —— 5/8 个有
- `easy cleanGpuUsed` —— 5/8 个有
- `ConditioningZeroOut` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `CLIPLoaderGGUF` —— 3/8 个有
- `Text Multiline` —— 3/8 个有
- `UnetLoaderGGUF` —— 3/8 个有
- `DF_Image_scale_to_side` —— 2/8 个有
- `Image Save` —— 2/8 个有
- `LoadImageListFromDir //Inspire` —— 2/8 个有
- `CheckpointLoaderSimple` —— 1/8 个有
- `FluxKontextImageScale` —— 1/8 个有
- `Text Concatenate` —— 1/8 个有
- `Text Load Line From File` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 8 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（10/8 个样本）：Steps较低可能导致细节不足
