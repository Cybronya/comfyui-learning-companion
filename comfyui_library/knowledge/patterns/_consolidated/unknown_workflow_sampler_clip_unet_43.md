---
name: unknown_workflow_sampler_clip_unet_43
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.906833
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: PurgeVRAM, Lora Loader Stack (rgthree), Upscale Model Loader, CR Prompt Text, CR Text Concatenate]
members: [图片生成/文生图/1911385397333585922.json, 图片生成/文生图/1915296194967306242.json, 图片生成/文生图/1917149291704418305.json, 图片生成/文生图/1923215248826748929.json, 图片生成/文生图/1929761113691340801.json, 图片生成/文生图/1949732974748672001.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_43

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1911385397333585922.json、图片生成/文生图/1915296194967306242.json、图片生成/文生图/1917149291704418305.json、图片生成/文生图/1923215248826748929.json、图片生成/文生图/1929761113691340801.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Lora Loader Stack (rgthree)` —— 3/6 个有
- `LoraLoader` —— 3/6 个有
- `RH_Translator` —— 3/6 个有
- `ImageUpscaleWithModel` —— 2/6 个有
- `LayerUtility: PurgeVRAM` —— 2/6 个有
- `TeaCache` —— 2/6 个有
- `Upscale Model Loader` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `FluxGuidance` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `ShowText` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 600 - 1024 | 6 | 82% |
| 高度 | 1024 | 800 - 1536 | 6 | 76% |
| LoRA 模型强度 | 0.6 | 0.6 - 0.8 | 3 | 86% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 600 - 1024，6 个样本，取值集中（一致性 82%）
- 高度 中位数 1024，观测区间 800 - 1536，6 个样本
- LoRA 模型强度 中位数 0.6，观测区间 0.6 - 0.8，3 个样本，取值集中（一致性 86%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM、Lora Loader Stack (rgthree)、Upscale Model Loader、CR Prompt Text、CR Text Concatenate
