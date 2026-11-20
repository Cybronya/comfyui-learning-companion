---
name: text_to_image_sampler_clip_unet_38
type: Text To Image
frequency: 14
level: strong
coverage: 0.943214
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image-turbo ControNet文生图姿势控制_2045229213636108290.json, 图片生成/文生图/Z-image-turbo-文生图（开源之王）_1997492012880433154.json, 图片生成/文生图/Z-image文生图_1993860574876467201.json, 图片生成/文生图/Z-image文生图_1993881668454907906.json, 图片生成/文生图/Z-image文生图_1993883811278684161.json, 图片生成/文生图/Z-image文生图_1993952320304201730.json, 图片生成/文生图/Z-image文生图_1994050196562706434.json, 图片生成/文生图/Z-image文生图_1994253056955138050.json, 图片生成/文生图/Z-image文生图_1994323420024422402.json, 图片生成/文生图/Z-image文生图——25年末的超级王炸_1994392372287053826.json, 图片生成/文生图/Z_image_turbo快速文生图 自用版_2097176754392756226.json, 图片生成/文生图/Z_image_turbo快速文生图_2051577152918835202.json, 图片生成/文生图/krea2 Lora文生图加英伟达rtx nodes高清放大_2074689431730221057.json, 图片生成/文生图/z-image超写实逼真人物生成_2031760767321640962.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_38

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Z-image-turbo ControNet文生图姿势控制_2045229213636108290.json、图片生成/文生图/Z-image-turbo-文生图（开源之王）_1997492012880433154.json、图片生成/文生图/Z-image文生图_1993860574876467201.json、图片生成/文生图/Z-image文生图_1993881668454907906.json、图片生成/文生图/Z-image文生图_1993883811278684161.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 13/14 个有
- `PreviewImage` —— 4/14 个有
- `LoadImage` —— 3/14 个有
- `RTXVideoSuperResolution` —— 3/14 个有
- `ModelPatchLoader` —— 2/14 个有
- `QwenImageDiffsynthControlnet` —— 2/14 个有
- `AIO_Preprocessor` —— 1/14 个有
- `Fast Groups Bypasser (rgthree)` —— 1/14 个有
- `ImageScale` —— 1/14 个有
- `ImageScaleToTotalPixels` —— 1/14 个有
- `LoraLoaderModelOnly` —— 1/14 个有
- `SetUnionControlNetType` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 12 | 14 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 1084 | 688 - 1920 | 14 | 70% |
| 高度 | 1600 | 1080 - 1920 | 14 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 12，14 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 1084，观测区间 688 - 1920，14 个样本
- 高度 中位数 1600，观测区间 1080 - 1920，14 个样本，取值集中（一致性 80%）
