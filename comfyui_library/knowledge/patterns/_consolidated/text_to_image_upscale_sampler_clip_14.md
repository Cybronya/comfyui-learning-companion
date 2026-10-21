---
name: text_to_image_upscale_sampler_clip_14
type: Text To Image
frequency: 5
level: weak
coverage: 0.9432
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima预览版动漫模型-文生图 邪修版 RH工作流_2021210100874092545.json, 图片生成/文生图/Krea2 - 2K Ultra-clear details_2093616734757543938.json, 图片生成/文生图/Krea2 - 2K Ultra-clear details_2095547125550641153.json, 图片生成/文生图/Krea2 lora+高清放大基础工作流_2089602538793422849.json, 图片生成/文生图/QWEN-IMAGE商用快速流(YIHAN AIGC)_2027722964245942273.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_14

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Anima预览版动漫模型-文生图 邪修版 RH工作流_2021210100874092545.json、图片生成/文生图/Krea2 - 2K Ultra-clear details_2093616734757543938.json、图片生成/文生图/Krea2 - 2K Ultra-clear details_2095547125550641153.json、图片生成/文生图/Krea2 lora+高清放大基础工作流_2089602538793422849.json、图片生成/文生图/QWEN-IMAGE商用快速流(YIHAN AIGC)_2027722964245942273.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `CheckpointLoaderSimple` —— 1/5 个有
- `DuckHideNode` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `ImageScaleBy` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `TTResolutionSelector` —— 1/5 个有
- `TextEncodeQwenImageEditPlus` —— 1/5 个有
- `easy clearCacheAll` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 30 | 5 | 23% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 5 | 25% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 0.58 - 1 | 5 | 82% |
| 宽度 | 768 | 512 - 1080 | 5 | 69% |
| 高度 | 1024 | 512 - 1920 | 5 | 58% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 30，5 个样本，取值分散，一致性仅 23%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，5 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.58 - 1，5 个样本，取值集中（一致性 82%）
- 宽度 中位数 768，观测区间 512 - 1080，5 个样本
- 高度 中位数 1024，观测区间 512 - 1920，5 个样本
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
