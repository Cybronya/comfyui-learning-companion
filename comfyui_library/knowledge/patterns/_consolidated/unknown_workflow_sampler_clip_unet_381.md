---
name: unknown_workflow_sampler_clip_unet_381
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.878
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, GetImageSize, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image二次采样反推洗图_2073307813459353602.json, 图片生成/文生图/Z-Image哈迪斯风格反推重绘_2073310291110223874.json, 图片生成/文生图/qwen_image_Qwen3VL_txt2img   文本到图像工作流_1981021439052615681.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_381

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-Image二次采样反推洗图_2073307813459353602.json、图片生成/文生图/Z-Image哈迪斯风格反推重绘_2073310291110223874.json、图片生成/文生图/qwen_image_Qwen3VL_txt2img   文本到图像工作流_1981021439052615681.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `GetImageSize`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 2/3 个有
- `LatentUpscaleBy` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `AILab_QwenVL` —— 1/3 个有
- `AILab_QwenVL_Advanced` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `UltimateSDUpscale` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 19 | - | 2 | 42% |
| Prompt 约束强度(CFG) | 4 | 1 - 8 | 3 | 34% |
| 采样算法 | 1 | - | 3 | 33% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 0.6 | - | 2 | 33% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 19，样本不足，未给区间，2 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 8，3 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 1，3 个样本，一致性 33%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 0.6，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
