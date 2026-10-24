---
name: unknown_workflow_upscale_sampler_clip_34
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.86125
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, Image Comparer (rgthree), KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-imagebase蛋挞Lora+放大_2026169943431057410.json, 图片生成/文生图/ainmap3反推画风选择放大_2044263221657341953.json, 图片生成/文生图/bangdream_mygo_2046920939073445889.json, 数字人/数字人/文生图v1_2049795277200084993.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_34

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-imagebase蛋挞Lora+放大_2026169943431057410.json、图片生成/文生图/ainmap3反推画风选择放大_2044263221657341953.json、图片生成/文生图/bangdream_mygo_2046920939073445889.json、数字人/数字人/文生图v1_2049795277200084993.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `llama_cpp_instruct_adv` —— 3/4 个有
- `llama_cpp_model_loader` —— 3/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `llama_cpp_parameters` —— 2/4 个有
- `ImageScaleBy` —— 1/4 个有
- `LoraLoader` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `easy saveText` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 39 | 28 - 50 | 4 | 72% |
| Prompt 约束强度(CFG) | 5 | 2.5 - 5 | 4 | 75% |
| 采样算法 | res_multistep | - | 4 | 50% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 0.6 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 39，观测区间 28 - 50，4 个样本
- Prompt 约束强度(CFG) 中位数 5，观测区间 2.5 - 5，4 个样本
- 采样算法 最常用 res_multistep，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
