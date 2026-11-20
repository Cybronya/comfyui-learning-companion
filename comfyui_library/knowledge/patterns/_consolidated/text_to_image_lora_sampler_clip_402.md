---
name: text_to_image_lora_sampler_clip_402
type: Text To Image
frequency: 5
level: weak
coverage: 0.7162
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, GetNode, INTConstant, KSampler, KSamplerAdvanced, LoraLoaderModelOnly, SaveImage, SetNode, Text Multiline, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/智绘品牌秒出全案｜LOGO名片招牌工服多场景自动生成_2090089023988654082.json, 图片生成/文生图/短剧主角人设文生图｜附带提示词直接套用出图_2106591010779385858.json, 图片生成/文生图/短剧人物主角设计附带提示词工作流，文生图角色设计创作工具_2106893671210766338.json, 图片生成/文生图/短剧人物主角设计附带提示词工作流，文生图角色设计创作工具_2108742835515248641.json, 平台全量/智绘品牌 · 秒出全案_2088142228068847618.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_402

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/智绘品牌秒出全案｜LOGO名片招牌工服多场景自动生成_2090089023988654082.json、图片生成/文生图/短剧主角人设文生图｜附带提示词直接套用出图_2106591010779385858.json、图片生成/文生图/短剧人物主角设计附带提示词工作流，文生图角色设计创作工具_2106893671210766338.json、图片生成/文生图/短剧人物主角设计附带提示词工作流，文生图角色设计创作工具_2108742835515248641.json、平台全量/智绘品牌 · 秒出全案_2088142228068847618.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetNode`
- `INTConstant`
- `KSampler`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SetNode`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 4/5 个有
- `solarL_SaveImagesToZip` —— 4/5 个有
- `AILab_QwenVL` —— 3/5 个有
- `CR Text` —— 3/5 个有
- `Int` —— 3/5 个有
- `ModelSamplingAuraFlow` —— 3/5 个有
- `Text Concatenate` —— 3/5 个有
- `孤海注释` —— 3/5 个有
- `ImageScaleToTotalPixels` —— 2/5 个有
- `JjkShowText` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `RH_LLMAPI_NODE` —— 2/5 个有
- `RH_RhartImageG2ImageToImage` —— 2/5 个有
- `TextEncodeQwenImageEditPlus` —— 2/5 个有
- `VAEEncode` —— 2/5 个有
- `EmptyImage` —— 1/5 个有
- `PreviewImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 8 | 5 | 73% |
| 采样算法 | er_sde | - | 5 | 80% |
| 调度器 | beta | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 1024 | 5 | 0% |
| 高度 | 80 | 80 - 1536 | 5 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 8，5 个样本
- 采样算法 最常用 er_sde，5 个样本，一致性 80%
- 调度器 最常用 beta，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，5 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1536，5 个样本，取值分散，一致性仅 0%
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
