---
name: text_to_image_sampler_clip_unet_221
type: Text To Image
frequency: 2
level: weak
coverage: 0.9075
common_nodes: [CLIPLoader, CLIPTextEncode, CM_BoolToInt, CR Prompt Text, CR Text Replace, EmptyLatentImage, ExecutionBlocker, If ANY execute A else B, ImpactNeg, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PlaySound|pysssss, PrimitiveBoolean, RHLLMChatNode, SaveImage, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy mathString]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/anima自动角色立绘_2079854385512931330.json, 图片生成/文生图/anima自动角色立绘生成｜文生图反推提示词角色设计_2091241220306726914.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_221

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/anima自动角色立绘_2079854385512931330.json、图片生成/文生图/anima自动角色立绘生成｜文生图反推提示词角色设计_2091241220306726914.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CM_BoolToInt`
- `CR Prompt Text`
- `CR Text Replace`
- `EmptyLatentImage`
- `ExecutionBlocker`
- `If ANY execute A else B`
- `ImpactNeg`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PlaySound|pysssss`
- `PrimitiveBoolean`
- `RHLLMChatNode`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy mathString`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `easy showAnything` —— 1/2 个有
- `solarL_SaveImagesToZip` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22 | - | 2 | 18% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 680 | - | 2 | 12% |
| 高度 | 680 | - | 2 | 12% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 22，样本不足，未给区间，2 个样本，取值分散，一致性仅 18%
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 680，样本不足，未给区间，2 个样本，取值分散，一致性仅 12%
- 高度 中位数 680，样本不足，未给区间，2 个样本，取值分散，一致性仅 12%
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
