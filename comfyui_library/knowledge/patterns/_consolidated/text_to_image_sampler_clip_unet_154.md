---
name: text_to_image_sampler_clip_unet_154
type: Text To Image
frequency: 4
level: moderate
coverage: 0.98875
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, RH_Translator, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/QWEN3反推提示+Z-image图生图_1995786213816676354.json, 图片生成/文生图/QWEN3反推提示词+Z-image图生图123_1999891271516815361.json, 图片生成/文生图/boogu_base 文生图_2068898981547171841.json, 图片生成/文生图/千问+Qwen3VL反推提示词 超级文生图工作流_1980137914665439234.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_154

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/QWEN3反推提示+Z-image图生图_1995786213816676354.json、图片生成/文生图/QWEN3反推提示词+Z-image图生图123_1999891271516815361.json、图片生成/文生图/boogu_base 文生图_2068898981547171841.json、图片生成/文生图/千问+Qwen3VL反推提示词 超级文生图工作流_1980137914665439234.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `RH_Translator`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL_Advanced` —— 3/4 个有
- `Int` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `TextInput_` —— 3/4 个有
- `easy textSwitch` —— 3/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `SeedVR2GGUF` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1536 | 1024 - 1536 | 4 | 84% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 25 | 10 - 40 | 4 | 40% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4.5 | 4 | 38% |
| 采样算法 | dpmpp_2m | - | 4 | 50% |
| 调度器 | sgm_uniform | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1536，观测区间 1024 - 1536，4 个样本，取值集中（一致性 84%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 10 - 40，4 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4.5，4 个样本，取值分散，一致性仅 38%
- 采样算法 最常用 dpmpp_2m，4 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
