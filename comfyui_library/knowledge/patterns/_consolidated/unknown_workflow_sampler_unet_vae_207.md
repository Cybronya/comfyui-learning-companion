---
name: unknown_workflow_sampler_unet_vae_207
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.881714
common_nodes: [BasicGuider, BasicScheduler, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/故事_1982707861027471361.json, 图片生成/文生图/文生图+LoRA_1932450301490425858.json, 图片生成/文生图/红线-文生图-LoRA_1937538449320906754.json, 图片生成/文生图/英文字体设计_1927964492725141505.json, 图片生成/文生图/英文字体设计_2084095503633043458.json, 图片生成/文生图/超好用室内文生图+放大集合_1963922300439547906.json, 平台全量/带着画笔去旅行_1838478160345153538.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_207

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/故事_1982707861027471361.json、图片生成/文生图/文生图+LoRA_1932450301490425858.json、图片生成/文生图/红线-文生图-LoRA_1937538449320906754.json、图片生成/文生图/英文字体设计_1927964492725141505.json、图片生成/文生图/英文字体设计_2084095503633043458.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
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
- `CLIPTextEncode` —— 6/7 个有
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `LoraLoader` —— 4/7 个有
- `UltimateSDUpscale` —— 4/7 个有
- `UpscaleModelLoader` —— 4/7 个有
- `FluxGuidance` —— 2/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `BatchPromptSchedule` —— 1/7 个有
- `CheckpointLoaderSimple` —— 1/7 个有
- `PreviewImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1280 | 7 | 84% |
| 高度 | 1024 | 720 - 1600 | 7 | 70% |
| LoRA 模型强度 | 0.7 | 0.6 - 0.8 | 4 | 86% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1280，7 个样本，取值集中（一致性 84%）
- 高度 中位数 1024，观测区间 720 - 1600，7 个样本
- LoRA 模型强度 中位数 0.7，观测区间 0.6 - 0.8，4 个样本，取值集中（一致性 86%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
