---
name: text_to_image_upscale_lora_sampler_13
type: Text To Image
frequency: 6
level: strong
coverage: 0.849
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageUpscaleWithModel, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/LEO-Qwen千问文生图+一键自动角色三视图工作流_2066384439432802305.json, 图片生成/文生图/Qwen-Image-基础版_2082365287453773826.json, 图片生成/文生图/Qwen千问文生图【含加速 LoRA 提速版】：原版 fp8_e4m3f + 低配 GGUF_2006697843498684418.json, 图片生成/文生图/千问Qwen-image-文生图_2057449926543626241.json, 图片生成/文生图/工作流千问篇1-Qwen千问文生图-国产大模型之光_2022215261247512578.json, 视频生成/文生视频/千问文生图【加速+放大】_2065018446563340289.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_13

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/LEO-Qwen千问文生图+一键自动角色三视图工作流_2066384439432802305.json、图片生成/文生图/Qwen-Image-基础版_2082365287453773826.json、图片生成/文生图/Qwen千问文生图【含加速 LoRA 提速版】：原版 fp8_e4m3f + 低配 GGUF_2006697843498684418.json、图片生成/文生图/千问Qwen-image-文生图_2057449926543626241.json、图片生成/文生图/工作流千问篇1-Qwen千问文生图-国产大模型之光_2022215261247512578.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
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
- `UnetLoaderGGUF` —— 4/6 个有
- `FluxResolutionNode` —— 3/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `FluxKontextImageScale` —— 1/6 个有
- `Node Collector (rgthree)` —— 1/6 个有
- `Seed (rgthree)` —— 1/6 个有
- `SmartImageConcat` —— 1/6 个有
- `TextEncodeQwenImageEditPlus` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1536 | 1024 - 1920 | 6 | 79% |
| 高度 | 1984 | 1080 - 2048 | 6 | 80% |
| 采样步数 | 4 | 4 - 8 | 6 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1536，观测区间 1024 - 1920，6 个样本
- 高度 中位数 1984，观测区间 1080 - 2048，6 个样本
- 采样步数 中位数 4，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（14/6 个样本）：Steps较低可能导致细节不足
