---
name: text_to_image_lora_sampler_clip_621
type: Text To Image
frequency: 2
level: weak
coverage: 0.8985
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DapaoImageAspectRatioResizeNode, EmptyLatentImage, Fast Bypasser (rgthree), KSampler, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, Mute / Bypass Repeater (rgthree), Qwen3VL_Chat, RandomNoise, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAELoader, easy int, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/251225001.015.Z-image 二次元拆解专属lora+提取人物特征_2004261138974076930.json, 平台全量/Z-image 二次元拆解 +提取人物表情特征+服饰服装_2006989429369479169.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_621

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/251225001.015.Z-image 二次元拆解专属lora+提取人物特征_2004261138974076930.json、平台全量/Z-image 二次元拆解 +提取人物表情特征+服饰服装_2006989429369479169.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DapaoImageAspectRatioResizeNode`
- `EmptyLatentImage`
- `Fast Bypasser (rgthree)`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mute / Bypass Repeater (rgthree)`
- `Qwen3VL_Chat`
- `RandomNoise`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy int`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 2048 | - | 2 | 100% |
| 高度 | 2048 | - | 2 | 100% |
| 采样步数 | 9 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 2048，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 2048，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
