---
name: text_to_image_lora_sampler_clip_534
type: Text To Image
frequency: 3
level: strong
coverage: 0.892
common_nodes: [AddLabel, CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize, GetImagesFromBatchIndexed, GetVideoComponents, JjkText, KSampler, LoadVideoWithFilename, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, easy batchAnything, easy convertAnything, easy forLoopEnd, easy forLoopStart, easy imageScaleDownBy, easy indexAnything, easy mathInt, solarL_SaveImagesToZip, workflow>合并]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/视频二创神器_姿势提取加角色设定提取，角色一致性图生图_2110439126616072193.json, 图片生成/图生图/视频二创神器_姿势提取加角色设定提取，角色一致性图生图_2114178239458529282.json, 图片生成/图生图/视频姿势提取二创｜角色设定图生图角色一致性_2092199662181765122.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_534

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/视频二创神器_姿势提取加角色设定提取，角色一致性图生图_2110439126616072193.json、图片生成/图生图/视频二创神器_姿势提取加角色设定提取，角色一致性图生图_2114178239458529282.json、图片生成/图生图/视频姿势提取二创｜角色设定图生图角色一致性_2092199662181765122.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `AddLabel`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize`
- `GetImagesFromBatchIndexed`
- `GetVideoComponents`
- `JjkText`
- `KSampler`
- `LoadVideoWithFilename`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy batchAnything`
- `easy convertAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageScaleDownBy`
- `easy indexAnything`
- `easy mathInt`
- `solarL_SaveImagesToZip`
- `workflow>合并`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 2/3 个有
- `EmptyImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
