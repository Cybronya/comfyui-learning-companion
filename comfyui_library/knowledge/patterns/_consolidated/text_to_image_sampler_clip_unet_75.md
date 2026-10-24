---
name: text_to_image_sampler_clip_unet_75
type: Text To Image
frequency: 8
level: moderate
coverage: 0.83825
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Anima+ToriiGate-0.5无审查反推+controlnet强控图生图(已修复)_2061398059543785474.json, 图片生成/图生图/Anima+ToriiGate-0.5无审查反推图生图(ToriiGate反推节点已修复)_2061105029859336193.json, 图片生成/图生图/Anima+V1.0 图生图 二次元手绘风 anima_base 卡通动漫角色Q版可爱动画风_2057338559039885313.json, 图片生成/图生图/（风格Lora版）Anima 自动提示词文生图V1_2060735043315785730.json, 图片生成/文生图/Anima V1.0正式版参考图生图_2056978691254734849.json, 图片生成/文生图/Anima base V1.0 正式版_2057422872104235009.json, 图片生成/文生图/AnimaBase-动漫抽卡神器-全自动提示词-文生图_2057408001748856833.json, 图片生成/文生图/反推提示词后anima文生图+全节点注释_2056999144727867393.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_75

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Anima+ToriiGate-0.5无审查反推+controlnet强控图生图(已修复)_2061398059543785474.json、图片生成/图生图/Anima+ToriiGate-0.5无审查反推图生图(ToriiGate反推节点已修复)_2061105029859336193.json、图片生成/图生图/Anima+V1.0 图生图 二次元手绘风 anima_base 卡通动漫角色Q版可爱动画风_2057338559039885313.json、图片生成/图生图/（风格Lora版）Anima 自动提示词文生图V1_2060735043315785730.json、图片生成/文生图/Anima V1.0正式版参考图生图_2056978691254734849.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ConcatTextOfUtils` —— 7/8 个有
- `LoadImage` —— 7/8 个有
- `Florence2ModelLoader` —— 4/8 个有
- `Florence2Run` —— 4/8 个有
- `RHLLMChatNode` —— 4/8 个有
- `Random Line` —— 3/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `ToriiGateT8_LlamaCppVisionGenerate` —— 2/8 个有
- `AnimaLLLiteApply` —— 1/8 个有
- `Latent Switch (JPS)` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `RHHiddenNodes` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 10 - 40 | 8 | 73% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 8 | 72% |
| 采样算法 | er_sde | - | 8 | 75% |
| 调度器 | beta | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1920 | 1000 - 3056 | 8 | 64% |
| 高度 | 1080 | 1080 - 1920 | 8 | 76% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 10 - 40，8 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，8 个样本
- 采样算法 最常用 er_sde，8 个样本，一致性 75%
- 调度器 最常用 beta，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1920，观测区间 1000 - 3056，8 个样本
- 高度 中位数 1080，观测区间 1080 - 1920，8 个样本
