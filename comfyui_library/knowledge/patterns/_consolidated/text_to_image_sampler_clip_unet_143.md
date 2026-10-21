---
name: text_to_image_sampler_clip_unet_143
type: Text To Image
frequency: 3
level: strong
coverage: 0.896333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, JjkText, JoinStringMulti, KSampler, SaveImage, SeedVR2, ShowAnything|Mie, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/动漫模型anima文生图（API调用）_2057341043246460930.json, 图片生成/文生图/动漫模型anima文生图（千问3）_2057344225120972802.json, 图片生成/文生图/动漫模型anima文生图（手动版）_2056539223683063809.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_143

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/动漫模型anima文生图（API调用）_2057341043246460930.json、图片生成/文生图/动漫模型anima文生图（千问3）_2057344225120972802.json、图片生成/文生图/动漫模型anima文生图（手动版）_2056539223683063809.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `JjkText`
- `JoinStringMulti`
- `KSampler`
- `SaveImage`
- `SeedVR2`
- `ShowAnything|Mie`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_LLMAPI_Pro_Node` —— 1/3 个有
- `llama_cpp_instruct_adv` —— 1/3 个有
- `llama_cpp_model_loader` —— 1/3 个有
- `llama_cpp_parameters` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 40 - 40 | 3 | 100% |
| Prompt 约束强度(CFG) | 5 | 5 - 5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1920 | 1920 - 1920 | 3 | 100% |
| 高度 | 1128 | 1128 - 1128 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 40 - 40，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1920，观测区间 1920 - 1920，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1128，观测区间 1128 - 1128，3 个样本，取值集中（一致性 100%）
