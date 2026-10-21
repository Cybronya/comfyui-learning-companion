---
name: unknown_workflow_sampler_unet_vae_168
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8655
common_nodes: [BatchImagesNode, CLIPLoader, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/文生图_参考生图2合1（改）_2108160229987938306.json, 数字人/数字人/Qwen Image 2.1 图像编辑 Image Edit_2101822303028989953.json, 视频生成/图生视频/Qwen_image_2.1图片编辑_2104046916651798529.json, 视频生成/图生视频/换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2102960653840510977.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_168

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/文生图_参考生图2合1（改）_2108160229987938306.json、数字人/数字人/Qwen Image 2.1 图像编辑 Image Edit_2101822303028989953.json、视频生成/图生视频/Qwen_image_2.1图片编辑_2104046916651798529.json、视频生成/图生视频/换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2102960653840510977.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 3/4 个有
- `SaveImageAdvanced` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `EmptyImage` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `llama_cpp_instruct_adv` —— 1/4 个有
- `llama_cpp_model_loader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 37.5 | 20 - 50 | 4 | 62% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 4 | 0% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 37.5，观测区间 20 - 50，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，4 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
