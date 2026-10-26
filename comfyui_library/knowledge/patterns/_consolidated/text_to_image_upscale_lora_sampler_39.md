---
name: text_to_image_upscale_lora_sampler_39
type: Text To Image
frequency: 7
level: strong
coverage: 0.833714
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageUpscaleWithModel, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/LEO-Qwen千问文生图+一键自动角色三视图工作流_2066384439432802305.json, 图片生成/文生图/Qwen-Image-基础版_2082365287453773826.json, 图片生成/文生图/Qwen千问文生图【加速+放大】image_fp8_e4m3f + 低配 GGUF_2060253510142349313.json, 图片生成/文生图/Qwen千问文生图【含加速 LoRA 提速版】：原版 fp8_e4m3f + 低配 GGUF_1986395833375617026.json, 图片生成/文生图/千问Qwen-image-文生图_2057449926543626241.json, 图片生成/文生图/工作流千问篇1-Qwen千问文生图-国产大模型之光_2022215261247512578.json, 视频生成/文生视频/千问文生图【加速+放大】_2065018446563340289.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_39

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/LEO-Qwen千问文生图+一键自动角色三视图工作流_2066384439432802305.json、图片生成/文生图/Qwen-Image-基础版_2082365287453773826.json、图片生成/文生图/Qwen千问文生图【加速+放大】image_fp8_e4m3f + 低配 GGUF_2060253510142349313.json、图片生成/文生图/Qwen千问文生图【含加速 LoRA 提速版】：原版 fp8_e4m3f + 低配 GGUF_1986395833375617026.json、图片生成/文生图/千问Qwen-image-文生图_2057449926543626241.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
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
- `FluxResolutionNode` —— 5/7 个有
- `Image Comparer (rgthree)` —— 5/7 个有
- `UnetLoaderGGUF` —— 5/7 个有
- `Seed (rgthree)` —— 2/7 个有
- `FluxKontextImageScale` —— 1/7 个有
- `Node Collector (rgthree)` —— 1/7 个有
- `SmartImageConcat` —— 1/7 个有
- `TextEncodeQwenImageEditPlus` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1536 | 1080 - 1920 | 7 | 85% |
| 高度 | 2048 | 1080 - 2048 | 7 | 82% |
| 采样步数 | 4 | 4 - 8 | 7 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1536，观测区间 1080 - 1920，7 个样本，取值集中（一致性 85%）
- 高度 中位数 2048，观测区间 1080 - 2048，7 个样本，取值集中（一致性 82%）
- 采样步数 中位数 4，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（16/7 个样本）：Steps较低可能导致细节不足
