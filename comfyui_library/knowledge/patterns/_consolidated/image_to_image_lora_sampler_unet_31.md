---
name: image_to_image_lora_sampler_unet_31
type: Image To Image
frequency: 14
level: weak
coverage: 0.968143
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image-edit线图或插图直接转换3D真实图_1981531839686942721.json, 图片生成/图生图/QwenEdit图片编辑+1个流的多玩法_1959226835055882241.json, 图片生成/图生图/qwen_edit_一键Chibi角色风格转换 Q版风格化_1980449032965435394.json, 图片生成/图生图/人物服装提取_2000685930392547330.json, 图片生成/图生图/真人转动漫  真人转卡通 真人转漫画   真人转3D Q版卡通_2053882425570275329.json, 图片生成/图生图/真人转动漫  真人转卡通 真人转漫画   真人转3D Q版卡通_2053887409280045058.json, 图片生成/图生图/真人转动漫  真人转卡通 真人转漫画   真人转3D Q版卡通_2053906302581125121.json, 图片生成/图生图/真人转卡通 真人转漫画 真人转动漫  真人转3D Q版卡通_2053640385771122690.json, 图片生成/图生图/真人转卡通 真人转漫画 真人转动漫  真人转3D Q版卡通_2053861700239151106.json, 图片生成/图生图/真人转漫画 真人转动漫  Q版卡通  Q版风格化_2053635738796867585.json, 图片生成/图生图/真人转漫画 真人转动漫  真人转3D Q版卡通  Q版风格化_2053637683863400450.json, 图片生成/图生图/真人转漫画 真人转动漫  真人转3D Q版卡通  Q版风格化_2061046452033507329.json, 图片生成/图生图/真人转漫画_2108503903443705858.json, 图片生成/文生图/Qwen-Image-Edit-一键转宫崎骏风_2095060097503420418.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_31

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Qwen-image-edit线图或插图直接转换3D真实图_1981531839686942721.json、图片生成/图生图/QwenEdit图片编辑+1个流的多玩法_1959226835055882241.json、图片生成/图生图/qwen_edit_一键Chibi角色风格转换 Q版风格化_1980449032965435394.json、图片生成/图生图/人物服装提取_2000685930392547330.json、图片生成/图生图/真人转动漫  真人转卡通 真人转漫画   真人转3D Q版卡通_2053882425570275329.json…）

- **类型**：Image To Image
- **样本数**：14
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 13/14 个有
- `TextEncodeQwenImageEdit` —— 13/14 个有
- `ImageScaleToTotalPixels` —— 12/14 个有
- `CR Simple Image Compare` —— 11/14 个有
- `Image Comparer (rgthree)` —— 3/14 个有
- `JjkText` —— 2/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/14 个有
- `AILab_ImageStitch` —— 1/14 个有
- `TextEncodeQwenImageEditEnhanced` —— 1/14 个有
- `easy cleanGpuUsed` —— 1/14 个有
- `easy imageSave` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 14 | 54% |
| Prompt 约束强度(CFG) | 1 | 0.47 - 8 | 14 | 0% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，14 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 0.47 - 8，14 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0.47，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 高发问题（13/14 个样本）：Steps较低可能导致细节不足
