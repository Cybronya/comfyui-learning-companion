---
name: unknown_workflow_sampler_clip_unet_338
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.926667
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Qwen-image最强反推洗图~洗文字，洗海报！无所不洗！_1954009993588690946.json, 图片生成/文生图/QWen-Image 表情包 解锁你的情绪新表达_1955541581090754561.json, 图片生成/文生图/Qwen-Image文生图+提示词优化器_1953302071052333057.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_338

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen-image最强反推洗图~洗文字，洗海报！无所不洗！_1954009993588690946.json、图片生成/文生图/QWen-Image 表情包 解锁你的情绪新表达_1955541581090754561.json、图片生成/文生图/Qwen-Image文生图+提示词优化器_1953302071052333057.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 2/3 个有
- `EmptySD3LatentImage` —— 2/3 个有
- `ImpactInt` —— 2/3 个有
- `RH_LLMAPI_NODE` —— 2/3 个有
- `StringReplace` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `TextInput_` —— 2/3 个有
- `easy anythingIndexSwitch` —— 2/3 个有
- `FluxKontextImageScale` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 4 | 2.5 - 4 | 3 | 80% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 2.5 - 4，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
