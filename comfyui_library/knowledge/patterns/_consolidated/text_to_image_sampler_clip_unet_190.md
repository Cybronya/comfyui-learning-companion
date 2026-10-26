---
name: text_to_image_sampler_clip_unet_190
type: Text To Image
frequency: 3
level: moderate
coverage: 0.985
common_nodes: [AILab_QwenVL_Advanced, CLIPLoader, CLIPTextEncode, EmptyLatentImage, Int, KSampler, LoadImage, RH_Translator, SaveImage, TextInput_, UNETLoader, VAEDecode, VAELoader, easy textSwitch]
problems: []
missing: []
members: [图片生成/文生图/QWEN3反推提示+Z-image图生图_1995786213816676354.json, 图片生成/文生图/QWEN3反推提示词+Z-image图生图123_1999891271516815361.json, 图片生成/文生图/千问+Qwen3VL反推提示词 超级文生图工作流_1980137914665439234.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_190

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/QWEN3反推提示+Z-image图生图_1995786213816676354.json、图片生成/文生图/QWEN3反推提示词+Z-image图生图123_1999891271516815361.json、图片生成/文生图/千问+Qwen3VL反推提示词 超级文生图工作流_1980137914665439234.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `AILab_QwenVL_Advanced`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Int`
- `KSampler`
- `LoadImage`
- `RH_Translator`
- `SaveImage`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy textSwitch`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `SeedVR2GGUF` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1536 | 1536 - 1536 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| 采样步数 | 10 | 10 - 40 | 3 | 29% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 3 | 24% |
| 采样算法 | dpmpp_2m | - | 3 | 67% |
| 调度器 | sgm_uniform | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1536，观测区间 1536 - 1536，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 10 - 40，3 个样本，取值分散，一致性仅 29%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，3 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 67%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
