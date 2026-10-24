---
name: text_to_image_video_lora_sampler_101
type: Text To Image
frequency: 7
level: strong
coverage: 0.731429
common_nodes: [Any Switch (rgthree), AutoCropFaces, BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, Fast Groups Bypasser (rgthree), Fast Muter (rgthree), GetImagesFromBatchIndexed, GetNode, GetVideoComponents, Image Comparer (rgthree), ImageConcatFromBatch, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PreviewImage, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/H3角色资产四视图制作 超强一致性角色卡详拆_2098838938864668673.json, 图片生成/图生图/H3角色资产四视图角色卡超强一致性详拆图生图工具_2101388653078605826.json, 图片生成/图生图/H3角色资产四视图角色卡超强一致性详拆图生图工具_2101860871252303874.json, 图片生成/图生图/H3角色资产四视图详拆08集｜超强一致性角色卡制作教学｜图生图_2099144828830445570.json, 图片生成/图生图/MiniMax H3短剧人物设定多视图 角色一致性图生图_2098840781778935810.json, 图片生成/图生图/Minimax H3 AI短剧人物多视图设定｜角色一致性立绘一次到位｜图生图_2099129262816190466.json, 数字人/数字人/Minimax H3高一致性人物四视图快速处理V2.0 PLUS工作流，人物类特效图生图_2107980124158259202.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_101

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/H3角色资产四视图制作 超强一致性角色卡详拆_2098838938864668673.json、图片生成/图生图/H3角色资产四视图角色卡超强一致性详拆图生图工具_2101388653078605826.json、图片生成/图生图/H3角色资产四视图角色卡超强一致性详拆图生图工具_2101860871252303874.json、图片生成/图生图/H3角色资产四视图详拆08集｜超强一致性角色卡制作教学｜图生图_2099144828830445570.json、图片生成/图生图/MiniMax H3短剧人物设定多视图 角色一致性图生图_2098840781778935810.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 7 个 workflow 都包含：
- `Any Switch (rgthree)`
- `AutoCropFaces`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Muter (rgthree)`
- `GetImagesFromBatchIndexed`
- `GetNode`
- `GetVideoComponents`
- `Image Comparer (rgthree)`
- `ImageConcatFromBatch`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 6/7 个有
- `ResizeImageMaskNode` —— 5/7 个有
- `workflow>SeedVR放大节点` —— 5/7 个有
- `ImageScaleBy` —— 4/7 个有
- `VOSR2ModelLoader` —— 4/7 个有
- `VOSR2Upscale` —— 4/7 个有
- `easy float` —— 4/7 个有
- `easy int` —— 4/7 个有
- `ImageScaleToTotalPixels` —— 2/7 个有
- `SeedVR2LoadDiTModel` —— 2/7 个有
- `SeedVR2LoadVAEModel` —— 2/7 个有
- `SeedVR2VideoUpscaler` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
