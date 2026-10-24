---
name: unknown_workflow_lora_sampler_clip_130
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8505
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen千问反推生图8步lora加速_1954719425863794689.json, 图片生成/图生图/Qwen多图编辑_1960167987355529217.json, 图片生成/图生图/qwen-image-edit 千问双图编辑_1958439990143434754.json, 图片生成/图生图/qwen-image-edit 千问多图像编辑高清修复_1958171523389538305.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_130

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen千问反推生图8步lora加速_1954719425863794689.json、图片生成/图生图/Qwen多图编辑_1960167987355529217.json、图片生成/图生图/qwen-image-edit 千问双图编辑_1958439990143434754.json、图片生成/图生图/qwen-image-edit 千问多图像编辑高清修复_1958171523389538305.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 3/4 个有
- `TextEncodeQwenImageEdit` —— 3/4 个有
- `easy imageRemBg` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `ImageScaleToMegapixels` —— 2/4 个有
- `Int` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `SeedVR2` —— 2/4 个有
- `SeedVR2BlockSwap` —— 2/4 个有
- `ImageConcanate` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 4 | 26% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，4 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
