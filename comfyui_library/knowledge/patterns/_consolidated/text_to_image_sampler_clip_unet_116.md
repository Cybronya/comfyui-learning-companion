---
name: text_to_image_sampler_clip_unet_116
type: Text To Image
frequency: 6
level: weak
coverage: 0.872167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/王炸 Z-image-trubo 极速洗图_1993949795630989314.json, 图片生成/图生图/百度ERNIE-imag-turbo-洗图工作流（反推提示词）_2044786223306252289.json, 图片生成/文生图/Qwen-iamge2.1-文生图（自动提示词版）_2102004749242552322.json, 图片生成/文生图/Qwen-iamge2.1文生图自动提示词版｜描述自动补全优化｜懒人直出利器_2102271791212359682.json, 图片生成/文生图/文生图参考生图2合1 二合一图像生成方案_2108618211246825474.json, 图片生成/文生图/文生图参考生图二合一改进版｜双模式图像生成工作流_2108383787649425409.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_116

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/王炸 Z-image-trubo 极速洗图_1993949795630989314.json、图片生成/图生图/百度ERNIE-imag-turbo-洗图工作流（反推提示词）_2044786223306252289.json、图片生成/文生图/Qwen-iamge2.1-文生图（自动提示词版）_2102004749242552322.json、图片生成/文生图/Qwen-iamge2.1文生图自动提示词版｜描述自动补全优化｜懒人直出利器_2102271791212359682.json、图片生成/文生图/文生图参考生图2合1 二合一图像生成方案_2108618211246825474.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `llama_cpp_instruct_adv` —— 5/6 个有
- `llama_cpp_model_loader` —— 5/6 个有
- `ConditioningZeroOut` —— 4/6 个有
- `LoadImage` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `QwenImage21Cache` —— 4/6 个有
- `ResolutionSelector` —— 4/6 个有
- `ShowText|pysssss` —— 4/6 个有
- `TextGenerateLTX2Prompt` —— 4/6 个有
- `JjkText` —— 3/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `solarL_SaveImagesToZip` —— 3/6 个有
- `孤海注释` —— 3/6 个有
- `BatchImagesNode` —— 2/6 个有
- `CR Prompt Text` —— 2/6 个有
- `SaveImageAdvanced` —— 2/6 个有
- `TextEncodeQwenImage21` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `Anything Everywhere3` —— 1/6 个有
- `ImageConcanate` —— 1/6 个有
- `RH_Captioner` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 400 | 80 - 1024 | 6 | 14% |
| 高度 | 552 | 80 - 1664 | 6 | 8% |
| 采样步数 | 7 | 4 - 25 | 6 | 22% |
| Prompt 约束强度(CFG) | 2.75 | 1 - 4.5 | 6 | 36% |
| 采样算法 | euler | - | 6 | 50% |
| 调度器 | simple | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 400，观测区间 80 - 1024，6 个样本，取值分散，一致性仅 14%
- 高度 中位数 552，观测区间 80 - 1664，6 个样本，取值分散，一致性仅 8%
- 采样步数 中位数 7，观测区间 4 - 25，6 个样本，取值分散，一致性仅 22%
- Prompt 约束强度(CFG) 中位数 2.75，观测区间 1 - 4.5，6 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，6 个样本，一致性 50%
- 调度器 最常用 simple，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（3/6 个样本）：Steps较低可能导致细节不足
