---
name: image_to_image_lora_sampler_unet_38
type: Image To Image
frequency: 15
level: strong
coverage: 0.887
common_nodes: [CLIPLoader, EmptySD3LatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen2511一键人头部多角度_2057125039929118722.json, 图片生成/图生图/qwen2511一键人头部多角度_2060165198916448257.json, 图片生成/图生图/qwen2511美女多角度美图生成_2061363062426398721.json, 图片生成/图生图/一键人物多角度qwen-edit-2511_1995447122415824897.json, 图片生成/图生图/人物表情迁移_2003532219891261442.json, 图片生成/图生图/千问编辑2511-人物多角度出图_2003744366952890369.json, 图片生成/图生图/千问编辑2511-人物多角度出图_2041116912347783169.json, 图片生成/图生图/图片多角度镜头调度qwen-image-edit-2509_2054884995881283585.json, 图片生成/图生图/图片多角度镜头调度qwen-image-edit-2509_2056222385287778305.json, 图片生成/图生图/图片多角度镜头调度qwen-image-edit-2509_2090260862845149185.json, 图片生成/图生图/图片多角度镜头调度qwen-image-edit-2509_2090607346560094210.json, 图片生成/图生图/图片多角度镜头调度qwen-image-edit-2509_2090624833217458178.json, 图片生成/图生图/图生图+qwen2511+一键人头部多角度_2059435976203784193.json, 平台全量/一键角色多角度_2061328198817894401.json, 平台全量/镜头调度qwen-image-edit-2509_2001898906076233730.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_38

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/qwen2511一键人头部多角度_2057125039929118722.json、图片生成/图生图/qwen2511一键人头部多角度_2060165198916448257.json、图片生成/图生图/qwen2511美女多角度美图生成_2061363062426398721.json、图片生成/图生图/一键人物多角度qwen-edit-2511_1995447122415824897.json、图片生成/图生图/人物表情迁移_2003532219891261442.json…）

- **类型**：Image To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 14/15 个有
- `LayerUtility: PurgeVRAM` —— 13/15 个有
- `PreviewImage` —— 13/15 个有
- `CFGNorm` —— 10/15 个有
- `easy promptLine` —— 9/15 个有
- `Text Multiline` —— 7/15 个有
- `PreviewAny` —— 6/15 个有
- `TextCombinerSix` —— 6/15 个有
- `ImageBatchMulti` —— 5/15 个有
- `ImageFromBatch+` —— 5/15 个有
- `ImpactImageBatchToImageList` —— 5/15 个有
- `ResizeImagesByLongerEdge` —— 5/15 个有
- `ImageScaleBy` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 10 | 15 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler_ancestral | - | 15 | 73% |
| 调度器 | simple | - | 15 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 10，15 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，15 个样本，一致性 73%
- 调度器 最常用 simple，15 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（8/15 个样本）：Steps较低可能导致细节不足
