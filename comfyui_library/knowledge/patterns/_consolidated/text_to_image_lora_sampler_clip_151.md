---
name: text_to_image_lora_sampler_clip_151
type: Text To Image
frequency: 6
level: strong
coverage: 0.858833
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: [NuiKr.OpenPoseEditor]
members: [图片生成/图生图/2102549583330111489.json, 图片生成/图生图/2102560585291493377.json, 图片生成/图生图/2102623788155363330.json, 视频生成/图生视频/Qwen_Image_2.1多图编辑工作流，支持保留人物姿势换服饰等多图参考场景_2106172420255207425.json, 视频生成/图生视频/Qwen_image_2.1多图编辑int8版｜自带提示词增强｜图生图低显存友好_2104450980506062849.json, 视频生成/图生视频/qwen_image_2.1编辑工作流｜文生图图生图双支持｜日常改图必备款_2102310384794427394.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_151

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/2102549583330111489.json、图片生成/图生图/2102560585291493377.json、图片生成/图生图/2102623788155363330.json、视频生成/图生视频/Qwen_Image_2.1多图编辑工作流，支持保留人物姿势换服饰等多图参考场景_2106172420255207425.json、视频生成/图生视频/Qwen_image_2.1多图编辑int8版｜自带提示词增强｜图生图低显存友好_2104450980506062849.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 5/6 个有
- `PrimitiveBoolean` —— 5/6 个有
- `TextGenerateLTX2Prompt` —— 5/6 个有
- `PreviewImage` —— 4/6 个有
- `easy showAnything` —— 4/6 个有
- `EmptyImage` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `QwenImage21Cache` —— 3/6 个有
- `孤海注释` —— 3/6 个有
- `Fast Groups Muter (rgthree)` —— 2/6 个有
- `GetImageSize` —— 1/6 个有
- `GroupSwitcher` —— 1/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `ImageMergeNode` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `NuiKr.OpenPoseEditor` —— 1/6 个有
- `OpenposePreprocessor` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：NuiKr.OpenPoseEditor
