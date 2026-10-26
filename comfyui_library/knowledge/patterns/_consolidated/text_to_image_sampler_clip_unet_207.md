---
name: text_to_image_sampler_clip_unet_207
type: Text To Image
frequency: 3
level: strong
coverage: 0.835333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ConcatTextOfUtils, EmptyLatentImage, KSampler, RHLLMChatNode, Random Line, SaveImage, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/自动优化提示词（动漫大批量出图）Anima V1.1_2078467633908895746.json, 图片生成/文生图/（动漫大批量出图）Anima V1.1自动扩写提示词_2078405199697371137.json, 图片生成/文生图/（动漫抽卡神器）Anima V1.1自动提示词文生图_2077989830809710594.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_207

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/自动优化提示词（动漫大批量出图）Anima V1.1_2078467633908895746.json、图片生成/文生图/（动漫大批量出图）Anima V1.1自动扩写提示词_2078405199697371137.json、图片生成/文生图/（动漫抽卡神器）Anima V1.1自动提示词文生图_2077989830809710594.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConcatTextOfUtils`
- `EmptyLatentImage`
- `KSampler`
- `RHLLMChatNode`
- `Random Line`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ProcessString` —— 2/3 个有
- `easy convertAnything` —— 2/3 个有
- `easy promptLine` —— 2/3 个有
- `孤海注释` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 40 - 40 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1080 | 1080 - 1080 | 3 | 100% |
| 高度 | 1920 | 1920 - 1920 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 40 - 40，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1080，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，3 个样本，取值集中（一致性 100%）
