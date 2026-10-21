---
name: text_to_image_sampler_clip_unet_101
type: Text To Image
frequency: 4
level: moderate
coverage: 0.83375
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyLatentImage, KSampler, RHLLMChatNode, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/Anima base V1.0 正式版_2057422872104235009.json, 图片生成/文生图/AnimaBase-动漫抽卡神器-全自动提示词-文生图_2057408001748856833.json, 图片生成/文生图/（Lora版）Anima 自动提示词文生图V1_2059972222953017346.json, 图片生成/文生图/（动漫抽卡神器）Anima V1.0正式版自动提示词文生图V4_2056904337720430594.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_101

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Anima base V1.0 正式版_2057422872104235009.json、图片生成/文生图/AnimaBase-动漫抽卡神器-全自动提示词-文生图_2057408001748856833.json、图片生成/文生图/（Lora版）Anima 自动提示词文生图V1_2059972222953017346.json、图片生成/文生图/（动漫抽卡神器）Anima V1.0正式版自动提示词文生图V4_2056904337720430594.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyLatentImage`
- `KSampler`
- `RHLLMChatNode`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ConcatTextOfUtils` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `Random Line` —— 3/4 个有
- `Florence2ModelLoader` —— 2/4 个有
- `Florence2Run` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `AnimaArtistStyleT8` —— 1/4 个有
- `AnimaPromptCombinerT8` —— 1/4 个有
- `AnimaPromptT8` —— 1/4 个有
- `Latent Switch (JPS)` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `VRGDG_ShowAny` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 10 - 40 | 4 | 60% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 4 | 58% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1920 | 1080 - 3056 | 4 | 65% |
| 高度 | 1080 | 1080 - 1920 | 4 | 72% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 10 - 40，4 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，4 个样本
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1920，观测区间 1080 - 3056，4 个样本
- 高度 中位数 1080，观测区间 1080 - 1920，4 个样本
