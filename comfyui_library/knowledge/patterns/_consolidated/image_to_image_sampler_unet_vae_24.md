---
name: image_to_image_sampler_unet_vae_24
type: Image To Image
frequency: 9
level: moderate
coverage: 0.933889
common_nodes: [CLIPLoader, ConditioningZeroOut, ImageScaleToTotalPixels, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-klein角色替换_2012312687472025602.json, 图片生成/图生图/Z-image增加人物质感_1993876234681729025.json, 图片生成/图生图/cad平面图转彩图-室内设计专用-Flux2-klein_2012841471073853441.json, 图片生成/图生图/室内-klein-平面图转彩图工作流_2040793589877317633.json, 图片生成/图生图/穿上服装 2511_2020420989573664769.json, 图片生成/图生图/站立拍摄 2511_2037007001368141825.json, 图片生成/图生图/蹲拍 2511_2036798331170594817.json, 图片生成/文生图/万物cheems狗-qwen_1960294148945358849.json, 图片生成/文生图/双胞胎 2511_2027523066724618241.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_24

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Flux2-klein角色替换_2012312687472025602.json、图片生成/图生图/Z-image增加人物质感_1993876234681729025.json、图片生成/图生图/cad平面图转彩图-室内设计专用-Flux2-klein_2012841471073853441.json、图片生成/图生图/室内-klein-平面图转彩图工作流_2040793589877317633.json、图片生成/图生图/穿上服装 2511_2020420989573664769.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ReferenceLatent` —— 8/9 个有
- `JjkText` —— 6/9 个有
- `PIP_图像联结` —— 6/9 个有
- `CFGNorm` —— 5/9 个有
- `EmptyLatentImage` —— 5/9 个有
- `LoraLoaderModelOnly` —— 5/9 个有
- `ModelSamplingAuraFlow` —— 5/9 个有
- `TextEncodeQwenImageEditPlus` —— 5/9 个有
- `CLIPTextEncode` —— 4/9 个有
- `MultiTextConcatenate` —— 4/9 个有
- `RH_Captioner` —— 3/9 个有
- `LatentUpscaleBy` —— 2/9 个有
- `PreviewAny` —— 2/9 个有
- `easy imageConcat` —— 2/9 个有
- `CR Prompt List` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `RMBG` —— 1/9 个有
- `easy anythingIndexSwitch` —— 1/9 个有
- `easy int` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 9 | 63% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 0.2 - 1 | 9 | 72% |
| 宽度 | 928 | 928 - 1024 | 5 | 95% |
| 高度 | 1664 | 1024 - 1664 | 5 | 84% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 0.2 - 1，9 个样本
- 宽度 中位数 928，观测区间 928 - 1024，5 个样本，取值集中（一致性 95%）
- 高度 中位数 1664，观测区间 1024 - 1664，5 个样本，取值集中（一致性 84%）
- 高发问题（8/9 个样本）：Steps较低可能导致细节不足
