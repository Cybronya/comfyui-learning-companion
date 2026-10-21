---
name: unknown_workflow_lora_sampler_clip_88
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.73675
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2512 风格化 二次元_2006545169251831809.json, 图片生成/文生图/Qwen-Image-2512自动提示词优化版工作流_2006331950679724033.json, 图片生成/文生图/千文2512 风格化-高清_2006552224855494658.json, 数字人/数字人/文生图v1_2049795277200084993.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_88

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2512 风格化 二次元_2006545169251831809.json、图片生成/文生图/Qwen-Image-2512自动提示词优化版工作流_2006331950679724033.json、图片生成/文生图/千文2512 风格化-高清_2006552224855494658.json、数字人/数字人/文生图v1_2049795277200084993.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 3/4 个有
- `CFGNorm` —— 3/4 个有
- `ImpactSwitch` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `TextBox` —— 3/4 个有
- `EmptySD3LatentImage` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `QwenImageLatentAspectRatio` —— 2/4 个有
- `SeedVR2LoadDiTModel` —— 2/4 个有
- `SeedVR2LoadVAEModel` —— 2/4 个有
- `SeedVR2VideoUpscaler` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `llama_cpp_instruct_adv` —— 1/4 个有
- `llama_cpp_model_loader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 50 | 4 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 4 | 53% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 50，4 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
