---
name: text_to_image_upscale_lora_sampler_16
type: Text To Image
frequency: 10
level: strong
coverage: 0.856
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageUpscaleWithModel, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-controlnet线稿上色【含加速lora】_2066817304670855169.json, 图片生成/图生图/Qwen-controlnet线稿上色【含加速lora】_2067059788407721986.json, 图片生成/图生图/Qwen千问controlnet【加速 LoRA 提速版】：原版 fp8_e4m3f+低配 GGUF_1986439176663035905.json, 图片生成/图生图/Qwen千问controlnet【加速 LoRA 提速版】：原版 fp8_e4m3f+低配 GGUF_2003016885039951873.json, 图片生成/图生图/千问控制_2011334569835896833.json, 图片生成/图生图/千问控制工作流_2005606054086012929.json, 图片生成/图生图/千问控制工作流_2011336744066621442.json, 图片生成/图生图/千问版contronet工作流_1988909676433641473.json, 图片生成/文生图/Qwen千问文生图【含加速 LoRA 提速版】：原版 fp8_e4m3f + 低配 GGUF_2006697843498684418.json, 图片生成/文生图/千问文生图ControlNet控制+加速+电影感_1981575575947091970.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_16

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwen-controlnet线稿上色【含加速lora】_2066817304670855169.json、图片生成/图生图/Qwen-controlnet线稿上色【含加速lora】_2067059788407721986.json、图片生成/图生图/Qwen千问controlnet【加速 LoRA 提速版】：原版 fp8_e4m3f+低配 GGUF_1986439176663035905.json、图片生成/图生图/Qwen千问controlnet【加速 LoRA 提速版】：原版 fp8_e4m3f+低配 GGUF_2003016885039951873.json、图片生成/图生图/千问控制_2011334569835896833.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGNorm`
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
- `AIO_Preprocessor` —— 9/10 个有
- `ControlNetApplyAdvanced` —— 9/10 个有
- `ControlNetLoader` —— 9/10 个有
- `ImageScaleToTotalPixels` —— 9/10 个有
- `LoadImage` —— 9/10 个有
- `PreviewImage` —— 9/10 个有
- `UnetLoaderGGUF` —— 7/10 个有
- `CLIPLoaderGGUF` —— 2/10 个有
- `Image Comparer (rgthree)` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1536 | 1024 - 1536 | 10 | 83% |
| 高度 | 1024 | 1024 - 1536 | 10 | 82% |
| 采样步数 | 8 | 4 - 12 | 10 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| ControlNet 权重 | 0.8 | 0.8 - 0.8 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1536，观测区间 1024 - 1536，10 个样本，取值集中（一致性 83%）
- 高度 中位数 1024，观测区间 1024 - 1536，10 个样本，取值集中（一致性 82%）
- 采样步数 中位数 8，观测区间 4 - 12，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.8，观测区间 0.8 - 0.8，9 个样本，取值集中（一致性 100%）
- 高发问题（7/10 个样本）：Steps较低可能导致细节不足
