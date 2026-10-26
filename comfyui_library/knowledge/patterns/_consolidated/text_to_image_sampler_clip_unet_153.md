---
name: text_to_image_sampler_clip_unet_153
type: Text To Image
frequency: 4
level: moderate
coverage: 0.59525
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, PreviewAny, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AI代码侠土豆-Krea2光速风格迁移+超清图_2071481926183112706.json, 图片生成/图生图/风格迁移_Krea2_2072259727437942786.json, 图片生成/文生图/Krea2 Turbo 文生图  + 高清_2070085337044574209.json, 图片生成/文生图/Krea2光速风格迁移+超清图_2071859542836736001.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_153

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/AI代码侠土豆-Krea2光速风格迁移+超清图_2071481926183112706.json、图片生成/图生图/风格迁移_Krea2_2072259727437942786.json、图片生成/文生图/Krea2 Turbo 文生图  + 高清_2070085337044574209.json、图片生成/文生图/Krea2光速风格迁移+超清图_2071859542836736001.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `PreviewAny`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `1hew_StringJoinMulti` —— 3/4 个有
- `AILab_QwenVL` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `SeedVR2LoadDiTModel` —— 3/4 个有
- `SeedVR2LoadVAEModel` —— 3/4 个有
- `SeedVR2VideoUpscaler` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `Text` —— 3/4 个有
- `ResolutionSelector` —— 2/4 个有
- `StringConcatenate` —— 2/4 个有
- `TTResolutionSelector` —— 2/4 个有
- `TextGenerate` —— 2/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `easy positive` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 4 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler_ancestral | - | 4 | 75% |
| 调度器 | beta57 | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 512 | 512 - 1024 | 4 | 65% |
| 高度 | 512 | 512 - 1024 | 4 | 65% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，4 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 75%
- 调度器 最常用 beta57，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 1024，4 个样本
- 高度 中位数 512，观测区间 512 - 1024，4 个样本
