---
name: text_to_image_sampler_clip_unet_151
type: Text To Image
frequency: 5
level: moderate
coverage: 0.9286
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/超唯美生图：ZIT动漫大模+写实幻想曲lora_1994702476790075393.json, 图片生成/文生图/造相-Z-Image-Turbo 文生图高清图像_1998205959757553665.json, 图片生成/文生图/（贞贞版）boogu满血版文生图V1_2072037602269687810.json, 图片生成/文生图/（风格Lora版）Anima 自动_反推提示词_2073959866328432640.json, 图片生成/文生图/（风格Lora版）Anima+自动_反推提示词_2074373405180260354.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_151

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/超唯美生图：ZIT动漫大模+写实幻想曲lora_1994702476790075393.json、图片生成/文生图/造相-Z-Image-Turbo 文生图高清图像_1998205959757553665.json、图片生成/文生图/（贞贞版）boogu满血版文生图V1_2072037602269687810.json、图片生成/文生图/（风格Lora版）Anima 自动_反推提示词_2073959866328432640.json、图片生成/文生图/（风格Lora版）Anima+自动_反推提示词_2074373405180260354.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `CR Prompt Text` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `LoadImage` —— 2/5 个有
- `RHLLMChatNode` —— 2/5 个有
- `RH_Captioner` —— 2/5 个有
- `CheckpointLoaderSimple` —— 1/5 个有
- `JDCN_StringToList` —— 1/5 个有
- `Text Multiline` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 7 - 50 | 5 | 43% |
| Prompt 约束强度(CFG) | 4 | 1 - 4.5 | 5 | 46% |
| 采样算法 | ddim | - | 5 | 40% |
| 调度器 | beta | - | 5 | 40% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | 1024 - 1112 | 5 | 97% |
| 高度 | 1528 | 1024 - 1984 | 5 | 79% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 40，观测区间 7 - 50，5 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4.5，5 个样本，取值分散，一致性仅 46%
- 采样算法 最常用 ddim，5 个样本，一致性 40%
- 调度器 最常用 beta，5 个样本，一致性 40%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1112，5 个样本，取值集中（一致性 97%）
- 高度 中位数 1528，观测区间 1024 - 1984，5 个样本
