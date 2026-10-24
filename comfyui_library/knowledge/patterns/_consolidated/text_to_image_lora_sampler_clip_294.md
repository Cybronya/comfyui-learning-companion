---
name: text_to_image_lora_sampler_clip_294
type: Text To Image
frequency: 6
level: strong
coverage: 0.866167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/G2.5细节修复参考版图生图处理生成工具_2101377463984152578.json, 图片生成/图生图/Qwen Image 2.1一键换脸｜图生图人物面部替换神器_2103027527827677185.json, 图片生成/图生图/Qwen Image 2.1换脸工作流，一键面部替换的图生图处理工具_2103172786389864449.json, 图片生成/图生图/Qwen Image 2.1材质迁移｜金属木质一键换质感｜设计素材秒变新风格_2102599156345958401.json, 图片生成/图生图/Qwen-image2.1扩图工作流｜图生图智能扩展画幅 边缘补全自然_2104027097525211138.json, 图片生成/图生图/画面向外扩展补全 Qwen image2.1智能扩图工作流_2104303227163467778.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_294

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/G2.5细节修复参考版图生图处理生成工具_2101377463984152578.json、图片生成/图生图/Qwen Image 2.1一键换脸｜图生图人物面部替换神器_2103027527827677185.json、图片生成/图生图/Qwen Image 2.1换脸工作流，一键面部替换的图生图处理工具_2103172786389864449.json、图片生成/图生图/Qwen Image 2.1材质迁移｜金属木质一键换质感｜设计素材秒变新风格_2102599156345958401.json、图片生成/图生图/Qwen-image2.1扩图工作流｜图生图智能扩展画幅 边缘补全自然_2104027097525211138.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `TextEncodeQwenImage21` —— 5/6 个有
- `DrawMaskOnImage` —— 4/6 个有
- `MaskFillHoles` —— 3/6 个有
- `CR Prompt Text` —— 2/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `ImagePadForOutpaint` —— 2/6 个有
- `GH_CropRestore` —— 1/6 个有
- `GH_MaskCropV2` —— 1/6 个有
- `GoohaiUniversalSlider` —— 1/6 个有
- `GrowMaskWithBlur` —— 1/6 个有
- `MaskPreview+` —— 1/6 个有
- `RH_RhartImageG25SunburstImageToImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足
