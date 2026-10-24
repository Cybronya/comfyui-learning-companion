---
name: unknown_workflow_lora_sampler_clip_184
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.966
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/反推+洗图+图生图工作流_1895848802538618882.json, 图片生成/文生图/【AI由北】FLUX网红美女-工作流_1906689471180419073.json, 图片生成/文生图/文生图+LoRA_1912174132275150850.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_184

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/反推+洗图+图生图工作流_1895848802538618882.json、图片生成/文生图/【AI由北】FLUX网红美女-工作流_1906689471180419073.json、图片生成/文生图/文生图+LoRA_1912174132275150850.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 2/3 个有
- `FluxGuidance` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `StringFunction|pysssss` —— 2/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `LayerUtility: JoyCaption2ExtraOptions` —— 1/3 个有
- `LayerUtility: JoyCaption2Split` —— 1/3 个有
- `LayerUtility: LoadJoyCaption2Model` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy clearCacheAll` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 512 - 1080 | 3 | 70% |
| 高度 | 1432 | 512 - 1920 | 3 | 55% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 512 - 1080，3 个样本
- 高度 中位数 1432，观测区间 512 - 1920，3 个样本
