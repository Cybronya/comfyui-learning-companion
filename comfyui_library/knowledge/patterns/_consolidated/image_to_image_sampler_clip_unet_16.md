---
name: image_to_image_sampler_clip_unet_16
type: Image To Image
frequency: 12
level: moderate
coverage: 0.90475
common_nodes: [CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX.2-Klein_镜头角度编辑_2024306802296360961.json, 图片生成/图生图/FLUX.2-Klein图生图洗图工作流_2068593056466694146.json, 图片生成/图生图/FLUX2洗图工作流_2000578105506922497.json, 图片生成/图生图/FLUX3图像编辑_2110915403957497858.json, 图片生成/图生图/Flux-2 Klein 双图编辑_2093268073829724161.json, 图片生成/图生图/Flux2-Klein-9B-万物精修_2016119793451016194.json, 图片生成/图生图/Flux2-Klein-9B-毛坯图转效果图_2016119803773198338.json, 图片生成/图生图/Flux2-klein-万物精修（产品盒标贴一致性）_2036777306714279938.json, 图片生成/图生图/Kontext一键转为动漫风格（主体特征不变）_1991802548898328578.json, 图片生成/图生图/kontext_dev一键扩图_1952734346315821058.json, 图片生成/图生图/精修天花板Flux2-klein-万物精修_2017956716545056769.json, 图片生成/文生图/空白工作流_2085537334258393089.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_16

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/FLUX.2-Klein_镜头角度编辑_2024306802296360961.json、图片生成/图生图/FLUX.2-Klein图生图洗图工作流_2068593056466694146.json、图片生成/图生图/FLUX2洗图工作流_2000578105506922497.json、图片生成/图生图/FLUX3图像编辑_2110915403957497858.json、图片生成/图生图/Flux-2 Klein 双图编辑_2093268073829724161.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 11/12 个有
- `CLIPLoader` —— 10/12 个有
- `ReferenceLatent` —— 10/12 个有
- `Image Comparer (rgthree)` —— 9/12 个有
- `FluxKontextImageScale` —— 6/12 个有
- `ColorMatch` —— 4/12 个有
- `EmptyFlux2LatentImage` —— 3/12 个有
- `FluxGuidance` —— 3/12 个有
- `DualCLIPLoader` —— 2/12 个有
- `ImagePadForOutpaint` —— 2/12 个有
- `ImageResizeKJv2` —— 2/12 个有
- `CR Prompt List` —— 1/12 个有
- `DrawMaskOnImage` —— 1/12 个有
- `ImageScale` —— 1/12 个有
- `LayerUtility: NanoBananaImageScale` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 5 - 22 | 12 | 37% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 0.95 | 0.5 - 1 | 12 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 5 - 22，12 个样本，取值分散，一致性仅 37%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 0.95，观测区间 0.5 - 1，12 个样本，取值集中（一致性 82%）
- 高发问题（10/12 个样本）：Steps较低可能导致细节不足
