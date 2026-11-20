---
name: text_to_image_sampler_clip_unet_73
type: Text To Image
frequency: 10
level: moderate
coverage: 0.9185
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/ComfyUI_桌布V3_2053374663803326465.json, 图片生成/文生图/ERNIE-Image  百度团队的文生图模型80亿参数_2044578596047560706.json, 图片生成/文生图/ERNIE-Image  百度团队的文生图模型80亿参数_2047608589782622210.json, 图片生成/文生图/ERNIE-Image  百度团队的文生图模型80亿参数_2069658196112920577.json, 图片生成/文生图/ERNIE-Image-文生图_2044602654369783809.json, 图片生成/文生图/KREA2-CC人像版_2095722389442224130.json, 图片生成/文生图/N-Super Z-image 3.0+lota文生图_2020339880995332097.json, 图片生成/文生图/Zimage-ART文生图_2017256373024722946.json, 图片生成/文生图/（贞贞版）Z image Art文生图_2017605115783421953.json, 平台全量/溶图打光图片加光影qwenplus加速版_1973212898661109761.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_73

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/ComfyUI_桌布V3_2053374663803326465.json、图片生成/文生图/ERNIE-Image  百度团队的文生图模型80亿参数_2044578596047560706.json、图片生成/文生图/ERNIE-Image  百度团队的文生图模型80亿参数_2047608589782622210.json、图片生成/文生图/ERNIE-Image  百度团队的文生图模型80亿参数_2069658196112920577.json、图片生成/文生图/ERNIE-Image-文生图_2044602654369783809.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 9/10 个有
- `PrimitiveInt` —— 4/10 个有
- `Text` —— 4/10 个有
- `LoadImage` —— 2/10 个有
- `TextEncodeQwenImageEditPlus` —— 2/10 个有
- `DuckHideNode` —— 1/10 个有
- `GetImageSize` —— 1/10 个有
- `Seed (rgthree)` —— 1/10 个有
- `easy imageConcat` —— 1/10 个有
- `easy imageScaleDownToSize` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | 4 - 30 | 10 | 46% |
| Prompt 约束强度(CFG) | 3 | 1 - 4 | 10 | 45% |
| 采样算法 | euler | - | 10 | 80% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 1080 | 1024 - 1920 | 10 | 77% |
| 高度 | 1536 | 1024 - 1984 | 10 | 76% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 16，观测区间 4 - 30，10 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 4，10 个样本，取值分散，一致性仅 45%
- 采样算法 最常用 euler，10 个样本，一致性 80%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1024 - 1920，10 个样本
- 高度 中位数 1536，观测区间 1024 - 1984，10 个样本
