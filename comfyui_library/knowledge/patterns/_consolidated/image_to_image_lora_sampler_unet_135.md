---
name: image_to_image_lora_sampler_unet_135
type: Image To Image
frequency: 6
level: strong
coverage: 0.911833
common_nodes: [CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图片编辑 改图_2112431618567794689.json, 图片生成/图生图/图生图 _ 场景角度切换_1996085406431166466.json, 图片生成/图生图/头像生成_2044697290111193089.json, 图片生成/图生图/室内设计 建筑设计   效果图 渲染图_2060281824609390593.json, 图片生成/图生图/灵魂画手工作流_1972209323231342593.json, 平台全量/漫画转真人  动漫转真人 线稿转真人  线稿上色 去AI感 超真实_2118301684203081729.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_135

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/图片编辑 改图_2112431618567794689.json、图片生成/图生图/图生图 _ 场景角度切换_1996085406431166466.json、图片生成/图生图/头像生成_2044697290111193089.json、图片生成/图生图/室内设计 建筑设计   效果图 渲染图_2060281824609390593.json、图片生成/图生图/灵魂画手工作流_1972209323231342593.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/6 个有
- `CFGNorm` —— 3/6 个有
- `ModelSamplingAuraFlow` —— 3/6 个有
- `TextEncodeQwenImageEdit` —— 3/6 个有
- `WD14Tagger|pysssss` —— 3/6 个有
- `easy showAnything` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `ImageResizePresetNode` —— 1/6 个有
- `LayerFilter: GaussianBlur` —— 1/6 个有
- `MaskToImage` —— 1/6 个有
- `PIP_图像联结` —— 1/6 个有
- `Qwen3_VQA_Plus` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 6 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | res_2m | - | 6 | 50% |
| 调度器 | sgm_uniform | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2m，6 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
