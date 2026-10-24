---
name: unknown_workflow_sampler_clip_unet_271
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9428
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/【潮玩盲盒】可爱卡通黏土风_1984515249296523265.json, 图片生成/文生图/中文直出---F.1-FLUX文生图工作流+LORA（一键运行）_1929761113691340801.json, 图片生成/文生图/去AI味！Flux_Krea文生图_1952185609727234050.json, 图片生成/文生图/沙雕动画都市背景_1933850253839749122.json, 图片生成/文生图/特密文生图工作流_1962372606101950465.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_271

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/【潮玩盲盒】可爱卡通黏土风_1984515249296523265.json、图片生成/文生图/中文直出---F.1-FLUX文生图工作流+LORA（一键运行）_1929761113691340801.json、图片生成/文生图/去AI味！Flux_Krea文生图_1952185609727234050.json、图片生成/文生图/沙雕动画都市背景_1933850253839749122.json、图片生成/文生图/特密文生图工作流_1962372606101950465.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
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
- `ImageUpscaleWithModel` —— 4/5 个有
- `UpscaleModelLoader` —— 4/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `RH_Translator` —— 3/5 个有
- `FluxGuidance` —— 1/5 个有
- `ImageScaleBy` —— 1/5 个有
- `JoinStrings` —— 1/5 个有
- `LoraLoader` —— 1/5 个有
- `ShowText` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1344 | 5 | 78% |
| 高度 | 1024 | 768 - 1536 | 5 | 74% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1344，5 个样本
- 高度 中位数 1024，观测区间 768 - 1536，5 个样本
