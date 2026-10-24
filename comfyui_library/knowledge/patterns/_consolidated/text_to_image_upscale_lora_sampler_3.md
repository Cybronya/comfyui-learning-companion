---
name: text_to_image_upscale_lora_sampler_3
type: Text To Image
frequency: 20
level: moderate
coverage: 0.91475
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageUpscaleWithModel, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen千问文生图【加速+放大】image_fp8_e4m3f + 低配 GGUF_2060253510142349313.json, 图片生成/文生图/Qwen千问文生图【含加速 LoRA 提速版】：原版 fp8_e4m3f + 低配 GGUF_1986395833375617026.json, 图片生成/文生图/Qwen千问文生图【含加速 LoRA 提速版】：原版 fp8_e4m3f + 低配 GGUF_2006697843498684418.json, 图片生成/文生图/Z-image-turbo极速文生图（内置身材调节Lora）_2101265914195955713.json, 图片生成/文生图/Z-image超极速文生图（内置巨乳身材调节Lora）_2047308071554256898.json, 图片生成/文生图/krea2_turbo文生图+Lora+四倍高清放大_2080125976993947650.json, 图片生成/文生图/千问-文生图-高配精细_2097549428528869378.json, 图片生成/文生图/千问Qwen-image-文生图_2057449926543626241.json, 图片生成/文生图/千问优质生图快速工作流_1988895729412354050.json, 图片生成/文生图/千问文生图 高质量 高清晰_2097963267984543745.json, 图片生成/文生图/千问文生图-电商专用_2066788213078978561.json, 图片生成/文生图/千问文生图-电商专用_2108042168052043777.json, 图片生成/文生图/千问文生图-电商专用_2112373154172719105.json, 图片生成/文生图/千问文生图_高质量_高清晰_2098219987013033986.json, 图片生成/文生图/千问文生图基础款_1985377282284003329.json, 图片生成/文生图/千问文生图电商产品_2090229875432050689.json, 图片生成/文生图/千问超写实文生图（AI仿真人漫剧资产制作）_2021440026743148546.json, 图片生成/文生图/千问（qwen2512最新版）文生图（加速+电影感）_1978855905909444610.json, 图片生成/文生图/工作流千问篇1-Qwen千问文生图-国产大模型之光_2022215261247512578.json, 视频生成/文生视频/千问文生图【加速+放大】_2065018446563340289.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_3

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/文生图/Qwen千问文生图【加速+放大】image_fp8_e4m3f + 低配 GGUF_2060253510142349313.json、图片生成/文生图/Qwen千问文生图【含加速 LoRA 提速版】：原版 fp8_e4m3f + 低配 GGUF_1986395833375617026.json、图片生成/文生图/Qwen千问文生图【含加速 LoRA 提速版】：原版 fp8_e4m3f + 低配 GGUF_2006697843498684418.json、图片生成/文生图/Z-image-turbo极速文生图（内置身材调节Lora）_2101265914195955713.json、图片生成/文生图/Z-image超极速文生图（内置巨乳身材调节Lora）_2047308071554256898.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 17/20 个有
- `Image Comparer (rgthree)` —— 7/20 个有
- `UnetLoaderGGUF` —— 6/20 个有
- `FluxResolutionNode` —— 5/20 个有
- `PreviewImage` —— 5/20 个有
- `Seed (rgthree)` —— 2/20 个有
- `Int` —— 1/20 个有
- `MuyeTextEditOutput` —— 1/20 个有
- `QwenImageLatentAspectRatio` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1536 | 896 - 2304 | 20 | 77% |
| 高度 | 1776 | 904 - 2048 | 20 | 73% |
| 采样步数 | 6 | 4 - 11 | 20 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.5 | 20 | 89% |
| 采样算法 | euler | - | 20 | 100% |
| 调度器 | simple | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1536，观测区间 896 - 2304，20 个样本
- 高度 中位数 1776，观测区间 904 - 2048，20 个样本
- 采样步数 中位数 6，观测区间 4 - 11，20 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.5，20 个样本，取值集中（一致性 89%）
- 采样算法 最常用 euler，20 个样本，一致性 100%
- 调度器 最常用 simple，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（25/20 个样本）：Steps较低可能导致细节不足
