---
name: text_to_image_lora_sampler_clip_87
type: Text To Image
frequency: 11
level: strong
coverage: 0.886091
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/VOSR2超分放大 文生图高清增强处理工具_2098709966747160578.json, 图片生成/文生图/Z Image文生图标准版工作流，高质量文本到图像生成方案_2105786409570361346.json, 图片生成/文生图/Z-Image Turbo文生图快速高质量处理工具_2101047351329771521.json, 图片生成/文生图/Z-Image-Turbo文生图｜高速出图质量在线新体验_2105251524116041729.json, 图片生成/文生图/Z-image文生图 多风格高质量图片生成_2098860674293260290.json, 图片生成/文生图/Z-image真实文生图｜人像写真美少女高质量生成_2096726231373930498.json, 图片生成/文生图/ZIT基础文生图工作流，高质量文本到图像生成方案_2106810710041911298.json, 图片生成/文生图/去AI感增强真实感工作流，MiniMax H3 LTX Wan图生视频动作迁移多合一_2103189879533424642.json, 图片生成/文生图/没有AI味文生图｜Z-image Turbo真实模型工作流_2093450819793408001.json, 图片生成/文生图/没有AI味的模型｜Z-image Tubro文生图一键生成_2093784427087360002.json, 图片生成/文生图/背景图批量出图神器｜文生图一句提示词直出，场景背景素材随心换_2100476653272129538.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_87

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/VOSR2超分放大 文生图高清增强处理工具_2098709966747160578.json、图片生成/文生图/Z Image文生图标准版工作流，高质量文本到图像生成方案_2105786409570361346.json、图片生成/文生图/Z-Image Turbo文生图快速高质量处理工具_2101047351329771521.json、图片生成/文生图/Z-Image-Turbo文生图｜高速出图质量在线新体验_2105251524116041729.json、图片生成/文生图/Z-image文生图 多风格高质量图片生成_2098860674293260290.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 8/11 个有
- `ConditioningZeroOut` —— 6/11 个有
- `ModelSamplingAuraFlow` —— 6/11 个有
- `PreviewImage` —— 3/11 个有
- `VHS_LoadVideo` —— 2/11 个有
- `VHS_VideoCombine` —— 2/11 个有
- `VOSR2ModelLoader` —— 2/11 个有
- `VOSR2Upscale` —— 2/11 个有
- `CompressImages` —— 1/11 个有
- `RHHiddenNodes` —— 1/11 个有
- `ResolutionSelector` —— 1/11 个有
- `Text Multiline` —— 1/11 个有
- `VHS_VideoInfoLoaded` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（19/11 个样本）：Steps较低可能导致细节不足
