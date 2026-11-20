---
name: image_to_image_sampler_clip_unet_135
type: Image To Image
frequency: 5
level: weak
coverage: 0.9834
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image Base 图像放大细节修复ComfyUI工作流_2033567937352704002.json, 图片生成/文生图/文生图-直出4K-速度更快-效果更好Z-Image_2114241540112601090.json, 图片生成/文生图/空白工作流模板｜文生图自由搭建创作的起点画布_2114768132446445570.json, 平台全量/flux2-klein-auto_inpaint_advanced_2085255128151580673.json, 平台全量/光影融合_2037003058072260609.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_135

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Z-Image Base 图像放大细节修复ComfyUI工作流_2033567937352704002.json、图片生成/文生图/文生图-直出4K-速度更快-效果更好Z-Image_2114241540112601090.json、图片生成/文生图/空白工作流模板｜文生图自由搭建创作的起点画布_2114768132446445570.json、平台全量/flux2-klein-auto_inpaint_advanced_2085255128151580673.json、平台全量/光影融合_2037003058072260609.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ReferenceLatent` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `ConditioningClamp` —— 1/5 个有
- `EmptyImage` —— 1/5 个有
- `LatentUpscaleBy` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `Textbox` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 20 | 5 | 45% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 5 | 0% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 0.15 - 1 | 5 | 59% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 20，5 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，5 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.15 - 1，5 个样本
