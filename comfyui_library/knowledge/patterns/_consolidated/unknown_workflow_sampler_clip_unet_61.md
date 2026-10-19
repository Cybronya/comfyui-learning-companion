---
name: unknown_workflow_sampler_clip_unet_61
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.934
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1902172176840335361.json, 图片生成/文生图/1902293777606975490.json, 图片生成/文生图/1905507891238080513.json, 图片生成/文生图/1906558127117111297.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_61

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1902172176840335361.json、图片生成/文生图/1902293777606975490.json、图片生成/文生图/1905507891238080513.json、图片生成/文生图/1906558127117111297.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 3/4 个有
- `FluxGuidance` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `LoraLoader` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `ControlNetLoader` —— 1/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `InfiniteYouApply` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `TeaCache` —— 1/4 个有
- `UltimateSDUpscale` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1024 - 1440 | 3 | 84% |
| 高度 | 1920 | 1280 - 2560 | 3 | 73% |
| LoRA 模型强度 | 0.95 | - | 2 | 95% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 1024 - 1440，3 个样本，取值集中（一致性 84%）
- 高度 中位数 1920，观测区间 1280 - 2560，3 个样本
- LoRA 模型强度 中位数 0.95，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
