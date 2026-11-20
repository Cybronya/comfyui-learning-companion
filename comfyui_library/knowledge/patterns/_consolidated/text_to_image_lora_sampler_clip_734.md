---
name: text_to_image_lora_sampler_clip_734
type: Text To Image
frequency: 2
level: weak
coverage: 0.5455
common_nodes: [Anything Everywhere, CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, JjkText, JoinStrings, KSampler, LayerColor: AutoAdjust, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Lora Loader, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [平台全量/Krea2_次元人像摄影 （文生图+图生图工作流）_2118495612768444418.json, 平台全量/Zimage_lora_AI素人_李恩珠脸模文生图+反推工作流_2118956508196204545.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_734

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Krea2_次元人像摄影 （文生图+图生图工作流）_2118495612768444418.json、平台全量/Zimage_lora_AI素人_李恩珠脸模文生图+反推工作流_2118956508196204545.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：55%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `JjkText`
- `JoinStrings`
- `KSampler`
- `LayerColor: AutoAdjust`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Lora Loader`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有
- `llama_cpp_model_loader` —— 1/2 个有
- `llama_cpp_parameters` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12.5 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_2s | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1420 | - | 2 | 92% |
| 高度 | 1960 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 12.5，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1420，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- 高度 中位数 1960，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
