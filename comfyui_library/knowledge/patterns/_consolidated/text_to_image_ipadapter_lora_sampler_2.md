---
name: text_to_image_ipadapter_lora_sampler_2
type: Text To Image
frequency: 3
level: strong
coverage: 0.966667
common_nodes: [CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, EmptyLatentImage, IPAdapterFaceID, IPAdapterNoise, IPAdapterUnifiedLoaderFaceID, KSampler, LoadImage, LoraLoader, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/IPA+放大_2066554789101662210.json, 平台全量/ai换脸工作流_2002258029166882817.json, 平台全量/换脸的IPAdapter_1979724374242660354.json]
source: knowledge_consolidation
---

# text_to_image_ipadapter_lora_sampler_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/IPA+放大_2066554789101662210.json、平台全量/ai换脸工作流_2002258029166882817.json、平台全量/换脸的IPAdapter_1979724374242660354.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `IPAdapterFaceID`
- `IPAdapterNoise`
- `IPAdapterUnifiedLoaderFaceID`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `IPAdapterInsightFaceLoader` —— 2/3 个有
- `AdjustBrightness` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `MZ_IPAdapterInsightFaceLoader` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `UltimateSDUpscale` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| LoRA 模型强度 | 1 | 0.35 - 1 | 3 | 61% |
| LoRA 文本强度 | 1 | 0.8 - 1 | 3 | 90% |
| 采样步数 | 25 | 25 - 35 | 3 | 83% |
| Prompt 约束强度(CFG) | 6.5 | 6.5 - 6.5 | 3 | 100% |
| 采样算法 | dpmpp_2m | - | 3 | 67% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 0.35 - 1，3 个样本
- LoRA 文本强度 中位数 1，观测区间 0.8 - 1，3 个样本，取值集中（一致性 90%）
- 采样步数 中位数 25，观测区间 25 - 35，3 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 6.5，观测区间 6.5 - 6.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 67%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
