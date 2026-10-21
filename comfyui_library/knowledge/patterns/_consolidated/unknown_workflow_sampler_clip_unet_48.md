---
name: unknown_workflow_sampler_clip_unet_48
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9077
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1905507891238080513.json, 图片生成/文生图/1906689471180419073.json, 图片生成/文生图/1907035068605292545.json, 图片生成/文生图/1907048220537544706.json, 图片生成/文生图/1909542088999116801.json, 图片生成/文生图/1910653440345997314.json, 图片生成/文生图/1932450301490425858.json, 图片生成/文生图/1937538449320906754.json, 图片生成/文生图/1963922300439547906.json, 图片生成/文生图/1972618798815698945.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_48

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/1905507891238080513.json、图片生成/文生图/1906689471180419073.json、图片生成/文生图/1907035068605292545.json、图片生成/文生图/1907048220537544706.json、图片生成/文生图/1909542088999116801.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 10 个 workflow 都包含：
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
- `LoraLoader` —— 5/10 个有
- `UltimateSDUpscale` —— 4/10 个有
- `UpscaleModelLoader` —— 4/10 个有
- `Image Comparer (rgthree)` —— 3/10 个有
- `LoraLoaderModelOnly` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `RH_Translator` —— 3/10 个有
- `CheckpointLoaderSimple` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `LoadImage` —— 2/10 个有
- `ShowText|pysssss` —— 2/10 个有
- `ConditioningZeroOut` —— 1/10 个有
- `JjkShowText` —— 1/10 个有
- `RH_Captioner` —— 1/10 个有
- `TeaCache` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | 0.8 - 1 | 5 | 89% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1052 | 512 - 1440 | 10 | 78% |
| 高度 | 1024 | 512 - 2560 | 10 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 1，5 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1052，观测区间 512 - 1440，10 个样本
- 高度 中位数 1024，观测区间 512 - 2560，10 个样本
