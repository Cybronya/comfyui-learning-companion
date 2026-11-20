---
name: text_to_image_lora_sampler_clip_209
type: Text To Image
frequency: 9
level: strong
coverage: 0.890111
common_nodes: [BatchImagesNode, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 2.1图片编辑测试工作流，图生图处理方案_2103536589963087874.json, 图片生成/图生图/Qwen Image 2.1 BFS换脸换头工作流，角色一致性图生图面部替换_2106134123172683777.json, 图片生成/图生图/Qwen Image 2.1 BFS换脸换头工作流，角色一致性图生图面部替换工具_2105787847952392193.json, 图片生成/图生图/Qwen Image 2.1 BFS换脸换头工作流，角色一致性图生图面部替换工具_2106129646071926786.json, 图片生成/图生图/Qwen Image 2.1图片编辑工作流官流版，局部重绘人像写真图生图方案_2106901434481602561.json, 图片生成/图生图/Qwen Image 2.1官方图片编辑｜局部重绘人像写真_2106601449881952257.json, 图片生成/图生图/Qwen Image 2.1漫转真｜二次元图一键转真人写真_2106609135612686338.json, 图片生成/图生图/Qwen_Image_2.1图片编辑工作流官流版，局部重绘人像写真图生图方案_2108733918542389249.json, 图片生成/图生图/千问2.1图片编辑测试工作流｜文生图图生图双修，稳定可用优先_2107371246542475265.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_209

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen 2.1图片编辑测试工作流，图生图处理方案_2103536589963087874.json、图片生成/图生图/Qwen Image 2.1 BFS换脸换头工作流，角色一致性图生图面部替换_2106134123172683777.json、图片生成/图生图/Qwen Image 2.1 BFS换脸换头工作流，角色一致性图生图面部替换工具_2105787847952392193.json、图片生成/图生图/Qwen Image 2.1 BFS换脸换头工作流，角色一致性图生图面部替换工具_2106129646071926786.json、图片生成/图生图/Qwen Image 2.1图片编辑工作流官流版，局部重绘人像写真图生图方案_2106901434481602561.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 8/9 个有
- `ComfySwitchNode` —— 6/9 个有
- `JoinStrings` —— 6/9 个有
- `PreviewImage` —— 6/9 个有
- `PrimitiveBoolean` —— 6/9 个有
- `ShowText|pysssss` —— 6/9 个有
- `easy positive` —— 6/9 个有
- `ImageConcatMulti` —— 5/9 个有
- `ImageScaleToTotalPixels` —— 5/9 个有
- `LoadImageGoohai` —— 3/9 个有
- `MuyeTextEditOutput` —— 3/9 个有
- `SplitImageWithAlpha` —— 3/9 个有
- `VOSR2ModelLoader` —— 3/9 个有
- `VOSR2Upscale` —— 3/9 个有
- `ModelPreviewOverrideKJ` —— 2/9 个有
- `EmptyImage` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（13/9 个样本）：Steps较低可能导致细节不足
