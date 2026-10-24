---
name: text_to_image_lora_sampler_clip_438
type: Text To Image
frequency: 4
level: strong
coverage: 0.757
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveBoolean, ResolutionSelector, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-trubo+Qwen-HDR-VAE-极致美学文生图工作流_2072939844057260033.json, 图片生成/文生图/Krea2-trubo+Qwen-HDR-VAE-极致美学文生图工作流_2073668554435678209.json, 图片生成/文生图/Krea2-trubo极致美学文生图工作流_2070143360244998145.json, 图片生成/文生图/Krea2经典省心工作流（旁路版）_2074515678991831042.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_438

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Krea2-trubo+Qwen-HDR-VAE-极致美学文生图工作流_2072939844057260033.json、图片生成/文生图/Krea2-trubo+Qwen-HDR-VAE-极致美学文生图工作流_2073668554435678209.json、图片生成/文生图/Krea2-trubo极致美学文生图工作流_2070143360244998145.json、图片生成/文生图/Krea2经典省心工作流（旁路版）_2074515678991831042.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveBoolean`
- `ResolutionSelector`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `ResizeImagesByLongerEdge` —— 1/4 个有
- `VRAM_Debug` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
