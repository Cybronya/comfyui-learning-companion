---
name: unknown_workflow_controlnet_lora_sampler_19
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.783333
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetApplyAdvanced, ControlNetLoader, EmptySD3LatentImage, GetImageSize, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2512图生图精准控制版_2064527820356939777.json, 图片生成/图生图/Qwen-Image最强ControlNet图生图_1966787895946326018.json, 图片生成/文生图/Qwen-Image最强CN控制模型_1960378242681155586.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_19

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2512图生图精准控制版_2064527820356939777.json、图片生成/图生图/Qwen-Image最强ControlNet图生图_1966787895946326018.json、图片生成/文生图/Qwen-Image最强CN控制模型_1960378242681155586.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptySD3LatentImage`
- `GetImageSize`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `SetUnionControlNetType` —— 2/3 个有
- `Canny` —— 1/3 个有
- `ComfySwitchNode` —— 1/3 个有
- `PrimitiveBoolean` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `ResizeImageMaskNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 3 | 10% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 3 | 29% |
| 采样算法 | res_2s | - | 3 | 67% |
| 调度器 | bong_tangent | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，3 个样本，取值分散，一致性仅 10%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，3 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 res_2s，3 个样本，一致性 67%
- 调度器 最常用 bong_tangent，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
