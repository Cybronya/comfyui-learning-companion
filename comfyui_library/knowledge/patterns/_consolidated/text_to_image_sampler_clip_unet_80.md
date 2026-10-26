---
name: text_to_image_sampler_clip_unet_80
type: Text To Image
frequency: 8
level: strong
coverage: 0.834625
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Anima+ToriiGate-0.5无审查反推+controlnet强控图生图(已修复)_2061398059543785474.json, 图片生成/图生图/Anima+ToriiGate-0.5无审查反推图生图(ToriiGate反推节点已修复)_2061105029859336193.json, 图片生成/图生图/Anima+V1.0 图生图 二次元手绘风 anima_base 卡通动漫角色Q版可爱动画风_2057338559039885313.json, 图片生成/文生图/Anima Base any-test-like控制生图_2073323335081095169.json, 图片生成/文生图/Anima V1.0正式版参考图生图_2056978691254734849.json, 图片生成/文生图/Anima base V1.0 正式版_2057422872104235009.json, 图片生成/文生图/反推提示词后anima文生图+全节点注释_2056999144727867393.json, 图片生成/文生图/（动漫抽卡神器）Anima V1.0正式版自动提示词文生图V4_2056904337720430594.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_80

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Anima+ToriiGate-0.5无审查反推+controlnet强控图生图(已修复)_2061398059543785474.json、图片生成/图生图/Anima+ToriiGate-0.5无审查反推图生图(ToriiGate反推节点已修复)_2061105029859336193.json、图片生成/图生图/Anima+V1.0 图生图 二次元手绘风 anima_base 卡通动漫角色Q版可爱动画风_2057338559039885313.json、图片生成/文生图/Anima Base any-test-like控制生图_2073323335081095169.json、图片生成/文生图/Anima V1.0正式版参考图生图_2056978691254734849.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 7/8 个有
- `ConcatTextOfUtils` —— 7/8 个有
- `easy showAnything` —— 7/8 个有
- `Florence2ModelLoader` —— 5/8 个有
- `Florence2Run` —— 5/8 个有
- `RHLLMChatNode` —— 3/8 个有
- `Random Line` —— 3/8 个有
- `AnimaLLLiteApply` —— 2/8 个有
- `ToriiGateT8_LlamaCppVisionGenerate` —— 2/8 个有
- `AnimaArtistStyleT8` —— 1/8 个有
- `AnimaPromptCombinerT8` —— 1/8 个有
- `AnimaPromptT8` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `RHHiddenNodes` —— 1/8 个有
- `VRGDG_ShowAny` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 30 - 40 | 8 | 91% |
| Prompt 约束强度(CFG) | 4.5 | 4 - 4.5 | 8 | 96% |
| 采样算法 | er_sde | - | 8 | 75% |
| 调度器 | beta | - | 8 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1560 | 1000 - 1920 | 8 | 72% |
| 高度 | 1080 | 1024 - 1920 | 8 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 30 - 40，8 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4 - 4.5，8 个样本，取值集中（一致性 96%）
- 采样算法 最常用 er_sde，8 个样本，一致性 75%
- 调度器 最常用 beta，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1560，观测区间 1000 - 1920，8 个样本
- 高度 中位数 1080，观测区间 1024 - 1920，8 个样本
