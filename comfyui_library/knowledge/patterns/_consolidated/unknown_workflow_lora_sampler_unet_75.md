---
name: unknown_workflow_lora_sampler_unet_75
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.953333
common_nodes: [CLIPLoader, ConditioningZeroOut, CropWithPadInfo, KSampler, LoadImage, LoraLoaderModelOnly, QwenEditConfigPreparer, QwenEditOutputExtractor, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/二次元国风漫画风格转绘-qwen2511-小宣喧-rh_2039599859279335425.json, 图片生成/图生图/千问→异形背景墙灯带（发布版本）_2057265237006569474.json, 图片生成/图生图/千问→白色自发光红框框选（发布版本）_2057265127598149633.json, 图片生成/图生图/千问→镜面材质红框框选（发布版本）_2057265361845837826.json, 图片生成/图生图/智柚AI模型渲染1-26v2_2015695801804136450.json, 图片生成/图生图/智柚AI模型渲染1-26v3_2062727167049551874.json, 图片生成/图生图/美漫风格转绘-Qwen2511-小宣喧-RH_2042055399045603329.json, 图片生成/图生图/（童装版）模特换姿势qwen2511_2040093318956191746.json, 图片生成/图生图/（童装版）模特换衣模特换装+模特换姿势qwen2511_2040078089027325953.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_75

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/二次元国风漫画风格转绘-qwen2511-小宣喧-rh_2039599859279335425.json、图片生成/图生图/千问→异形背景墙灯带（发布版本）_2057265237006569474.json、图片生成/图生图/千问→白色自发光红框框选（发布版本）_2057265127598149633.json、图片生成/图生图/千问→镜面材质红框框选（发布版本）_2057265361845837826.json、图片生成/图生图/智柚AI模型渲染1-26v2_2015695801804136450.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `CropWithPadInfo`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 7/9 个有
- `SaveImage` —— 7/9 个有
- `PreviewImage` —— 4/9 个有
- `DWPreprocessor` —— 2/9 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/9 个有
- `Image Comparer (rgthree)` —— 2/9 个有
- `ImageResize+` —— 2/9 个有
- `ImageStitch` —— 2/9 个有
- `KOOK_SaveJPGImage` —— 2/9 个有
- `GetImage` —— 1/9 个有
- `kkGetImage` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 10 | 9 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | beta57 | - | 9 | 78% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 10，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 beta57，9 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（7/9 个样本）：Steps较低可能导致细节不足
