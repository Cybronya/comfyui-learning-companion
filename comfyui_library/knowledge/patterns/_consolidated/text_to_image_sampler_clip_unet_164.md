---
name: text_to_image_sampler_clip_unet_164
type: Text To Image
frequency: 4
level: weak
coverage: 0.86075
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, PreviewImage, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Ernie-image-turbo与Z-image-turbo对比工作流_2044632672093343745.json, 图片生成/文生图/Krea2-文生图+自动扩写提示词_2068202850336985089.json, 图片生成/文生图/Qwen-iamge2.1-文生图（自动提示词版）_2102004749242552322.json, 图片生成/文生图/Qwen-iamge2.1文生图自动提示词版｜描述自动补全优化｜懒人直出利器_2102271791212359682.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_164

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Ernie-image-turbo与Z-image-turbo对比工作流_2044632672093343745.json、图片生成/文生图/Krea2-文生图+自动扩写提示词_2068202850336985089.json、图片生成/文生图/Qwen-iamge2.1-文生图（自动提示词版）_2102004749242552322.json、图片生成/文生图/Qwen-iamge2.1文生图自动提示词版｜描述自动补全优化｜懒人直出利器_2102271791212359682.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `ConditioningZeroOut` —— 3/4 个有
- `QwenImage21Cache` —— 2/4 个有
- `ResolutionSelector` —— 2/4 个有
- `TextGenerateLTX2Prompt` —— 2/4 个有
- `AddLabel` —— 1/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `JDCN_StringToList` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `solarL_SaveImagesToZip` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 808 | 80 - 1024 | 4 | 47% |
| 高度 | 1152 | 80 - 1280 | 4 | 46% |
| 采样步数 | 8 | 4 - 25 | 4 | 28% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 4 | 19% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 808，观测区间 80 - 1024，4 个样本，取值分散，一致性仅 47%
- 高度 中位数 1152，观测区间 80 - 1280，4 个样本，取值分散，一致性仅 46%
- 采样步数 中位数 8，观测区间 4 - 25，4 个样本，取值分散，一致性仅 28%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，4 个样本，取值分散，一致性仅 19%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
