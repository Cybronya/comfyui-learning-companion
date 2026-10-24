---
name: text_to_image_sampler_clip_unet_73
type: Text To Image
frequency: 9
level: moderate
coverage: 0.950222
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/ComfyUI_桌布V3_2053374663803326465.json, 图片生成/文生图/ERNIE-Image  百度团队的文生图模型80亿参数_2044578596047560706.json, 图片生成/文生图/ERNIE-Image  百度团队的文生图模型80亿参数_2047608589782622210.json, 图片生成/文生图/ERNIE-Image  百度团队的文生图模型80亿参数_2069658196112920577.json, 图片生成/文生图/ERNIE-Image-文生图_2044602654369783809.json, 图片生成/文生图/Krea2-turbo文生图3D国漫CG场景_2085325906326937602.json, 图片生成/文生图/Krea2-turbo文生图3D国漫CG风格_2089394677895221249.json, 图片生成/文生图/Krea2-turbo文生图超写实真人摄影风格_2089316645973086210.json, 图片生成/文生图/N-Super Z-image 3.0+lota文生图_2020339880995332097.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_73

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/ComfyUI_桌布V3_2053374663803326465.json、图片生成/文生图/ERNIE-Image  百度团队的文生图模型80亿参数_2044578596047560706.json、图片生成/文生图/ERNIE-Image  百度团队的文生图模型80亿参数_2047608589782622210.json、图片生成/文生图/ERNIE-Image  百度团队的文生图模型80亿参数_2069658196112920577.json、图片生成/文生图/ERNIE-Image-文生图_2044602654369783809.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 8/9 个有
- `Text` —— 4/9 个有
- `ConditioningKrea2Rebalance` —— 2/9 个有
- `PrimitiveInt` —— 2/9 个有
- `DuckHideNode` —— 1/9 个有
- `LoadImage` —— 1/9 个有
- `TextEncodeQwenImageEditPlus` —— 1/9 个有
- `easy imageScaleDownToSize` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 4 - 20 | 9 | 53% |
| Prompt 约束强度(CFG) | 2 | 1 - 4 | 9 | 42% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1080 | 1024 - 1920 | 9 | 72% |
| 高度 | 1536 | 1024 - 1920 | 9 | 77% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，观测区间 4 - 20，9 个样本
- Prompt 约束强度(CFG) 中位数 2，观测区间 1 - 4，9 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1024 - 1920，9 个样本
- 高度 中位数 1536，观测区间 1024 - 1920，9 个样本
