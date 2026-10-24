---
name: image_to_image_controlnet_sampler_clip_4
type: Image To Image
frequency: 8
level: moderate
coverage: 0.830875
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetApplyAdvanced, ControlNetLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/nunchaku qwen加速姿态迁移_1969261471488241666.json, 图片生成/图生图/nunchaku双截棍加速 qwen-image-edit 千问姿态迁移工作流_1970131353419345921.json, 图片生成/图生图/人物姿态迁移qwen版 单人使用版_1970816529736605698.json, 图片生成/文生图/QWen-Image多合一控制引导_Instantx-Controlnet_1960651156605272065.json, 图片生成/文生图/controlnet—千问教学工作流_1994239870906417154.json, 图片生成/文生图/qwen-毛坯房一键精装图_1994410356925665282.json, 图片生成/文生图/千问Qwen-Image多合一控制_Instantx-Controlnet_1961110552913362946.json, 图片生成/文生图/🦖QWen-Image Controlnet多合一生图_1961690453156499458.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_4

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/nunchaku qwen加速姿态迁移_1969261471488241666.json、图片生成/图生图/nunchaku双截棍加速 qwen-image-edit 千问姿态迁移工作流_1970131353419345921.json、图片生成/图生图/人物姿态迁移qwen版 单人使用版_1970816529736605698.json、图片生成/文生图/QWen-Image多合一控制引导_Instantx-Controlnet_1960651156605272065.json、图片生成/文生图/controlnet—千问教学工作流_1994239870906417154.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 7/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `UNETLoader` —— 6/8 个有
- `AIO_Preprocessor` —— 5/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/8 个有
- `DWPreprocessor` —— 4/8 个有
- `ImageScaleDownToSize` —— 3/8 个有
- `ImageStitch` —— 3/8 个有
- `TextEncodeQwenImageEdit` —— 3/8 个有
- `Canny` —— 2/8 个有
- `Image Comparer (rgthree)` —— 2/8 个有
- `NunchakuQwenImageDiTLoader` —— 2/8 个有
- `SetUnionControlNetType` —— 2/8 个有
- `ImageConcatMulti` —— 1/8 个有
- `PMRF` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | 0.75 - 2 | 8 | 64% |
| 采样步数 | 9 | 4 - 20 | 8 | 49% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 8 | 54% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 1，观测区间 0.75 - 2，8 个样本
- 采样步数 中位数 9，观测区间 4 - 20，8 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（4/8 个样本）：Steps较低可能导致细节不足
