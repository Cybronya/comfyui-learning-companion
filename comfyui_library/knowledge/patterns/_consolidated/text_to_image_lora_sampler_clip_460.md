---
name: text_to_image_lora_sampler_clip_460
type: Text To Image
frequency: 4
level: strong
coverage: 0.73175
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, GetNode, INTConstant, JjkText, KSampler, KSamplerAdvanced, LoraLoaderModelOnly, SaveImage, SetNode, Text Multiline, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/智绘品牌秒出全案｜LOGO名片招牌工服多场景自动生成_2090089023988654082.json, 图片生成/文生图/短剧主角人设文生图｜附带提示词直接套用出图_2106591010779385858.json, 图片生成/文生图/短剧人物主角设计附带提示词工作流，文生图角色设计创作工具_2106893671210766338.json, 图片生成/文生图/短剧人物主角设计附带提示词工作流，文生图角色设计创作工具_2108742835515248641.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_460

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/智绘品牌秒出全案｜LOGO名片招牌工服多场景自动生成_2090089023988654082.json、图片生成/文生图/短剧主角人设文生图｜附带提示词直接套用出图_2106591010779385858.json、图片生成/文生图/短剧人物主角设计附带提示词工作流，文生图角色设计创作工具_2106893671210766338.json、图片生成/文生图/短剧人物主角设计附带提示词工作流，文生图角色设计创作工具_2108742835515248641.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetNode`
- `INTConstant`
- `JjkText`
- `KSampler`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SetNode`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 3/4 个有
- `CR Text` —— 3/4 个有
- `Int` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `Text Concatenate` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `EmptyImage` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `JjkShowText` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `RH_RhartImageG2ImageToImage` —— 1/4 个有
- `TextEncodeQwenImageEditPlus` —— 1/4 个有
- `VAEEncode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
