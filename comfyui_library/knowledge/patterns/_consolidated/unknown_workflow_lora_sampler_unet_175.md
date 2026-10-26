---
name: unknown_workflow_lora_sampler_unet_175
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.80975
common_nodes: [BasicGuider, CLIPLoader, EmptyLatentImage, JsonExtractString, KSamplerSelect, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, StringFormat, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen-Image 2.1｜5倍加速 _ 角色三视图工作流_2105209871988781057.json, 图片生成/图生图/Qwen-Image-2.1-viggle-turbo-edit-auto-sigma_2104804428602765313.json, 图片生成/图生图/Qwen-Image-2.1-viggle-turbo-edit-auto-sigma_三图编辑6步快速出图_2105184881469911042.json, 图片生成/文生图/Qwen-Image-2.1-viggle-turbo-t2i-auto-sigma_2104764845521461250.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_175

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-Image 2.1｜5倍加速 _ 角色三视图工作流_2105209871988781057.json、图片生成/图生图/Qwen-Image-2.1-viggle-turbo-edit-auto-sigma_2104804428602765313.json、图片生成/图生图/Qwen-Image-2.1-viggle-turbo-edit-auto-sigma_三图编辑6步快速出图_2105184881469911042.json、图片生成/文生图/Qwen-Image-2.1-viggle-turbo-t2i-auto-sigma_2104764845521461250.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `EmptyLatentImage`
- `JsonExtractString`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringFormat`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `QwenImage21Cache` —— 3/4 个有
- `TextGenerate` —— 3/4 个有
- `BatchImagesNode` —— 2/4 个有
- `ComfySwitchNode` —— 2/4 个有
- `PreviewAny` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `PrimitiveBoolean` —— 2/4 个有
- `SeedNode` —— 2/4 个有
- `StringCompare` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `CR Model Input Switch` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `KSampler` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `StringToInt` —— 1/4 个有
- `TextGenerateLTX2Prompt` —— 1/4 个有
- `easy imageConcat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 40 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | normal | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
