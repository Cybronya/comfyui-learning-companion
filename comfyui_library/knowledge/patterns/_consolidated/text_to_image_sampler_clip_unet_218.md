---
name: text_to_image_sampler_clip_unet_218
type: Text To Image
frequency: 3
level: moderate
coverage: 1
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/小奶狗生成器_1922031385077547010.json, 平台全量/KEREA空白工作流txt_1954569649281220609.json, 平台全量/[jason]黑暗骑士_1950938920911577089.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_218

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/小奶狗生成器_1922031385077547010.json、平台全量/KEREA空白工作流txt_1954569649281220609.json、平台全量/[jason]黑暗骑士_1950938920911577089.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 2/3 个有
- `ArgosTranslateTextNode` —— 1/3 个有
- `Bjornulf_ShowStringText` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `FluxGuidance` —— 1/3 个有
- `LatentUpscale` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.675 | - | 2 | 52% |
| LoRA 文本强度 | 0.6 | - | 2 | 33% |
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 2048 | 3 | 65% |
| 采样步数 | 30 | 20 - 30 | 3 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.675，样本不足，未给区间，2 个样本
- LoRA 文本强度 中位数 0.6，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 2048，3 个样本
- 采样步数 中位数 30，观测区间 20 - 30，3 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
