---
name: text_to_image_lora_sampler_clip_456
type: Text To Image
frequency: 4
level: moderate
coverage: 0.894
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/超唯美生图：ZIT动漫大模+写实幻想曲lora_1994702476790075393.json, 图片生成/文生图/（Lora版）Anima 自动提示词文生图V1_2059972222953017346.json, 图片生成/文生图/（风格Lora版）Anima 自动_反推提示词_2073959866328432640.json, 图片生成/文生图/（风格Lora版）Anima+自动_反推提示词_2074373405180260354.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_456

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/超唯美生图：ZIT动漫大模+写实幻想曲lora_1994702476790075393.json、图片生成/文生图/（Lora版）Anima 自动提示词文生图V1_2059972222953017346.json、图片生成/文生图/（风格Lora版）Anima 自动_反推提示词_2073959866328432640.json、图片生成/文生图/（风格Lora版）Anima+自动_反推提示词_2074373405180260354.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `RHLLMChatNode` —— 3/4 个有
- `RH_Captioner` —— 2/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `JDCN_StringToList` —— 1/4 个有
- `Text Multiline` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 12 - 40 | 4 | 63% |
| Prompt 约束强度(CFG) | 4.5 | 1.1 - 4.5 | 4 | 60% |
| 采样算法 | er_sde | - | 4 | 75% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1068 | 1024 - 3056 | 4 | 44% |
| 高度 | 1528 | 1080 - 1984 | 4 | 79% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 12 - 40，4 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1.1 - 4.5，4 个样本
- 采样算法 最常用 er_sde，4 个样本，一致性 75%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1068，观测区间 1024 - 3056，4 个样本，取值分散，一致性仅 44%
- 高度 中位数 1528，观测区间 1080 - 1984，4 个样本
