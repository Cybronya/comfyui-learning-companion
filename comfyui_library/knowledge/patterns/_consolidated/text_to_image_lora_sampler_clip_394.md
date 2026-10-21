---
name: text_to_image_lora_sampler_clip_394
type: Text To Image
frequency: 2
level: weak
coverage: 0.857
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, RHLLMChatNode, RH_Captioner, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/（风格Lora版）Anima 自动_反推提示词_2073959866328432640.json, 图片生成/文生图/（风格Lora版）Anima+自动_反推提示词_2074373405180260354.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_394

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/（风格Lora版）Anima 自动_反推提示词_2073959866328432640.json、图片生成/文生图/（风格Lora版）Anima+自动_反推提示词_2074373405180260354.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RHLLMChatNode`
- `RH_Captioner`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1528 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1528，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
