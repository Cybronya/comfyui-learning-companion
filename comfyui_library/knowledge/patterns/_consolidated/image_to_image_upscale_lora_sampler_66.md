---
name: image_to_image_upscale_lora_sampler_66
type: Image To Image
frequency: 3
level: strong
coverage: 0.850333
common_nodes: [BNK_CLIPTextEncodeAdvanced, BasicGuider, BasicScheduler, CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, DualCLIPLoader, Florence2ModelLoader, Florence2Run, Image Comparer (rgthree), ImageResizeKJ, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/图生图低重绘 源歌_1937703020937547778.json, 图片生成/图生图/高清细节修复 源歌_1931581670690848770.json, 图片生成/图生图/高清细节修复 源歌_2027682421029736450.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_66

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/图生图低重绘 源歌_1937703020937547778.json、图片生成/图生图/高清细节修复 源歌_1931581670690848770.json、图片生成/图生图/高清细节修复 源歌_2027682421029736450.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `BNK_CLIPTextEncodeAdvanced`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Florence2ModelLoader`
- `Florence2Run`
- `Image Comparer (rgthree)`
- `ImageResizeKJ`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniCPM_VQA` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `StringFunction|pysssss` —— 2/3 个有
- `easy getNode` —— 2/3 个有
- `easy setNode` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 0.31 | 0.31 - 0.31 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 0.31，观测区间 0.31 - 0.31，3 个样本，取值集中（一致性 100%）
