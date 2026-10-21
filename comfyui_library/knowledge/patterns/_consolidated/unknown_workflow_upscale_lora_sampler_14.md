---
name: unknown_workflow_upscale_lora_sampler_14
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7996
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, Image Remove Alpha JK, KSampler, Lora Loader Stack (rgthree), PlaySound|pysssss, PreviewImage, PrimitiveStringMultiline, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy cleanGpuUsed]
problems: []
missing: []
members: ["图片生成/文生图/Qwen Image 2.1 skills+for循环-文生图+放大2K,4K_2102658672664072194.json", "图片生成/文生图/Qwen Image 2.1 skills文生图+放大2K,4K_2102616610388406274.json", "图片生成/文生图/Qwen Image 2.1 skills文生图+放大2K,4K_2102657150928642049.json", "图片生成/文生图/Qwen Image 2.1 加速1分35秒出2K,4K_2103662823787286529.json", "图片生成/文生图/Qwen Image 2.1-mxlz- skills文生图+放大2K,4K_2102952303706857474.json"]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_14

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1 skills+for循环-文生图+放大2K,4K_2102658672664072194.json、图片生成/文生图/Qwen Image 2.1 skills文生图+放大2K,4K_2102616610388406274.json、图片生成/文生图/Qwen Image 2.1 skills文生图+放大2K,4K_2102657150928642049.json、图片生成/文生图/Qwen Image 2.1 加速1分35秒出2K,4K_2103662823787286529.json、图片生成/文生图/Qwen Image 2.1-mxlz- skills文生图+放大2K,4K_2102952303706857474.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Image Remove Alpha JK`
- `KSampler`
- `Lora Loader Stack (rgthree)`
- `PlaySound|pysssss`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageApplyLUT+` —— 4/5 个有
- `easy imageChooser` —— 4/5 个有
- `GetItemFromList` —— 1/5 个有
- `QwenImage21BlockCacheT8` —— 1/5 个有
- `QwenImage21SageAttentionT8` —— 1/5 个有
- `QwenImage21SpectrumT8` —— 1/5 个有
- `easy batchAnything` —— 1/5 个有
- `easy forLoopEnd` —— 1/5 个有
- `easy forLoopStart` —— 1/5 个有
- `easy lengthAnything` —— 1/5 个有
- `easy promptList` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |
| 采样步数 | 40 | 40 - 40 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 40 - 40，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
