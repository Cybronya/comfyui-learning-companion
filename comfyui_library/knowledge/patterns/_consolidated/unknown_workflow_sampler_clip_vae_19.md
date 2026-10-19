---
name: unknown_workflow_sampler_clip_vae_19
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.88375
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode]
problems: []
missing: [Lora Loader Stack (rgthree)]
members: [图片生成/文生图/1954823552040091649.json, 图片生成/文生图/1970368325295480834.json, 图片生成/文生图/Flux Schnell模型4步快速生图工作流_1896880774707093505.json, 图片生成/文生图/Flux文生图快速出图版_1896542920525406210.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_19

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1954823552040091649.json、图片生成/文生图/1970368325295480834.json、图片生成/文生图/Flux Schnell模型4步快速生图工作流_1896880774707093505.json、图片生成/文生图/Flux文生图快速出图版_1896542920525406210.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `VAELoader` —— 3/4 个有
- `CFGZeroStar` —— 2/4 个有
- `CLIPTextEncodeFlux` —— 2/4 个有
- `KSamplerAdvanced` —— 2/4 个有
- `Lora Loader Stack (rgthree)` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `StringConstantMultiline` —— 2/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `TeaCache` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1052 | 1024 - 1080 | 4 | 97% |
| 高度 | 1728 | 1024 - 1920 | 4 | 77% |
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 31 | - | 2 | 100% |
| 采样算法 | 2 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | normal | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1052，观测区间 1024 - 1080，4 个样本，取值集中（一致性 97%）
- 高度 中位数 1728，观测区间 1024 - 1920，4 个样本
- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 31，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 normal，2 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 31，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：Lora Loader Stack (rgthree)
