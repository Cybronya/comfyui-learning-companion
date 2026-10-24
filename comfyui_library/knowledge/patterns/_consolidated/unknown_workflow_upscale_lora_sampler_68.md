---
name: unknown_workflow_upscale_lora_sampler_68
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.908333
common_nodes: [Anything Everywhere3, BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Float, Int, KSamplerAdvanced, KSamplerSelect, LatentPixelScale, LoraLoader, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveImage, Text Multiline, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Alan测Z Image Turbo 满血版极速文生图ComfyUI工作流_2040617972292657154.json, 图片生成/文生图/Z Image Turbo 满血版极速文生图ComfyUI工作流_2040042157939105793.json, 图片生成/文生图/z image 文生图_1995307580987781122.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_68

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Alan测Z Image Turbo 满血版极速文生图ComfyUI工作流_2040617972292657154.json、图片生成/文生图/Z Image Turbo 满血版极速文生图ComfyUI工作流_2040042157939105793.json、图片生成/文生图/z image 文生图_1995307580987781122.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere3`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Float`
- `Int`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `LatentPixelScale`
- `LoraLoader`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `> Save Image` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 10 | 10 - 10 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | dpmpp_3m_sde | - | 3 | 100% |
| 重绘幅度 | ddim_uniform | - | 3 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 720 | 720 - 720 | 3 | 100% |
| 高度 | 1280 | 1280 - 1280 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_3m_sde，3 个样本，一致性 100%
- 重绘幅度 最常用 ddim_uniform，3 个样本，一致性 100%
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 720，观测区间 720 - 720，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 1280 - 1280，3 个样本，取值集中（一致性 100%）
