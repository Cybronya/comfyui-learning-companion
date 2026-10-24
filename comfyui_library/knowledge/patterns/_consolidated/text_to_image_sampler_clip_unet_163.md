---
name: text_to_image_sampler_clip_unet_163
type: Text To Image
frequency: 4
level: moderate
coverage: 0.9065
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/flux1-krea-文生图_1951258671458234369.json, 图片生成/文生图/krea-文生图-Moebius (Jean Giraud)风格美洲虎捕猎鳄鱼_1962669092442386433.json, 图片生成/文生图/【遇见AI】flex2-preview 基础文生图_2049429860640100354.json, 图片生成/文生图/【阡陌】FLUX krea 文生图工作流_1951489939009646593.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_163

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/flux1-krea-文生图_1951258671458234369.json、图片生成/文生图/krea-文生图-Moebius (Jean Giraud)风格美洲虎捕猎鳄鱼_1962669092442386433.json、图片生成/文生图/【遇见AI】flex2-preview 基础文生图_2049429860640100354.json、图片生成/文生图/【阡陌】FLUX krea 文生图工作流_1951489939009646593.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
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
- `LoadImage` —— 3/4 个有
- `RH_Translator` —— 2/4 个有
- `Flex2Conditioner` —— 1/4 个有
- `FluxGuidance` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 24 | 20 - 30 | 4 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 4 | 33% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 896 | 512 - 1024 | 4 | 74% |
| 高度 | 1024 | 512 - 1536 | 4 | 65% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 24，观测区间 20 - 30，4 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，4 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 896，观测区间 512 - 1024，4 个样本
- 高度 中位数 1024，观测区间 512 - 1536，4 个样本
