---
name: unknown_workflow_sampler_clip_unet_53
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8938
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, KSamplerSelect, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [SDXLEmptyLatentSizePicker+, ttN imageREMBG]
members: [图片生成/文生图/1937517741597179906.json, 图片生成/文生图/1946106579613609985.json, 图片生成/文生图/1953439745546309634.json, 图片生成/文生图/Flux稳定生成文字_1819769505672531969.json, 图片生成/文生图/Flux稳定生成文字_1824318987025952770.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_53

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1937517741597179906.json、图片生成/文生图/1946106579613609985.json、图片生成/文生图/1953439745546309634.json、图片生成/文生图/Flux稳定生成文字_1819769505672531969.json、图片生成/文生图/Flux稳定生成文字_1824318987025952770.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSamplerSelect`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 3/5 个有
- `CR SDXL Aspect Ratio` —— 2/5 个有
- `DisplayText` —— 2/5 个有
- `LoraLoader` —— 2/5 个有
- `SDXLEmptyLatentSizePicker+` —— 2/5 个有
- `TextConcat` —— 2/5 个有
- `Textbox` —— 2/5 个有
- `RandomPrompt` —— 1/5 个有
- `ttN imageREMBG` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1024 | 3 | 72% |
| 高度 | 512 | 1 - 1024 | 5 | 11% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1024，3 个样本
- 高度 中位数 512，观测区间 1 - 1024，5 个样本，取值分散，一致性仅 11%
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：SDXLEmptyLatentSizePicker+、ttN imageREMBG
