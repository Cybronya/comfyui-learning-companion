---
name: text_to_image_sampler_clip_unet_185
type: Text To Image
frequency: 3
level: moderate
coverage: 0.937333
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/2031340892564492289.json, 图片生成/文生图/Flux.1-Krea-Dev文生图-无AI味逼真质感_1951288817326215170.json, 图片生成/文生图/krea-文生图-Moebius (Jean Giraud)风格美洲虎捕猎鳄鱼_1962669092442386433.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_185

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/2031340892564492289.json、图片生成/文生图/Flux.1-Krea-Dev文生图-无AI味逼真质感_1951288817326215170.json、图片生成/文生图/krea-文生图-Moebius (Jean Giraud)风格美洲虎捕猎鳄鱼_1962669092442386433.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `MultiLinePromptIndex` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `RH_LLMAPI_Pro_Node` —— 1/3 个有
- `RH_Translator` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 3 | 36% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 1024 - 1920 | 3 | 68% |
| 高度 | 1280 | 1080 - 1536 | 3 | 86% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，3 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1920，3 个样本
- 高度 中位数 1280，观测区间 1080 - 1536，3 个样本，取值集中（一致性 86%）
