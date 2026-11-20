---
name: text_to_image_sampler_clip_unet_172
type: Text To Image
frequency: 4
level: strong
coverage: 0.87475
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image-turbo ControNet文生图姿势控制_2045229213636108290.json, 图片生成/文生图/Z-image-turbo+D-opsd-文生图_2056751759552503810.json, 图片生成/文生图/krea2-trubo-青绿水彩风格+水墨风格+光影效果彩色极简素描风格_2069757903887753218.json, 图片生成/文生图/z-image超写实逼真人物生成_2031760767321640962.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_172

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-image-turbo ControNet文生图姿势控制_2045229213636108290.json、图片生成/文生图/Z-image-turbo+D-opsd-文生图_2056751759552503810.json、图片生成/文生图/krea2-trubo-青绿水彩风格+水墨风格+光影效果彩色极简素描风格_2069757903887753218.json、图片生成/文生图/z-image超写实逼真人物生成_2031760767321640962.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `ModelPatchLoader` —— 2/4 个有
- `QwenImageDiffsynthControlnet` —— 2/4 个有
- `AIO_Preprocessor` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `ImageScale` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `SetUnionControlNetType` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1084 | 1024 - 1536 | 4 | 83% |
| 高度 | 1536 | 1280 - 1920 | 4 | 85% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1084，观测区间 1024 - 1536，4 个样本，取值集中（一致性 83%）
- 高度 中位数 1536，观测区间 1280 - 1920，4 个样本，取值集中（一致性 85%）
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足
